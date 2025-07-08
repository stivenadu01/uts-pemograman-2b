import tkinter as tk
from tkinter import ttk, messagebox
from .db import get_conn, clear_from

def penduduk_gui(main):
    for widget in main.winfo_children():
        widget.destroy()
    
    # Frame judul dan tombol
    judul_frame = tk.Frame(main)
    judul_frame.pack(fill='both', ipadx=10, ipady=10)

    # Judul
    judul = tk.Label(judul_frame, text="Penduduk", font=('Helvetica', 24, 'bold'))
    judul.pack(pady=20, fill='both')

    # Tabel penduduk
    columns = ('ID', 'Nama Penduduk')
    tree = ttk.Treeview(main, columns=columns, show='headings', height=15)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.CENTER)
    tree.pack(pady=10, fill='x', expand=True, padx=10)
    
    # Tombol tindakan
    tk.Button(judul_frame, text="Tambah Penduduk", bg='blue', fg="white", command=lambda: open_add_penduduk_modal(tree)).pack(side=tk.LEFT, padx=10)
    tk.Button(judul_frame, text="Edit Penduduk", bg='yellow', fg="black", command=lambda: open_edit_penduduk_modal(tree)).pack(side=tk.LEFT, padx=10)
    tk.Button(judul_frame, text="Hapus Penduduk", bg='red', fg="white", command=lambda: delete_penduduk(tree)).pack(side=tk.LEFT, padx=10)  
     

    # Muat data awal
    fetch_penduduk(tree)


def open_add_penduduk_modal(tree):
    modal = tk.Toplevel()
    modal.title("Tambah Penduduk")
    modal.geometry("400x200")
    modal.grab_set()
    modal.configure(bg='white')

    modal_frame = tk.Frame(modal, bg='white')
    modal_frame.pack(pady=20)

    nama_var = tk.StringVar()
    tk.Label(modal_frame, text="Nama Penduduk", bg='white').grid(row=0, column=0, padx=10, pady=10)
    tk.Entry(modal_frame, textvariable=nama_var, width=30).grid(row=0, column=1, padx=10, pady=10)
    # id_var = tk.StringVar()
    # tk.Label(modal_frame, text="Tambah ID", bg='white').grid(row=1, column=1, padx=10, pady=10)
    # tk.Entry(modal_frame, textvariable=id_var, width=30).grid(row=1, column=1, padx=10, pady=10)
    tk.Button(modal_frame, text="Tambah", bg='blue', fg="white", command=lambda: add_penduduk(nama_var, tree, modal)).grid(row=2, column=0, pady=20, columnspan=3)


def open_edit_penduduk_modal(tree):
    select = tree.selection()
    if not select or len(select) > 1:
        messagebox.showwarning("Edit Penduduk", "Pilih satu penduduk untuk diedit!")
        return

    modal = tk.Toplevel()
    modal.title("Edit Penduduk")
    modal.geometry("400x200")
    modal.configure(bg='white')
    modal.grab_set()

    modal_frame = tk.Frame(modal, bg='white')
    modal_frame.pack(pady=20)

    nama_var = tk.StringVar()
    nama_var.set(tree.item(select)['values'][1])

    tk.Label(modal_frame, text="Nama Penduduk", bg='white').grid(row=0, column=0, padx=10, pady=10)
    tk.Entry(modal_frame, textvariable=nama_var, width=30).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(modal_frame, text="Edit", bg='yellow', fg="black", command=lambda: edit_penduduk(nama_var, tree, modal)).grid(row=1, column=0, columnspan=2, pady=20)


def fetch_penduduk(tree):
    for row in tree.get_children():
        tree.delete(row)
    try:
        db = get_conn()
        cursor = db.cursor()
        cursor.execute("SELECT id, nama FROM penduduk")
        rows = cursor.fetchall()
        for row in rows:
            tree.insert("", "end", values=row)
    except Exception as err:
        messagebox.showerror("Database Error", f"Terjadi kesalahan: {err}")
    finally:
        db.close()


def add_penduduk(nama_var, tree, modal):
    nama = nama_var.get().strip()
    if not nama:
        messagebox.showwarning("Input Error", "Nama wajib diisi!")
        return
    try:
        db = get_conn()
        cursor = db.cursor()
        cursor.execute("INSERT INTO penduduk (nama) VALUES (%s)", (nama,))
        db.commit()
        modal.destroy()
        fetch_penduduk(tree)
    except Exception as err:
        messagebox.showerror("Database Error", f"Terjadi kesalahan: {err}")
    finally:
        db.close()


def edit_penduduk(nama_var, tree, modal):
    select = tree.selection()
    id_penduduk = tree.item(select)['values'][0]
    nama_baru = nama_var.get().strip()
    if not nama_baru:
        messagebox.showwarning("Input Error", "Nama wajib diisi!")
        return
    try:
        db = get_conn()
        cursor = db.cursor()
        cursor.execute("UPDATE penduduk SET nama = %s WHERE id = %s", (nama_baru, id_penduduk))
        db.commit()
        modal.destroy()
        fetch_penduduk(tree)
    except Exception as err:
        messagebox.showerror("Database Error", f"Terjadi kesalahan: {err}")
    finally:
        db.close()


def delete_penduduk(tree):
    select_item = tree.selection()
    if not select_item:
        messagebox.showwarning("Hapus Penduduk", "Pilih penduduk yang ingin dihapus!")
        return
    if not messagebox.askokcancel("Hapus Penduduk", "Yakin ingin menghapus penduduk ini?"):
        return
    try:
        db = get_conn()
        cursor = db.cursor()
        for select in select_item:
            id_penduduk = tree.item(select)['values'][0]
            cursor.execute("DELETE FROM penduduk WHERE id = %s", (id_penduduk,))
        db.commit()
        fetch_penduduk(tree)
    except Exception as err:
        messagebox.showerror("Database Error", f"Terjadi kesalahan: {err}")
    finally:
        db.close()
