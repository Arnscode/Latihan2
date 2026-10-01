# Latihan Pertemuan 3 — Transformasi Data Produk dengan Python

Tugas ini membaca data produk dari file JSON, memfilter produk yang tersedia (`is_available == True`), lalu memformat ulang datanya dan menyimpannya ke file CSV. Transformasi data yang sama dikerjakan dengan **3 pendekatan berbeda** untuk membandingkan gaya penulisan kode di Python: **Standard For Loop**, **List & Dict Comprehension**, dan **Functional Programming (filter + map + lambda)**.

## Struktur Folder

```
.
├── data/
│   └── raw_products.json      # data mentah (input)
├── products_loop.py            # metode 1: standard for loop
├── products_lc.py              # metode 2: list & dict comprehension
├── products_fp.py              # metode 3: functional programming / lambda
└── README.md
```

Setelah dijalankan, masing-masing skrip akan menghasilkan file CSV baru di dalam folder `data/`:
- `data/products_loop.csv`
- `data/products_lc.csv`
- `data/products_fp.csv`

## Aturan Transformasi Data

1. Hanya ambil produk dengan `is_available == True`.
2. Format ulang setiap produk menjadi dictionary dengan key:
   | Key | Keterangan |
   |---|---|
   | `item_code` | Kode produk (teks) |
   | `product_name` | Nama produk dalam **HURUF KAPITAL** |
   | `price` | Harga produk (float) |
   | `stock_category` | `"High Stock"` jika `stock >= 20`, selain itu `"Low Stock"` |

## Cara Menjalankan

Pastikan file `data/raw_products.json` sudah ada, lalu jalankan salah satu (atau semua) skrip dari root folder project:

```bash/Terminal
python products_loop.py
python products_lc.py
python products_fp.py
```

Setiap skrip akan mencetak pesan konfirmasi, contoh:
```
[SUCCESS] Data berhasil disimpan di: data/products_loop.csv
```

## Catatan

Ketiga pendekatan di atas **menghasilkan output CSV yang identik** karena menjalankan aturan transformasi yang sama persis. Perbedaannya pada gaya penulisan kode, bukan pada hasil akhirnya — ini untuk menunjukkan bahwa satu masalah yang sama bisa diselesaikan dengan beberapa cara berbeda di Python.
