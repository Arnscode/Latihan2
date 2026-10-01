import json
import csv
from typing import List, Dict, Any

# 1. READ: Membaca langsung dari file JSON
input_file_json: str = "data/raw_products.json"
with open(input_file_json, mode="r", encoding="utf-8") as file:
    payload: Dict[str, Any] = json.load(file)
raw_items: List[Dict[str, Any]] = payload.get("products")
items: List[Dict[str, Any]] = raw_items if isinstance(raw_items, list) else []

# 2. TRANSFORM: Transformasi menggunakan filter dan lambda
# [Langkah 1] Filter Data
filtered_items: List[Dict[str, Any]] = filter(lambda item: item["is_available"] is True, items)

# [Langkah 2] Mapping Data
maping_data: map = map(
    lambda item: {
        "item_code": item["item_code"],
        "product_name": item["name"].upper(),
        "price": float(item["price"]),
        "stock_category": "High Stock" if item["stock"] >= 20 else "Low Stock"
    },
    filtered_items
)
# [Langkah 3] Convert map object to list
active_products: List[Dict[str, Any]] = list(maping_data)

# 3. WRITE: Menyimpan ke file CSV
output_path: str = "data/products_fp.csv"
headers: List[str] = list(active_products[0].keys())

with open(output_path, mode="w", encoding="utf-8", newline="") as file:
    writer: csv.DictWriter = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(active_products)

print(f"[SUCCESS] Data berhasil disimpan di: {output_path}")