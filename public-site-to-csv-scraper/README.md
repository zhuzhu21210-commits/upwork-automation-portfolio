# Public Website Data to CSV Scraper

This sample collects quote records from a public demo website and exports them
to a clean CSV file.

It intentionally uses only Python's standard library so a client can run it
without dependency setup.

## What It Demonstrates

- fetching public webpages
- parsing repeated HTML records
- extracting clean fields
- writing structured CSV output
- keeping the script small and easy to adapt

## Run

```bash
python public_site_to_csv_scraper.py
```

Expected output:

```text
Wrote 30 rows to quotes_sample.csv
```

## Output Fields

- `quote`
- `author`

## Example Output

The repository includes `quotes_sample.csv` as a small example output.

## Client Use Cases

- public directory listings to CSV
- product or article metadata collection
- simple lead list formatting from public pages
- spreadsheet-ready research tasks

## Notes

This sample avoids login-protected sites, CAPTCHA bypass, private data, and
terms-of-service circumvention.
