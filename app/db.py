import mysql.connector
from tkinter import messagebox

def get_conn():
  try:
    conn = mysql.connector.connect(
      host="Localhost",
      user="root",
      password="",
      database="penduduk"
    )
    return conn
  except mysql.connector.Error as err:
    messagebox.showerror("Database Error:", err)
    return None


# clear form input
def clear_from(*args):
  """Membersihkan Form Input"""
  for i in args:
    i.set("")