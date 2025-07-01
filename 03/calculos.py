import tkinter as tk
from tkinter import ttk, messagebox
import math

class CalculosNumericos:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Cálculos Numéricos")
        self.ventana.geometry("600x450")
        self.ventana.resizable(False, False)
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        frame_principal = ttk.Frame(self.ventana, padding="20")
        frame_principal.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(frame_principal, text="Calculadora de Logaritmo Neperiano y Raíz Cuadrada", 
                 font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        ttk.Label(frame_principal, text="Valor numérico:").grid(row=1, column=0, sticky=tk.W, pady=5)
        
        self.entry_valor = ttk.Entry(frame_principal, width=15)
        self.entry_valor.grid(row=1, column=1, padx=(10, 0), pady=5)
        
        frame_botones = ttk.Frame(frame_principal)
        frame_botones.grid(row=2, column=0, columnspan=3, pady=20)
        
        btn_logaritmo = ttk.Button(frame_botones, text="Calcular Logaritmo Neperiano", 
                                  command=self.calcular_logaritmo_neperiano)
        btn_logaritmo.grid(row=0, column=0, padx=5)
        
        btn_raiz = ttk.Button(frame_botones, text="Calcular Raíz Cuadrada", 
                             command=self.calcular_raiz_cuadrada)
        btn_raiz.grid(row=0, column=1, padx=5)
        
        ttk.Label(frame_principal, text="Resultados:", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky=tk.W, pady=(20, 5))
        
        self.text_resultados = tk.Text(frame_principal, height=8, width=45)
        self.text_resultados.grid(row=4, column=0, columnspan=3, pady=5)
        
        scrollbar = ttk.Scrollbar(frame_principal, orient="vertical", command=self.text_resultados.yview)
        scrollbar.grid(row=4, column=3, sticky=(tk.N, tk.S), pady=5)
        self.text_resultados.configure(yscrollcommand=scrollbar.set)
        
        btn_limpiar = ttk.Button(frame_principal, text="Limpiar", command=self.limpiar_resultados)
        btn_limpiar.grid(row=5, column=0, pady=10)
    
    def obtener_valor(self):
        try:
            valor = float(self.entry_valor.get())
            return valor
        except ValueError:
            raise ValueError("El valor debe ser numérico")
    
    def mostrar_resultado(self, mensaje):
        self.text_resultados.insert(tk.END, mensaje + "\n")
        self.text_resultados.see(tk.END)
    
    def calcular_logaritmo_neperiano(self):
        try:
            valor = self.obtener_valor()
            if valor <= 0:
                raise ArithmeticError("El valor debe ser un número positivo")
            
            resultado = math.log(valor)
            self.mostrar_resultado(f"Logaritmo neperiano de {valor} = {resultado}")
            
        except ArithmeticError as e:
            self.mostrar_resultado("El valor debe ser un número positivo para calcular el logaritmo")
        except ValueError:
            self.mostrar_resultado("El valor debe ser numérico para calcular el logaritmo")
    
    def calcular_raiz_cuadrada(self):
        try:
            valor = self.obtener_valor()
            if valor < 0:
                raise ArithmeticError("El valor debe ser un número positivo")
            
            resultado = math.sqrt(valor)
            self.mostrar_resultado(f"Raíz cuadrada de {valor} = {resultado}")
            
        except ArithmeticError as e:
            self.mostrar_resultado("El valor debe ser un número positivo para calcular la raíz cuadrada")
        except ValueError:
            self.mostrar_resultado("El valor debe ser numérico para calcular la raíz cuadrada")
    
    def limpiar_resultados(self):
        self.text_resultados.delete(1.0, tk.END)
        self.entry_valor.delete(0, tk.END)
    
    def ejecutar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = CalculosNumericos()
    app.ejecutar()