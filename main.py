import tkinter as tk
from tkinter import ttk
from app import dashboard, penduduk, tab

def main():
    # root
    root = tk.Tk()
    root.title("Aplikasi Mengelola Data Penduduk")
    root.geometry("900x600")

    # tab menu
    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both")
    tab_dashboard = tab.create_tab(notebook, "Dashboard")
    tab_penduduk = tab.create_tab(notebook, "Penduduk")

    # isi dari tab
    try:
        dashboard.dashboard_gui(tab_dashboard)
        penduduk.penduduk_gui(tab_penduduk)
    except Exception as e:
        print(f"Error: {e}")

    notebook.bind("<<NotebookTabChanged>>", lambda event: tab.refresh_tab(event, tab_dashboard))

    root.mainloop()


if __name__ == '__main__':
    main()
