"""Portfolio sample: turn spreadsheet rows into reviewable Gmail draft text.

This script intentionally writes draft previews to CSV instead of sending email.
It demonstrates the safe first step for an Excel-to-Gmail automation workflow.
"""

import csv


def build_draft(row):
    employee = row["employee"]
    sales = float(row["sales"])
    target = float(row["target"])
    tickets_closed = int(row["tickets_closed"])
    attainment = sales / target if target else 0

    if attainment >= 1:
        status = "above_target"
        subject = f"Great work this week, {employee}"
        body = (
            f"Hi {employee},\n\n"
            f"You reached {attainment:.0%} of your sales target and closed "
            f"{tickets_closed} tickets. Great work. Please review the numbers "
            "and let me know if anything needs correction.\n\n"
            "Best,\nHerry"
        )
    else:
        status = "needs_follow_up"
        subject = f"Weekly performance check-in for {employee}"
        body = (
            f"Hi {employee},\n\n"
            f"You are currently at {attainment:.0%} of your sales target with "
            f"{tickets_closed} tickets closed. Please review the numbers and "
            "share any blockers or updates before the final report.\n\n"
            "Best,\nHerry"
        )

    return {
        "email": row["email"],
        "subject": subject,
        "body": body,
        "status": status,
    }


def main():
    with open("sample_metrics.csv", newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source))

    drafts = [build_draft(row) for row in rows]

    with open("gmail_drafts_preview.csv", "w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=["email", "subject", "body", "status"])
        writer.writeheader()
        writer.writerows(drafts)

    print(f"Wrote {len(drafts)} draft previews to gmail_drafts_preview.csv")


if __name__ == "__main__":
    main()
