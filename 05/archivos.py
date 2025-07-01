import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os

class LeerArchivo:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Lector de Archivos")
        self.ventana.geometry("600x500")
        self.ventana.resizable(True, True)
        
        self.nombre_archivo = ""
        self.crear_interfaz()
    
    def crear_interfaz(self):
        frame_principal = ttk.Frame(self.ventana, padding="10")
        frame_principal.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        frame_principal.columnconfigure(1, weight=1)
        frame_principal.rowconfigure(2, weight=1)
        
        ttk.Label(frame_principal, text="Lector de Archivos de Texto", 
                 font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        ttk.Label(frame_principal, text="Archivo:").grid(row=1, column=0, sticky=tk.W, pady=5)
        
        self.entry_archivo = ttk.Entry(frame_principal, width=50)
        self.entry_archivo.grid(row=1, column=1, padx=(10, 5), pady=5, sticky=(tk.W, tk.E))
        self.entry_archivo.insert(0, "C:/prueba.txt")
        
        btn_examinar = ttk.Button(frame_principal, text="Examinar", command=self.examinar_archivo)
        btn_examinar.grid(row=1, column=2, padx=(5, 0), pady=5)
        
        frame_botones = ttk.Frame(frame_principal)
        frame_botones.grid(row=1, column=3, padx=(20, 0), pady=5)
        
        btn_leer = ttk.Button(frame_botones, text="Leer Archivo", command=self.leer_archivo)
        btn_leer.grid(row=0, column=0, padx=5)
        
        btn_limpiar = ttk.Button(frame_botones, text="Limpiar", command=self.limpiar_contenido)
        btn_limpiar.grid(row=0, column=1, padx=5)
        
        ttk.Label(frame_principal, text="Contenido del archivo:", 
                 font=("Arial", 10, "bold")).grid(row=2, column=0, sticky=(tk.W, tk.N), pady=(20, 5))
        
        frame_texto = ttk.Frame(frame_principal)
        frame_texto.grid(row=3, column=0, columnspan=4, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        frame_texto.columnconfigure(0, weight=1)
        frame_texto.rowconfigure(0, weight=1)
        
        self.text_contenido = tk.Text(frame_texto, wrap=tk.WORD, font=("Consolas", 10))
        self.text_contenido.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        scrollbar_v = ttk.Scrollbar(frame_texto, orient="vertical", command=self.text_contenido.yview)
        scrollbar_v.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.text_contenido.configure(yscrollcommand=scrollbar_v.set)
        
        scrollbar_h = ttk.Scrollbar(frame_texto, orient="horizontal", command=self.text_contenido.xview)
        scrollbar_h.grid(row=1, column=0, sticky=(tk.W, tk.E))
        self.text_contenido.configure(xscrollcommand=scrollbar_h.set)
        
        frame_info = ttk.Frame(frame_principal)
        frame_info.grid(row=4, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=(10, 0))
        
        self.label_info = ttk.Label(frame_info, text="Seleccione un archivo para leer", 
                                   font=("Arial", 9), foreground="gray")
        self.label_info.grid(row=0, column=0, sticky=tk.W)
    
    def examinar_archivo(self):
        archivo = filedialog.askopenfilename(
            title="Seleccionar archivo de texto",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if archivo:
            self.entry_archivo.delete(0, tk.END)
            self.entry_archivo.insert(0, archivo)
    
    def leer_archivo(self):
        self.nombre_archivo = self.entry_archivo.get()
        
        if not self.nombre_archivo:
            messagebox.showwarning("Advertencia", "Por favor ingrese la ruta del archivo")
            return
        
        try:
            with open(self.nombre_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                
            self.text_contenido.delete(1.0, tk.END)
            self.text_contenido.insert(1.0, contenido)
            
            num_lineas = contenido.count('\n') + 1 if contenido else 0
            tamano_archivo = os.path.getsize(self.nombre_archivo)
            
            self.label_info.config(
                text=f"Archivo leído: {os.path.basename(self.nombre_archivo)} | "
                     f"Líneas: {num_lineas} | Tamaño: {tamano_archivo} bytes",
                foreground="green"
            )
            
        except UnicodeDecodeError:
            try:
                with open(self.nombre_archivo, 'r', encoding='latin1') as archivo:
                    contenido = archivo.read()
                
                self.text_contenido.delete(1.0, tk.END)
                self.text_contenido.insert(1.0, contenido)
                
                self.label_info.config(
                    text=f"Archivo leído con codificación latin1: {os.path.basename(self.nombre_archivo)}",
                    foreground="orange"
                )
                
            except Exception as e:
                self.mostrar_error_lectura()
                
        except FileNotFoundError:
            self.mostrar_error_lectura()
            self.label_info.config(text="Error: Archivo no encontrado", foreground="red")
            
        except PermissionError:
            self.mostrar_error_lectura()
            self.label_info.config(text="Error: Sin permisos para leer el archivo", foreground="red")
            
        except Exception as e:
            self.mostrar_error_lectura()
    
    def mostrar_error_lectura(self):
        self.text_contenido.delete(1.0, tk.END)
        self.text_contenido.insert(1.0, "No se pudo leer el archivo.")
        messagebox.showerror("Error", "No se pudo leer el archivo.")
    
    def limpiar_contenido(self):
        self.text_contenido.delete(1.0, tk.END)
        self.entry_archivo.delete(0, tk.END)
        self.entry_archivo.insert(0, "C:/prueba.txt")
        self.label_info.config(text="Seleccione un archivo para leer", foreground="gray")
    
    def ejecutar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = LeerArchivo()
    app.ejecutar()