import tkinter as tk
from ventana_equipo import VentanaEquipo

def main():
    root = tk.Tk()
    app = VentanaEquipo(root)
    root.mainloop()

if __name__ == "__main__":
    main()