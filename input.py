# Control de dieta nutricional
# Pantalla de input con funciones

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

def main():
    name = pedir_texto("Ingrese su nombre o un apodo: ")
    age_or_dob = pedir_texto("Ingrese su edad (número entero) o su fecha de nacimiento (YYYY-MM-DD): ")
    if "-" in age_or_dob:
        print("Fecha de nacimiento registrada:", age_or_dob)

    act_fisica = pedir_numero(
        "Ingrese su nivel de actividad física (sedentario=1, ligero=2, moderado=3, alto=4, atleta=5): ",
        tipo=int, minimo=1, maximo=5
    )

    gen = pedir_opcion("Ingrese su género (M/F): ", ["m", "f"]).upper()
    high = pedir_numero("Ingrese su altura en metros: ", tipo=float, minimo=0.5)
    act_weight = pedir_numero("Ingrese su peso actual (kg): ", tipo=float, minimo=1)
    obj_weight = pedir_numero("Ingrese su peso objetivo (kg): ", tipo=float, minimo=1)

    print(f"Hola, {name}. Bienvenido a su control de dieta nutricional.")

    print("Por favor, ingrese sus objetivos y preferencias alimenticias.")
    obj_principal = pedir_texto("Ingrese su objetivo principal (pérdida de peso, ganancia muscular, mantenimiento, mejorar salud general): ").lower()
    dieta = pedir_texto("Ingrese su tipo de dieta preferida (vegetariana, vegana, omnívora, cetogénica, paleo): ").lower()
    alergia_list = pedir_lista_si_no("¿Tiene alguna alergia alimentaria? (sí/no): ", "Por favor, enumere sus alergias alimentarias separadas por comas: ")
    intolerancia_list = pedir_lista_si_no("¿Tiene alguna intolerancia alimentaria? (sí/no): ", "Por favor, enumere sus intolerancias alimentarias separadas por comas: ")
    comidas_por_dia = pedir_numero("¿Cuántas comidas realiza al día? (número entero): ", tipo=int, minimo=1)

    print(f"\nGracias por proporcionar su información, {name}.")
    print("Resumen de su información:")
    print(f"Nombre: {name}, edad o fecha de nacimiento: {age_or_dob}, género: {gen}, altura: {high} m, peso actual: {act_weight} kg, peso objetivo: {obj_weight} kg")
    print(f"Nivel de actividad física: {act_fisica}, objetivo principal: {obj_principal}, tipo de dieta: {dieta}, comidas por día: {comidas_por_dia}")
    print(f"Intolerancias: {', '.join(intolerancia_list) if intolerancia_list else 'Ninguna'}, alergias: {', '.join(alergia_list) if alergia_list else 'Ninguna'}")

if __name__ == "__main__":
    main()