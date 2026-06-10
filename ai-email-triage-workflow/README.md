# AI Email Triage Workflow

This sample describes a safe AI-assisted workflow for organizing inbound email.
It is designed around review and approval, not automatic sending.

## Client Problem

A founder or small team receives many inbound messages and wants a simple way
to identify:

- urgent requests
- sales opportunities
- invoices or payment issues
- emails that need a reply
- low-priority newsletters

## Proposed Workflow

1. Pull recent inbox messages from Gmail or an exported CSV.
2. Extract sender, subject, timestamp, and snippet.
3. Classify each message into a clear bucket.
4. Produce a daily summary with suggested next actions.
5. Draft replies for messages that need a response.
6. Require human approval before any reply is sent.

## Example Output

| Bucket | Sender | Why It Matters | Suggested Action |
| --- | --- | --- | --- |
| Urgent | Stripe | Failed payment notice | Update billing today |
| Sales | Potential client | Asked about automation help | Reply with discovery questions |
| Waiting | Upwork | Profile approval needed | Complete profile before proposing |
| FYI | Newsletter | No action required | Archive or ignore |

## Deliverables

- working script or automation recipe
- readable daily summary
- setup instructions
- customization options for buckets and tone

## Fixed-Price Scope

Starter version: USD $150-$300 depending on integrations and output format.

