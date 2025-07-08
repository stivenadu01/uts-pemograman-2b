# 🧑‍💻 UTS Pemrograman 2B – Aplikasi Manajemen Data Penduduk

Aplikasi desktop berbasis Python + Tkinter ini dibuat sebagai tugas **UTS Mata Kuliah Pemrograman**. Aplikasi ini memungkinkan pengguna mengelola data penduduk seperti menambahkan, mengedit, dan menghapus data secara langsung dari GUI yang terhubung ke database MySQL.

---

## 📌 Fitur Utama

✅ **Dashboard**

- Menampilkan total data penduduk secara real-time

✅ **Manajemen Data Penduduk**

- Tambah data penduduk
- Edit nama penduduk
- Hapus data penduduk
- Tampilan tabel data dengan TreeView Tkinter

✅ **Tab Navigasi Otomatis**

- Menggunakan `Notebook` (tab view) dari `ttk`
- Fitur refresh otomatis saat berpindah tab

✅ **Struktur Modular**

- `main.py` = Entry point
- `dashboard.py` = Tampilan dashboard
- `penduduk.py` = Fungsi CRUD data
- `tab.py` = Manajemen tab dan refresh
- `db.py` = Koneksi MySQL dan utilitas

---

## 💻 Teknologi yang Digunakan

| Komponen   | Teknologi                   |
| ---------- | --------------------------- |
| Bahasa     | Python 3                    |
| GUI        | Tkinter (`ttk`, `Treeview`) |
| Database   | MySQL                       |
| Koneksi    | mysql-connector-python      |
| Arsitektur | Modular (per file/fungsi)   |

---
