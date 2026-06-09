# Agent System Dashboard

Static dashboard generator for `/Users/sungs/agent-system`.

## Build

```sh
cd /Users/sungs/agent-system/dashboard
uv run python src/agent_dashboard/generate.py
```

The generated site is written to `dashboard/dist/`.

## Preview

```sh
cd /Users/sungs/agent-system/dashboard
uv run python src/agent_dashboard/generate.py --serve
```

Then open `http://127.0.0.1:8008/`.

## Design

The visual direction is inspired by Rowan's calm scientific SaaS style:
warm neutral surfaces, dark green text, muted green accents, compact cards,
metric strips, and readable technical reports.
