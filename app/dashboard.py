import tkinter as tk
from tkinter import messagebox
from .db import get_conn

BG1 = "#f0f0f0"
BG2 = "#e0e0e0"
BG3 = "#ddd"
FG = "#333"
BGWARNING = "#f2fc81"

def dashboard_gui(root):
  main = tk.Frame(root, bg=BG1)
  main.pack(expand=True, fill='both')
  
  try:
    db = get_conn()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM penduduk")
    data_penduduk = cursor.fetchall()
    db.close()
  except Exception as err:
    messagebox.showerror("Database Error", f"Terjadi kesalahan: {err}")
    return

  total_penduduk = len(data_penduduk)

  judul_frame = tk.Frame(main, bg=BG2, padx=20, pady=20)
  judul_frame.pack(fill='x', padx=20, pady=20)
  
  judul_label = tk.Label(judul_frame, text="Selamat datang di aplikasi data penduduk!", font=("Arial", 24), anchor='w', bg=BG2)
  judul_label.pack(fill='x')
  
  status_label = tk.Label(judul_frame, text="Status", font=("Arial", 12), bg=BG2, anchor='w')
  status_label.pack(fill='x')




  # card frame
  card_frame = tk.Frame(main, bg=BG1)
  card_frame.pack(fill='both', side='top')

  # card penduduk frame
  card_penduduk = tk.Frame(card_frame, padx=20, pady=20, bg=BG2)
  card_penduduk.pack(side='left', fill='y', padx=20, pady=20)
  
  # card penduduk label
  total_penduduk_label = tk.Label(card_penduduk, bg=BG2, text=f"Total penduduk {total_penduduk}", font=("Arial", 16))
  total_penduduk_label.pack()
  return  
