class Programador:
    def __init__(self, nombre: str, apellidos: str):
        Programador.validar_campo(nombre)
        Programador.validar_campo(apellidos)
        self.nombre = nombre
        self.apellidos = apellidos

    @staticmethod
    def validar_campo(campo: str):
        if any(c.isdigit() for c in campo):
            raise ValueError("El campo no puede contener dígitos.")
        if len(campo) >= 20:
            raise ValueError("La longitud del campo debe ser menor a 20 caracteres.")

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


class EquipoMaratonProgramacion:
    def __init__(self, nombre_equipo: str, universidad: str, lenguaje: str, capacidad: int):
        if capacidad not in [2, 3]:
            raise ValueError("El equipo debe tener 2 o 3 integrantes.")
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.capacidad = capacidad
        self.programadores = []

    def esta_lleno(self):
        return len(self.programadores) == self.capacidad

    def añadir(self, programador: Programador):
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar al programador.")
        self.programadores.append(programador)

    def mostrar_equipo(self):
        resultado = f"Equipo: {self.nombre_equipo}\n"
        resultado += f"Universidad: {self.universidad}\n"
        resultado += f"Lenguaje: {self.lenguaje}\n"
        resultado += "Integrantes:\n"
        for p in self.programadores:
            resultado += f" - {p}\n"
        return resultado