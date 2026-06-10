# Desired Inventory Report

The first prototype should produce a simple report with these fields:

- SKU
- Item name
- Category
- Supplier
- Location
- Current quantity
- Unit
- Unit cost
- Stock value
- Reorder level
- Status: OK, Low Stock, or Negative Stock
- Suggested action

## Example Rules

- If quantity is below `0`, mark as `Negative Stock`.
- If quantity is greater than or equal to `0` but less than or equal to reorder level, mark as `Low Stock`.
- Otherwise mark as `OK`.
- Stock value equals `quantity_on_hand * unit_cost`.

## First Milestone Output

For a `$250-$300` first milestone, the output can be:

- cleaned CSV/Excel-ready report
- repeatable Python script or spreadsheet workflow
- short setup notes
- one adjustment after review
