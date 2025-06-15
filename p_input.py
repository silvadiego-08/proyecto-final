import datos_personales
def registrar_comidas():
    comidas = []
    while True:
        print("\n--- Registro de Comidas ---")
        nombre = input("Nombre de la comida (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        porcion = input("Porción (ejemplo: 100g, 1 taza, etc.): ")
        calorias = input("Calorías: ")
        proteinas = input("Proteínas (g): ")
        carbohidratos = input("Carbohidratos (g): ")
        grasas = input("Grasas (g): ")

        comida = {
            "nombre": nombre,
            "porcion": porcion,
            "calorias": float(calorias),
            "proteinas": float(proteinas),
            "carbohidratos": float(carbohidratos),
            "grasas": float(grasas)
        }
        comidas.append(comida)
        print("Comida registrada exitosamente.")

    print("\n--- Resumen de Comidas Ingresadas ---")
    for c in comidas:
        print(f"{c['nombre']} - Porción: {c['porcion']}, Calorías: {c['calorias']} kcal, Proteínas: {c['proteinas']}g, Carbohidratos: {c['carbohidratos']}g, Grasas: {c['grasas']}g")

if __name__ == "__main__":
    registrar_comidas()