# AI Lab Dashboard

Static dashboard generator for `/Users/sungs/ai-lab`.

## Build

```sh
cd /Users/sungs/ai-lab/dashboard
uv run python src/agent_dashboard/generate.py
```

The generated site is written to `dashboard/dist/`.

## Preview

```sh
cd /Users/sungs/ai-lab/dashboard
uv run python src/agent_dashboard/generate.py --serve
```

Then open `http://127.0.0.1:8008/`.

## Design

The visual direction is a calm scientific workspace: warm neutral surfaces,
dark green text, muted green accents, compact cards, metric strips, and readable technical reports.
