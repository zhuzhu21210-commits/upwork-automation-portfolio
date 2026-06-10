# Zapier Trello to Google Calendar Workflow

This sample describes a focused first milestone for a Zapier workflow that turns
Trello card data into Google Calendar events, with optional Gmail and Google
Drive handoff steps.

It is designed for clients who need a clean automation before expanding into
Xero, Drive filing, or multi-Zap operational workflows.

## First Milestone Scope

- confirm Trello trigger board, list, label, and due-date rules
- map Trello fields into Google Calendar event title, time, description, and
  links
- create one working Zap or multi-step Zap
- add a simple error log or manual review path for missing dates
- document field mapping and limitations

## Example Field Map

| Source | Example Field | Calendar Output |
| --- | --- | --- |
| Trello card | Card title | Event title |
| Trello card | Due date | Event start time |
| Trello card | Description | Event description |
| Trello card | Card URL | Event description link |
| Trello label | Meeting / delivery | Calendar category note |

## Safe Questions Before Building

1. Should the Zap run when a card is created, moved to a list, or assigned a
   label?
2. Should calendar events update when the Trello card changes?
3. Which Trello field is the source of truth for date and time?
4. Should failed cards be skipped, logged, or emailed for review?
5. Should Xero files be handled in the same Zap or a second workflow?

## Deliverable

A good first milestone is one working automation with handoff notes. Larger
items such as Xero file routing, Drive folder automation, or multiple boards
should be separate later milestones.
