import tkinter as tk
from tkinter import ttk, messagebox

class Vendedor:
    def __init__(self, nombre: str, apellidos: str, edad: int):
        self.verificarEdad(edad)
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def imprimir(self) -> str:
        return (f"Nombre del vendedor: {self.nombre}\n"
                f"Apellidos del vendedor: {self.apellidos}\n"
                f"Edad del vendedor: {self.edad}\n")

    def verificarEdad(self, edad: int):
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120")
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años")

class VentanaVendedor:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Registro de Vendedor")
        self.ventana.geometry("500x400")
        self.ventana.resizable(False, False)

        self.crear_interfaz()

    def crear_interfaz(self):
        frame = ttk.Frame(self.ventana, padding="20")
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Registro de Vendedor", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        ttk.Label(frame, text="Nombre:").grid(row=1, column=0, sticky="e", pady=5)
        self.entry_nombre = ttk.Entry(frame, width=30)
        self.entry_nombre.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Apellidos:").grid(row=2, column=0, sticky="e", pady=5)
        self.entry_apellidos = ttk.Entry(frame, width=30)
        self.entry_apellidos.grid(row=2, column=1, pady=5)

        ttk.Label(frame, text="Edad:").grid(row=3, column=0, sticky="e", pady=5)
        self.entry_edad = ttk.Entry(frame, width=30)
        self.entry_edad.grid(row=3, column=1, pady=5)

        ttk.Button(frame, text="Registrar", command=self.registrar_vendedor).grid(row=4, column=0, columnspan=2, pady=15)

        ttk.Label(frame, text="Resultado:", font=("Arial", 10, "bold")).grid(row=5, column=0, columnspan=2, pady=(10, 5))

        self.resultados = tk.Text(frame, height=6, width=50)
        self.resultados.grid(row=6, column=0, columnspan=2)

        ttk.Button(frame, text="Limpiar", command=self.limpiar).grid(row=7, column=0, columnspan=2, pady=10)

    def registrar_vendedor(self):
        nombre = self.entry_nombre.get().strip()
        apellidos = self.entry_apellidos.get().strip()
        edad_texto = self.entry_edad.get().strip()

        try:
            edad = int(edad_texto)
            vendedor = Vendedor(nombre, apellidos, edad)
            self.resultados.insert(tk.END, vendedor.imprimir() + "\n")
            self.resultados.see(tk.END)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def limpiar(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellidos.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.resultados.delete(1.0, tk.END)

    def ejecutar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = VentanaVendedor()
    app.ejecutar()