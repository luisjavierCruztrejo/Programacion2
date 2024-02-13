from tkinter import ttk
import tkinter as tk
from tkinter import messagebox, ttk
main_window = tk.Tk()
main_window.config(width=300, height=200)
main_window.title("Combobox")
combo = ttk.Combobox()
combo.place(x=50, y=50)


combo = ttk.Combobox(state="readonly")
combo = ttk.Combobox(
    state="readonly",
    values=["Python", "C", "C++", "Java"]
)

def show_selection():
    # Obtener la opción seleccionada.
    selection = combo.get()
    messagebox.showinfo(
        message=f"La opción seleccionada es: {selection}",
        title="Selección"
    )
main_window = tk.Tk()
main_window.config(width=300, height=200)
main_window.title("Combobox")
combo = ttk.Combobox(
    state="readonly",
    values=["Python", "C", "C++", "Java"]
)
combo.place(x=50, y=50)
button = ttk.Button(text="Mostrar selección", command=show_selection)
button.place(x=50, y=100)
main_window.mainloop()
index = combo.current()
combo.set("Python")
# Selecciona "C++".
combo.current(2)
# Retorna ('Python', 'C', 'C++', 'Java')
values = combo["values"]
values = list(combo["values"])
combo["values"] = values + ["Nuevo elemento"]
# Vaciar la lista.
combo["values"] = []

def selection_changed(event):
    selection = combo.get()
    messagebox.showinfo(
        title="Nuevo elemento seleccionado",
        message=selection
    )
main_window = tk.Tk()
main_window.config(width=300, height=200)
main_window.title("Combobox")
combo = ttk.Combobox(values=["Python", "C", "C++", "Java"])
combo.bind("<<ComboboxSelected>>", selection_changed)
combo.place(x=50, y=50)
#main_window.mainloop()