import tkinter as tk
from ventana_excepciones import VentanaExcepciones

def main():
    root = tk.Tk()
    app = VentanaExcepciones(root)
    root.mainloop()

if __name__ == "__main__":
    main()