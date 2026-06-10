# Excel to Gmail Draft Automation

This sample shows a safe automation pattern for turning spreadsheet rows into
reviewable Gmail draft records.

It does not send emails. The script reads a CSV file, applies simple business
rules, and writes `gmail_drafts_preview.csv` so the results can be reviewed
before any Gmail API integration is added.

## What It Demonstrates

- reading spreadsheet-style CSV input
- calculating basic performance metrics
- selecting the right email template
- generating personalized draft subject/body text
- keeping human review before sending

## Run

```bash
python excel_to_gmail_drafts.py
```

Expected output:

```text
Wrote 4 draft previews to gmail_drafts_preview.csv
```

## Input Fields

- `employee`
- `email`
- `sales`
- `target`
- `tickets_closed`

## Output Fields

- `email`
- `subject`
- `body`
- `status`

## Client Use Cases

- Excel reports to Gmail drafts
- performance summary messages
- customer or employee update drafts
- spreadsheet-driven notification workflows

## Notes

For paid work, a production version can be connected to Gmail API drafts after
the spreadsheet rules, templates, and approval workflow are confirmed.
