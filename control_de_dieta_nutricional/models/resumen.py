def mostrar_resumen(comidas):
    total_calorias = sum(c["calorías"] for c in comidas)
    total_proteinas = sum(c["proteínas"] for c in comidas)
    total_carbs = sum(c["carbohidratos"] for c in comidas)
    total_grasas = sum(c["grasas"] for c in comidas)

    print("\nResumen diario de dieta:")
    print(f"Total calorías: {total_calorias} kcal")
    print(f"Proteínas: {total_proteinas} g")
    print(f"Carbohidratos: {total_carbs} g")
    print(f"Grasas: {total_grasas} g")
