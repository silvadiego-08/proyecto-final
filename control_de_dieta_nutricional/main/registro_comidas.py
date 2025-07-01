def registrar_comidas():
    comidas = []
    while True:
        print("\n--- Registro de Comidas ---")
        nombre = input("Nombre de la comida (o 'salir'): ")
        if nombre.lower() == 'salir':
            break

        porcion = input("Porción: ")
        calorias = float(input("Calorías: "))
        proteinas = float(input("Proteínas (g): "))
        carbohidratos = float(input("Carbohidratos (g): "))
        grasas = float(input("Grasas (g): "))

        comida = {
            "nombre": nombre,
            "porcion": porcion,
            "calorías": calorias,
            "proteínas": proteinas,
            "carbohidratos": carbohidratos,
            "grasas": grasas
        }

        comidas.append(comida)
        print("Comida registrada.\n")

    return comidas
