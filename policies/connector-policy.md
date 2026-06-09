# Connector Policy

## Read Access

The research agent may use web, Google Drive, Gmail, Google Calendar, and Slack for targeted read-only retrieval when the source is relevant to the user's task.

Read only the amount needed to answer the question. Prefer narrow searches and bounded date ranges for personal or work connectors.

## Write Access

The agent must ask before any connector write, including:

- creating, editing, moving, or deleting Drive files;
- creating Gmail drafts, labels, filters, sends, or archive/delete actions;
- creating, editing, or deleting Calendar events;
- sending Slack messages, creating drafts, creating canvases, or changing channels.

Local writes under `/Users/sungs/agent-system` do not require additional approval unless the user requests a read-only session.

## Summaries

Summarize connector content only as needed. Avoid copying full private messages, emails, calendar details, or document passages into durable local memory.

