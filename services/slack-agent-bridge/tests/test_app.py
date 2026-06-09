from __future__ import annotations

import unittest

from slack_agent_bridge.app import (
    ACCOUNT_PROMPT,
    MAX_SLACK_MESSAGE_CHARS,
    build_codex_prompt,
    clean_slack_text,
    post_response,
    split_for_slack,
    truncate,
)


class FakeSlackClient:
    def __init__(self) -> None:
        self.messages: list[dict[str, str]] = []

    def chat_postMessage(self, **kwargs: str) -> None:
        self.messages.append(kwargs)


class SlackAgentBridgeTests(unittest.TestCase):
    def test_clean_slack_text_removes_mentions_and_normalizes_spacing(self) -> None:
        self.assertEqual(
            clean_slack_text("<@U123ABC>   build this\n\nplease"),
            "build this please",
        )

    def test_build_codex_prompt_includes_slack_safety_context(self) -> None:
        prompt = build_codex_prompt("Build a prototype.", slack_user="U1", channel="D1")

        self.assertIn(ACCOUNT_PROMPT, prompt)
        self.assertIn("Do not write to Slack, Gmail, Drive, Calendar", prompt)
        self.assertIn("Slack user: U1", prompt)
        self.assertIn("Slack channel: D1", prompt)
        self.assertTrue(prompt.endswith("Build a prototype."))

    def test_truncate_leaves_short_text_unchanged(self) -> None:
        self.assertEqual(truncate("short", 10), "short")

    def test_truncate_shortens_long_text_with_marker(self) -> None:
        self.assertEqual(truncate("abcdef", 5), "\n... truncated ...")

    def test_split_for_slack_preserves_short_message(self) -> None:
        self.assertEqual(split_for_slack("hello"), ["hello"])

    def test_split_for_slack_chunks_long_message(self) -> None:
        text = ("a" * (MAX_SLACK_MESSAGE_CHARS - 10)) + "\n\n" + ("b" * 30)
        chunks = split_for_slack(text)

        self.assertEqual(len(chunks), 2)
        self.assertLessEqual(len(chunks[0]), MAX_SLACK_MESSAGE_CHARS)
        self.assertEqual(chunks[1], "b" * 30)

    def test_post_response_sends_all_chunks_to_thread(self) -> None:
        client = FakeSlackClient()
        text = "x" * (MAX_SLACK_MESSAGE_CHARS + 10)

        post_response(client, channel="D1", thread_ts="123.4", text=text)

        self.assertEqual(len(client.messages), 2)
        self.assertEqual(client.messages[0]["channel"], "D1")
        self.assertEqual(client.messages[0]["thread_ts"], "123.4")


if __name__ == "__main__":
    unittest.main()
