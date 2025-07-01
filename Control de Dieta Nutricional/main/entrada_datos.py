
def pedir_texto(mensaje):
    return input(mensaje).strip()

def pedir_opcion(mensaje, opciones):
    while True:
        valor = input(mensaje).strip().lower()
        if valor in opciones:
            return valor
        print(f"Opción inválida. Opciones válidas: {', '.join(opciones)}")

def pedir_numero(mensaje, tipo=float, minimo=None, maximo=None):
    while True:
        try:
            valor = tipo(input(mensaje))
            if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                print(f"El valor debe estar entre {minimo} y {maximo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")

def pedir_lista_si_no(mensaje_si_no, mensaje_lista):
    respuesta = pedir_opcion(mensaje_si_no, ["sí", "si", "no"])
    if respuesta in ["sí", "si"]:
        return [item.strip() for item in input(mensaje_lista).split(",") if item.strip()]
    return []

def entrada_usuario():
    print("\nBienvenido al sistema de control de dieta\n")
    nombre = pedir_texto("Ingrese su nombre: ")
    edad = pedir_numero("Ingrese su edad: ", tipo=int, minimo=1)
    sexo = pedir_opcion("Ingrese su sexo (M/F): ", ["m", "f"]).upper()
    altura = pedir_numero("Ingrese su altura en metros (ejemplo: 1.75): ", minimo=0.5)
    peso_actual = pedir_numero("Ingrese su peso actual en kilogramos (ejemplo: 70.5): ", minimo=1)
    objetivo = pedir_opcion(
        "Ingrese su objetivo físico (ganar masa muscular, perder grasa, mejorar salud): ",
        ["ganar masa muscular", "perder grasa", "mejorar salud"]
    )
    return nombre, edad, sexo, altura, peso_actual, objetivo
