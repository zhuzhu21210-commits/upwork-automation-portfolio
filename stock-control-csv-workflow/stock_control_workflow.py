import csv
from decimal import Decimal
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
INVENTORY_FILE = BASE_DIR / "sample_inventory.csv"
TRANSACTIONS_FILE = BASE_DIR / "sample_transactions.csv"
OUTPUT_FILE = BASE_DIR / "stock_report.csv"


def read_inventory(path):
    products = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            sku = row["sku"]
            products[sku] = {
                "sku": sku,
                "product_name": row["product_name"],
                "category": row["category"],
                "stock_on_hand": int(row["stock_on_hand"]),
                "reorder_level": int(row["reorder_level"]),
                "unit_cost": Decimal(row["unit_cost"]),
            }
    return products


def apply_transactions(products, path):
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            sku = row["sku"]
            if sku not in products:
                continue

            quantity = int(row["quantity"])
            transaction_type = row["transaction_type"].strip().lower()

            if transaction_type == "sale":
                products[sku]["stock_on_hand"] -= quantity
            elif transaction_type == "restock":
                products[sku]["stock_on_hand"] += quantity
            else:
                raise ValueError(f"Unknown transaction type: {transaction_type}")


def build_report_rows(products):
    rows = []
    for product in products.values():
        stock = product["stock_on_hand"]
        reorder_level = product["reorder_level"]
        stock_value = product["unit_cost"] * stock

        if stock <= reorder_level:
            status = "Low stock"
            recommended_action = "Reorder"
        else:
            status = "OK"
            recommended_action = "Monitor"

        rows.append(
            {
                "sku": product["sku"],
                "product_name": product["product_name"],
                "category": product["category"],
                "stock_on_hand": stock,
                "reorder_level": reorder_level,
                "unit_cost": f"{product['unit_cost']:.2f}",
                "stock_value": f"{stock_value:.2f}",
                "status": status,
                "recommended_action": recommended_action,
            }
        )

    return sorted(rows, key=lambda row: row["sku"])


def write_report(rows, path):
    fieldnames = [
        "sku",
        "product_name",
        "category",
        "stock_on_hand",
        "reorder_level",
        "unit_cost",
        "stock_value",
        "status",
        "recommended_action",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    products = read_inventory(INVENTORY_FILE)
    apply_transactions(products, TRANSACTIONS_FILE)
    rows = build_report_rows(products)
    write_report(rows, OUTPUT_FILE)

    low_stock_skus = [row["sku"] for row in rows if row["status"] == "Low stock"]
    print(f"Wrote {len(rows)} rows to {OUTPUT_FILE.name}")
    print(f"Low-stock SKUs: {', '.join(low_stock_skus) or 'None'}")


if __name__ == "__main__":
    main()
