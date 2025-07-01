import tkinter as tk
from tkinter import scrolledtext
from prueba_excepciones import PruebaExcepciones

class VentanaExcepciones:
    def __init__(self, contenedor):
        self.contenedor = contenedor
        self.prueba = PruebaExcepciones()
        self.init()
    
    def init(self):
        self.contenedor.title("Prueba de Excepciones")
        self.contenedor.geometry("600x450")
        self.contenedor.resizable(True, True)
        
        titulo = tk.Label(self.contenedor, text="Demostración de Manejo de Excepciones", 
                         font=("Arial", 14, "bold"))
        titulo.pack(pady=10)
        
        frame_botones = tk.Frame(self.contenedor)
        frame_botones.pack(pady=10)
        
        btn_primer_try = tk.Button(frame_botones, text="Ejecutar Primer Try", 
                                  command=self.ejecutar_primer_try, width=20, height=2)
        btn_primer_try.pack(side=tk.LEFT, padx=5)
        
        btn_segundo_try = tk.Button(frame_botones, text="Ejecutar Segundo Try", 
                                   command=self.ejecutar_segundo_try, width=20, height=2)
        btn_segundo_try.pack(side=tk.LEFT, padx=5)
        
        btn_ambos = tk.Button(frame_botones, text="Ejecutar Ambos", 
                             command=self.ejecutar_ambos, width=20, height=2)
        btn_ambos.pack(side=tk.LEFT, padx=5)
        
        btn_limpiar = tk.Button(frame_botones, text="Limpiar", 
                               command=self.limpiar_salida, width=15, height=2)
        btn_limpiar.pack(side=tk.LEFT, padx=5)
        
        tk.Label(self.contenedor, text="Salida del programa:", font=("Arial", 12, "bold")).pack(anchor="w", padx=20, pady=(20,5))
        
        self.area_salida = scrolledtext.ScrolledText(self.contenedor, width=70, height=15, 
                                                    font=("Courier", 10))
        self.area_salida.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        descripcion = tk.Label(self.contenedor, 
                              text="Esta aplicación demuestra el manejo de excepciones en Python\n" +
                                   "Primer Try: División por cero (ZeroDivisionError)\n" +
                                   "Segundo Try: Operación en objeto None (AttributeError)",
                              font=("Arial", 9), justify=tk.LEFT, fg="gray")
        descripcion.pack(pady=5)
    
    def ejecutar_primer_try(self):
        self.limpiar_salida()
        mensajes = self.prueba.primer_bloque_try()
        self.mostrar_mensajes(mensajes, "=== PRIMER BLOQUE TRY ===")
    
    def ejecutar_segundo_try(self):
        self.limpiar_salida()
        mensajes = self.prueba.segundo_bloque_try()
        self.mostrar_mensajes(mensajes, "=== SEGUNDO BLOQUE TRY ===")
    
    def ejecutar_ambos(self):
        self.limpiar_salida()
        self.area_salida.insert(tk.END, "=== EJECUTANDO AMBOS BLOQUES TRY ===\n\n")
        
        self.area_salida.insert(tk.END, "--- Primer bloque try ---\n")
        mensajes1 = self.prueba.primer_bloque_try()
        for mensaje in mensajes1:
            self.area_salida.insert(tk.END, f"{mensaje}\n")
        
        self.area_salida.insert(tk.END, "\n--- Segundo bloque try ---\n")
        mensajes2 = self.prueba.segundo_bloque_try()
        for mensaje in mensajes2:
            self.area_salida.insert(tk.END, f"{mensaje}\n")
        
        self.area_salida.insert(tk.END, "\n=== EJECUCIÓN COMPLETADA ===\n")
        self.area_salida.see(tk.END)
    
    def mostrar_mensajes(self, mensajes, titulo):
        self.area_salida.insert(tk.END, f"{titulo}\n\n")
        for mensaje in mensajes:
            self.area_salida.insert(tk.END, f"{mensaje}\n")
        self.area_salida.insert(tk.END, "\n=== EJECUCIÓN COMPLETADA ===\n")
        self.area_salida.see(tk.END)
    
    def limpiar_salida(self):
        self.area_salida.delete(1.0, tk.END)