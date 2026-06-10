# Slack Agent Bridge Proposal

Date: 2026-06-09

## Goal

Allow the user to talk to the local account agent from Slack using a private Slack app.

## Recommended Approach

Build a small Python service under `ai-lab` that uses Slack Socket Mode and Bolt for Python. Socket Mode avoids exposing a public HTTP endpoint; the local process connects outbound to Slack over WebSocket and receives app events.

The bridge should:

- listen for direct messages to the Slack app and direct mentions in channels;
- pass each prompt to the existing `codex-agent` account launcher through `codex exec`;
- reply in the same Slack thread or DM;
- avoid storing Slack tokens, user message bodies, or Codex output in durable memory by default;
- keep logs limited to timestamps, event IDs, and status.

## Slack App Requirements

Create or configure a Slack app with:

- Socket Mode enabled;
- app-level token with `connections:write`;
- bot token scopes:
  - `chat:write` to reply;
  - `app_mentions:read` for channel mentions;
  - `im:history` for direct messages;
- event subscriptions:
  - `app_mention`;
  - `message.im`.

Tokens should be provided at runtime through environment variables, not committed to files:

- `SLACK_APP_TOKEN` for the app-level token;
- `SLACK_BOT_TOKEN` for the bot token.

## Proposed Local Changes

Create a Python project at:

`<repo>/services/slack-agent-bridge/`

Files:

- `pyproject.toml`
- `uv.lock`
- `README.md`
- `src/slack_agent_bridge/__init__.py`
- `src/slack_agent_bridge/app.py`
- `scripts/run-slack-agent-bridge`

Dependencies:

- `slack-bolt`
- `slack-sdk`

No Homebrew, Node, Docker, or global Python package changes are required.

## Exact Commands

After approval:

```sh
mkdir -p <repo>/services/slack-agent-bridge
cd <repo>/services/slack-agent-bridge
uv init --package --name slack-agent-bridge
uv add slack-bolt slack-sdk
uv run python -m slack_agent_bridge.app
```

The implementation may use direct file creation instead of `uv init` if that keeps the generated project smaller and more controlled, but dependency resolution should still be done with `uv lock` or `uv sync`.

## Risk And Privacy Impact

Risk:

- Slack messages will be sent to local Codex as prompts.
- Codex may run local tools according to the current Codex approval and sandbox settings.
- Long-running Codex tasks may exceed Slack response expectations unless the bridge acknowledges quickly and posts the final response later.

Privacy:

- Do not store Slack token values.
- Do not persist raw Slack message bodies or Codex responses by default.
- Connector writes remain governed by account policy and require explicit user approval.

## Rollback

Remove the local service directory:

```sh
rm -rf <repo>/services/slack-agent-bridge
```

In Slack, disable Socket Mode or uninstall/delete the Slack app.

## Verification

Local:

```sh
uv sync
uv run python -m slack_agent_bridge.app --help
```

Slack:

- send a direct message to the app;
- mention the app in a channel where it has been invited;
- confirm the response appears in the same DM or thread.

## Source Map

- Slack Socket Mode docs: `https://docs.slack.dev/apis/events-api/using-socket-mode`
- Bolt for Python Socket Mode docs: `https://docs.slack.dev/tools/bolt-python/concepts/socket-mode`
- `app_mention` event docs: `https://docs.slack.dev/reference/events/app_mention/`
- `message.im` event docs: `https://docs.slack.dev/reference/events/message.im`
- `chat.postMessage` docs: `https://docs.slack.dev/reference/methods/chat.postMessage`
