# Stock Control CSV Workflow

This sample shows a small Python workflow for inventory and stock-control
projects. It reads a product inventory CSV, applies sales and restock
transactions, then exports an updated stock report with reorder flags.

It uses only Python's standard library so a client can run it without
dependency setup.

## What It Demonstrates

- reading product inventory from CSV
- applying stock-in and stock-out transactions
- calculating stock value
- flagging low-stock items
- exporting a clean CSV report for review
- keeping the first milestone small before building a larger system

## Run

```bash
python stock_control_workflow.py
```

Expected output:

```text
Wrote 5 rows to stock_report.csv
Low-stock SKUs: SKU-1002, SKU-1004
```

## Input Files

- `sample_inventory.csv`
- `sample_transactions.csv`

## Output Fields

- `sku`
- `product_name`
- `category`
- `stock_on_hand`
- `reorder_level`
- `unit_cost`
- `stock_value`
- `status`
- `recommended_action`

## Client Use Cases

- stock control spreadsheet cleanup
- CSV import/export workflow
- inventory reorder report
- first milestone before a full stock-control app
- Shopify, warehouse, or spreadsheet-based inventory review

## Notes

This sample is intentionally small. For a paid project, the first milestone can
confirm product fields, import format, stock update rules, and report output
before adding user accounts, dashboards, barcode scanning, or API integrations.
