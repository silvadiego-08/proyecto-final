
def masa_muscular(peso_actual):
    proteina_diaria = peso_actual * 2.2
    return f"""
La alimentación para aumentar la masa muscular se basa en el consumo adecuado de macronutrientes: proteínas, carbohidratos y grasas saludables.
Las proteínas son esenciales para la reparación y crecimiento de las fibras musculares, mientras que los carbohidratos proporcionan la energía necesaria para los entrenamientos y las grasas saludables apoyan funciones corporales vitales.
Aporte proteico adecuado: Se recomienda consumir entre 1.6 y 2.4 gramos de proteína por kilogramo de peso corporal al día.
Fuentes de proteínas de alta calidad incluyen carnes magras, pollo o pescado.
El aporte proteico según el peso actual es de: {proteina_diaria:.2f} gramos diarios.
Se recomienda consumir entre 4 y 6 comidas al día, distribuyendo las proteínas en cada una de ellas. (Cada 3 o 4 horas)
"""

def perder_grasa(peso_actual):
    grasa_diaria = peso_actual * 0.5
    return f"""
Se recomienda enfocarse en una dieta equilibrada que incluya frutas, verduras, granos integrales, proteínas magras y grasas saludables.
Se recomienda reducir el consumo de alimentos procesados, azúcares añadidos y grasas saturadas.
Es importante también controlar las porciones y mantener una hidratación adecuada.
Se recomienda un déficit calórico moderado, lo que significa consumir menos calorías de las que se queman diariamente para promover la pérdida de grasa de manera saludable.
Se recomiendan alimentos como aceite de oliva, carne magra, frutos secos, pescado, avena, arroz integral.
Una forma saludable de bajar de peso es perder entre 0.5 y 1 kg por semana.
El aporte de grasa según el peso actual es de: {grasa_diaria:.2f} gramos diarios.
"""

def mejorar_salud():
    return """
Para una alimentación saludable, se recomienda incluir alimentos de todos los grupos: frutas, verduras, cereales integrales, lácteos bajos en grasa y proteínas.
Es importante limitar el consumo de grasas saturadas y trans, azúcar, y sodio.
La alimentación saludable enfatiza las frutas, las verduras, los cereales integrales, los productos lácteos y las proteínas.
Las recomendaciones de lácteos incluyen leche baja en grasa o sin grasa, leche sin lactosa y bebidas de soya fortificadas.
Otras bebidas de origen vegetal no tienen las mismas propiedades nutricionales que la leche de origen animal y las bebidas de soya.
Las recomendaciones de proteínas incluyen mariscos, carnes y aves magras, huevos, legumbres (frijoles, guisantes y lentejas), productos de soya, nueces y semillas.
"""

def mostrar_recomendacion(objetivo, peso_actual):
    if objetivo == "ganar masa muscular":
        print(masa_muscular(peso_actual))
    elif objetivo == "perder grasa":
        print(perder_grasa(peso_actual))
    elif objetivo == "mejorar salud":
        print(mejorar_salud())
