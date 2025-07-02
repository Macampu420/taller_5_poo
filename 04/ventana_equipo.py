import tkinter as tk
from tkinter import ttk, messagebox
from equipo_maraton import EquipoMaratonProgramacion, Programador

class VentanaEquipo:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Equipo de Maratón de Programación")
        self.root.geometry("600x550")
        self.root.resizable(False, False)
        self.equipo = None
        self.crear_interfaz()

    def crear_interfaz(self):
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Datos del equipo", font=("Arial", 14, "bold")).grid(column=0, row=0, columnspan=2, pady=(0, 10))

        ttk.Label(frame, text="Nombre del equipo:").grid(column=0, row=1, sticky="e", pady=5)
        self.entry_equipo = ttk.Entry(frame, width=40)
        self.entry_equipo.grid(column=1, row=1)

        ttk.Label(frame, text="Universidad:").grid(column=0, row=2, sticky="e", pady=5)
        self.entry_universidad = ttk.Entry(frame, width=40)
        self.entry_universidad.grid(column=1, row=2)

        ttk.Label(frame, text="Lenguaje de programación:").grid(column=0, row=3, sticky="e", pady=5)
        self.entry_lenguaje = ttk.Entry(frame, width=40)
        self.entry_lenguaje.grid(column=1, row=3)

        ttk.Label(frame, text="Número de integrantes (2 o 3):").grid(column=0, row=4, sticky="e", pady=5)
        self.entry_capacidad = ttk.Entry(frame, width=40)
        self.entry_capacidad.grid(column=1, row=4)

        ttk.Button(frame, text="Crear equipo", command=self.crear_equipo).grid(column=0, row=5, columnspan=2, pady=15)

        ttk.Separator(frame).grid(column=0, row=6, columnspan=2, sticky="ew", pady=10)

        ttk.Label(frame, text="Agregar integrante", font=("Arial", 12, "bold")).grid(column=0, row=7, columnspan=2, pady=(0, 10))

        ttk.Label(frame, text="Nombre:").grid(column=0, row=8, sticky="e", pady=5)
        self.entry_nombre = ttk.Entry(frame, width=40)
        self.entry_nombre.grid(column=1, row=8)

        ttk.Label(frame, text="Apellidos:").grid(column=0, row=9, sticky="e", pady=5)
        self.entry_apellidos = ttk.Entry(frame, width=40)
        self.entry_apellidos.grid(column=1, row=9)

        ttk.Button(frame, text="Añadir integrante", command=self.agregar_integrante).grid(column=0, row=10, columnspan=2, pady=10)

        ttk.Label(frame, text="Resumen del equipo:", font=("Arial", 10, "bold")).grid(column=0, row=11, columnspan=2, pady=(10, 5))

        self.resultado = tk.Text(frame, height=10, width=70)
        self.resultado.grid(column=0, row=12, columnspan=2)

        ttk.Button(frame, text="Limpiar todo", command=self.limpiar).grid(column=0, row=13, columnspan=2, pady=10)

    def crear_equipo(self):
        try:
            nombre = self.entry_equipo.get().strip()
            universidad = self.entry_universidad.get().strip()
            lenguaje = self.entry_lenguaje.get().strip()
            capacidad = int(self.entry_capacidad.get().strip())
            self.equipo = EquipoMaratonProgramacion(nombre, universidad, lenguaje, capacidad)
            self.mostrar_mensaje("Equipo creado con éxito.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def agregar_integrante(self):
        if self.equipo is None:
            messagebox.showwarning("Advertencia", "Primero debes crear el equipo.")
            return

        try:
            nombre = self.entry_nombre.get().strip()
            apellidos = self.entry_apellidos.get().strip()
            programador = Programador(nombre, apellidos)
            self.equipo.añadir(programador)
            self.mostrar_mensaje("Integrante añadido.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mostrar_mensaje(self, mensaje):
        self.resultado.delete(1.0, tk.END)
        if self.equipo:
            self.resultado.insert(tk.END, self.equipo.mostrar_equipo())

    def limpiar(self):
        self.entry_equipo.delete(0, tk.END)
        self.entry_universidad.delete(0, tk.END)
        self.entry_lenguaje.delete(0, tk.END)
        self.entry_capacidad.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellidos.delete(0, tk.END)
        self.resultado.delete(1.0, tk.END)
        self.equipo = None