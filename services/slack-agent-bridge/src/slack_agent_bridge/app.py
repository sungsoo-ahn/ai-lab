from __future__ import annotations

import argparse
import logging
import os
import re
import subprocess
import tempfile
import threading
from pathlib import Path
from typing import Any

HOME = Path.home()
ACCOUNT_PROMPT = "Use the account agent setup. Read ~/AGENTS.md and continue from ~/agent-system."
DEFAULT_CODEX_TIMEOUT_SECONDS = 900
MAX_SLACK_MESSAGE_CHARS = 3500

MENTION_RE = re.compile(r"<@[A-Z0-9]+>")


def configure_logging() -> None:
    logging.basicConfig(
        level=os.getenv("SLACK_AGENT_LOG_LEVEL", "INFO"),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )


def clean_slack_text(text: str) -> str:
    text = MENTION_RE.sub("", text)
    return re.sub(r"\s+", " ", text).strip()


def build_codex_prompt(user_text: str, *, slack_user: str | None, channel: str) -> str:
    return "\n".join(
        [
            ACCOUNT_PROMPT,
            "",
            "You are responding to a Slack message. Keep the final answer concise and Slack-readable.",
            "Do not write to Slack, Gmail, Drive, Calendar, or any other external connector yourself.",
            "If a connector write is needed, ask for explicit approval in your final answer.",
            f"Slack user: {slack_user or 'unknown'}",
            f"Slack channel: {channel}",
            "",
            "User message:",
            user_text,
        ]
    )


def run_codex(user_text: str, *, slack_user: str | None, channel: str, timeout_seconds: int) -> str:
    prompt = build_codex_prompt(user_text, slack_user=slack_user, channel=channel)

    with tempfile.NamedTemporaryFile(prefix="slack-agent-", suffix=".txt") as output_file:
        cmd = [
            "codex",
            "--ask-for-approval",
            "never",
            "--search",
            "exec",
            "--cd",
            str(HOME),
            "--skip-git-repo-check",
            "--output-last-message",
            output_file.name,
            "-",
        ]
        completed = subprocess.run(
            cmd,
            input=prompt,
            text=True,
            capture_output=True,
            timeout=timeout_seconds,
            check=False,
        )

        output = Path(output_file.name).read_text(encoding="utf-8", errors="replace").strip()

    if completed.returncode == 0 and output:
        return output

    stderr = completed.stderr.strip()
    stdout = completed.stdout.strip()
    details = stderr or stdout or f"codex exited with status {completed.returncode}"
    return f"Codex did not return a final message.\n\n```{truncate(details, 1200)}```"


def truncate(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 20].rstrip() + "\n... truncated ..."


def split_for_slack(text: str) -> list[str]:
    text = text.strip() or "(empty response)"
    chunks: list[str] = []
    remaining = text
    while len(remaining) > MAX_SLACK_MESSAGE_CHARS:
        split_at = remaining.rfind("\n\n", 0, MAX_SLACK_MESSAGE_CHARS)
        if split_at < 500:
            split_at = remaining.rfind("\n", 0, MAX_SLACK_MESSAGE_CHARS)
        if split_at < 500:
            split_at = MAX_SLACK_MESSAGE_CHARS
        chunks.append(remaining[:split_at].strip())
        remaining = remaining[split_at:].strip()
    if remaining:
        chunks.append(remaining)
    return chunks


def post_response(client: Any, *, channel: str, thread_ts: str, text: str) -> None:
    for chunk in split_for_slack(text):
        client.chat_postMessage(channel=channel, thread_ts=thread_ts, text=chunk)


def handle_prompt_async(
    *,
    client: Any,
    channel: str,
    thread_ts: str,
    user_text: str,
    slack_user: str | None,
    timeout_seconds: int,
    logger: logging.Logger,
) -> None:
    def worker() -> None:
        try:
            response = run_codex(
                user_text,
                slack_user=slack_user,
                channel=channel,
                timeout_seconds=timeout_seconds,
            )
        except subprocess.TimeoutExpired:
            response = f"Codex timed out after {timeout_seconds} seconds."
        except Exception:
            logger.exception("failed to handle Slack prompt")
            response = "The Slack agent bridge hit a local error while running Codex."

        post_response(client, channel=channel, thread_ts=thread_ts, text=response)

    threading.Thread(target=worker, daemon=True).start()


def create_app(timeout_seconds: int) -> Any:
    from slack_bolt import App

    app = App(token=os.environ["SLACK_BOT_TOKEN"])
    logger = logging.getLogger("slack_agent_bridge")

    def dispatch(event: dict[str, Any], client: Any) -> None:
        if event.get("bot_id") or event.get("subtype"):
            return

        text = clean_slack_text(event.get("text", ""))
        channel = event.get("channel")
        ts = event.get("ts")
        user = event.get("user")

        if not text or not channel or not ts:
            return

        thread_ts = event.get("thread_ts") or ts
        client.chat_postMessage(channel=channel, thread_ts=thread_ts, text="Working on it.")
        handle_prompt_async(
            client=client,
            channel=channel,
            thread_ts=thread_ts,
            user_text=text,
            slack_user=user,
            timeout_seconds=timeout_seconds,
            logger=logger,
        )

    @app.event("app_mention")
    def handle_app_mention(event: dict[str, Any], client: Any) -> None:
        dispatch(event, client)

    @app.event("message")
    def handle_direct_message(event: dict[str, Any], client: Any) -> None:
        if event.get("channel_type") == "im":
            dispatch(event, client)

    return app


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the Slack Socket Mode bridge for Codex.")
    parser.add_argument(
        "--timeout",
        type=int,
        default=int(os.getenv("SLACK_AGENT_CODEX_TIMEOUT", DEFAULT_CODEX_TIMEOUT_SECONDS)),
        help="Maximum seconds to wait for a Codex response.",
    )
    return parser.parse_args()


def main() -> None:
    configure_logging()
    args = parse_args()

    missing = [name for name in ("SLACK_BOT_TOKEN", "SLACK_APP_TOKEN") if not os.getenv(name)]
    if missing:
        raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")

    from slack_bolt.adapter.socket_mode import SocketModeHandler

    app = create_app(timeout_seconds=args.timeout)
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()


if __name__ == "__main__":
    main()
