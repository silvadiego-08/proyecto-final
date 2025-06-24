# Lista con las comidas del día (simuladas)
comidas = [
    {
        "comida": "Desayuno",
        "calorías": 350,
        "proteínas": 20,
        "carbohidratos": 40,
        "grasas": 15
    },
    {
        "comida": "Almuerzo",
        "calorías": 600,
        "proteínas": 35,
        "carbohidratos": 50,
        "grasas": 25
    },
    {
        "comida": "Cena",
        "calorías": 500,
        "proteínas": 30,
        "carbohidratos": 45,
        "grasas": 20
    }
]

# Función que muestra el resumen diario
def resumen_dieta(comidas):
    # Suma de todos los nutrientes del día
    total_calorias = sum(c["calorías"] for c in comidas)
    total_proteinas = sum(c["proteínas"] for c in comidas)
    total_carbs = sum(c["carbohidratos"] for c in comidas)
    total_grasas = sum(c["grasas"] for c in comidas)

    # Mostrar resumen general al usuario
    print("Resumen diario de dieta:")
    print(f"Total calorías: {total_calorias} kcal")
    print(f"Proteínas: {total_proteinas} g")
    print(f"Carbohidratos: {total_carbs} g")
    print(f"Grasas: {total_grasas} g")

# Simula que ya se registró la última comida del día
print(" Última comida registrada. Generando resumen...\n")
resumen_dieta(comidas)
