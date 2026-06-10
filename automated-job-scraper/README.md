# Automated Job Scraper Sample

This sample demonstrates a small, reviewable job-listing scraper workflow.

It parses public job-listing style HTML, extracts structured fields, applies
simple filters, and exports a clean CSV file for review in Excel or Google
Sheets.

## What It Shows

- Parse repeated listing cards from HTML
- Extract title, company, location, pay, tags, and detail URL
- Filter by keyword and minimum pay
- Export a clean CSV output
- Keep the script small enough for fixed-scope client work

## Files

- `job_board_sample.html` - sample public-style job board HTML
- `job_scraper.py` - Python script using only the standard library
- `sample_job_output.csv` - generated CSV output

## Run

```bash
python job_scraper.py
```

Expected output:

```text
Wrote 4 jobs to sample_job_output.csv
```

## Client Fit

This pattern fits projects such as:

- scrape public job listings into CSV
- monitor public listing pages for matching roles
- export filtered records for review
- build a first milestone before adding scheduling or alerts

## Safety Notes

This sample is for public, permission-friendly pages. It does not bypass
CAPTCHAs, login walls, rate limits, or terms of service restrictions.
