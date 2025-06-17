def recomendaciones_personalizadas(objetivo, peso):
    objetivo = objetivo.lower()  # convierte todo a minúsculas para comparar
    proteina_diaria = peso * 2.2
    perder_grasa_diaria = peso * 0.5

    if objetivo == 'ganar masa muscular':
        return f"""
--- Recomendaciones para ganar masa muscular ---
La alimentación para aumentar masa muscular se basa en consumir proteínas, carbohidratos y grasas saludables.
• Proteínas: fundamentales para el crecimiento muscular.
• Carbohidratos: aportan energía para entrenar.
• Grasas saludables: apoyan funciones vitales.
• Aporte proteico recomendado: entre 1.6 y 2.4g/kg.
• Según tu peso ({peso}kg), tu ingesta ideal de proteínas es: {proteina_diaria:.2f}g diarios.
• Come entre 4 y 6 veces al día, distribuyendo la proteína en cada comida.
"""

    elif objetivo == 'perder grasa':
        return f"""
--- Recomendaciones para perder grasa ---
La base es una dieta equilibrada: frutas, verduras, proteínas magras, granos integrales y grasas saludables.
• Evita alimentos procesados, azúcares añadidos y grasas saturadas.
• Controla las porciones y mantente hidratado.
• Aplica un déficit calórico moderado (consumir menos calorías de las que quemas).
• Se recomienda perder entre 0.5 y 1 kg por semana.
• Según tu peso ({peso}kg), tu ingesta ideal de grasas es: {perder_grasa_diaria:.2f}g diarios.
"""

    elif objetivo == 'mejorar salud':
        return """
--- Recomendaciones para mejorar la salud ---
• Consume todos los grupos alimenticios: frutas, verduras, cereales integrales, lácteos bajos en grasa y proteínas.
• Limita grasas saturadas, azúcares y sodio.
• Las mejores fuentes de proteína: pescado, huevos, legumbres, productos de soya, nueces y semillas.
• Prefiere leche baja en grasa, sin lactosa o bebidas de soya fortificadas.
"""

    else:
        return "Objetivo no reconocido. No se pueden dar recomendaciones específicas."
