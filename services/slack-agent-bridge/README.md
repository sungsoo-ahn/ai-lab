# Slack Agent Bridge

Local Slack Socket Mode bridge for the account Codex agent.

## Slack App Setup

Create a Slack app and configure:

- Socket Mode: enabled
- App-level token: `connections:write`
- Bot token scopes:
  - `chat:write`
  - `app_mentions:read`
  - `im:history`
- Event subscriptions:
  - `app_mention`
  - `message.im`

Install the app to the workspace and invite it to any channel where mentions should work.

## Run

Export tokens in your shell. Do not save token values in this repository.

```sh
export SLACK_APP_TOKEN='xapp-...'
export SLACK_BOT_TOKEN='xoxb-...'
/Users/sungs/agent-system/services/slack-agent-bridge/scripts/run-slack-agent-bridge
```

Optional timeout:

```sh
SLACK_AGENT_CODEX_TIMEOUT=1200 scripts/run-slack-agent-bridge
```

## Behavior

- Direct messages to the app are sent to Codex.
- Channel mentions are sent to Codex after the bot mention is removed.
- The bridge posts an immediate acknowledgment, then posts the final Codex answer in the same Slack thread.
- Slack tokens, message bodies, and Codex outputs are not written to durable memory by this service.

## Local Verification

```sh
uv sync
PYTHONPATH=src uv run --no-sync python -m unittest discover -s tests -v
PYTHONPATH=src uv run --no-sync python -m slack_agent_bridge.app --help
```
