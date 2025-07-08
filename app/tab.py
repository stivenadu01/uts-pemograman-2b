from tkinter import ttk
from . import dashboard

def create_tab(notebook, tab_name):
  tab = ttk.Frame(notebook)
  notebook.add(tab, text=tab_name)
  return tab

# refresh tab
def hapus_widget(tab):
  for widget in tab.winfo_children():
    widget.destroy()
  return

def refresh_tab(event, tab_dashboard):
  selected_tab = event.widget.select()
  tab_text = event.widget.tab(selected_tab, "text")
  
  if tab_text == "Dashboard":
    hapus_widget(tab_dashboard)
    dashboard.dashboard_gui(tab_dashboard)
  return