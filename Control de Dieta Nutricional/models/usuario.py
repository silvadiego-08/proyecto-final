
class Usuario:
    def __init__(self, nombre, edad, sexo, altura, peso_actual, objetivo):
        self.nombre = nombre.capitalize()
        self.edad = edad
        self.sexo = 'Masculino' if sexo.upper() == 'M' else 'Femenino'
        self.altura = altura
        self.peso_actual = peso_actual
        self.objetivo = objetivo.capitalize()

    def resumen(self):
        return (
            f"Nombre: {self.nombre}\n"
            f"Edad: {self.edad} años\n"
            f"Sexo: {self.sexo}\n"
            f"Altura: {self.altura:.2f} metros\n"
            f"Peso actual: {self.peso_actual} kg\n"
            f"Objetivo físico: {self.objetivo}\n"
        )
