class PruebaExcepciones:
    def __init__(self):
        pass
    
    def primer_bloque_try(self):
        mensajes = []
        try:
            mensajes.append("Ingresando al primer try")
            cociente = 10000 / 0
            mensajes.append("Después de la división")
        except ZeroDivisionError as e:
            mensajes.append("División por cero")
        finally:
            mensajes.append("Ingresando al primer finally")
        return mensajes
    
    def segundo_bloque_try(self):
        mensajes = []
        try:
            mensajes.append("Ingresando al segundo try")
            objeto = None
            objeto.upper()
            mensajes.append("Imprimiendo objeto")
        except ZeroDivisionError as e:
            mensajes.append("División por cero")
        except Exception as e:
            mensajes.append("Ocurrió una excepción")
        finally:
            mensajes.append("Ingresando al segundo finally")
        return mensajes
    
    def ejecutar_ambos_bloques(self):
        todos_mensajes = []
        todos_mensajes.extend(self.primer_bloque_try())
        todos_mensajes.extend(self.segundo_bloque_try())
        return todos_mensajes