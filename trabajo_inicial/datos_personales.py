# Pantalla de inicio de la aplicacion (control de dieta)
# El sistema debe permitir ingresar datos básicos del usuario: nombre, edad, sexo o género, altura, peso actual, objetivo fisico 
# (Ganar masa muscular, perder grasa o mejorar salud)

# Datos basicos del usuario
print("\nBienvenido al sistema de control de dieta")
print ("\n")

# Solicitar nombre
while True:
    try:
        nombre = input("Ingrese su nombre: ")
        if nombre.strip():
            break
        else:
            print("El nombre no puede estar vacío. Inténtalo de nuevo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un nombre válido.")

# Solicitar edad
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad > 0:
            break
        else:
            print("La edad debe ser un número positivo. Inténtalo de nuevo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

# Solicitar sexo
while True:
    try:
        sexo = input("Ingrese su sexo (M/F): ").strip().upper()
        if sexo in ['M', 'F']:
            break
        else:
            print("Entrada inválida. Por favor, ingrese 'M' para masculino o 'F' para femenino.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese 'M' para masculino o 'F' para femenino.")

# Solicitar altura
while True:
    try:
        altura = float(input("Ingrese su altura en metros (ejemplo: 1.75): "))
        if altura > 0:
            break
        else:
            print("La altura debe ser un número positivo. Inténtalo de nuevo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")

# Solicitar peso actual
while True:
    try:
        peso_actual = float(input("Ingrese su peso actual en kilogramos (ejemplo: 70.5): "))
        if peso_actual > 0:
            break
        else:
            print("El peso debe ser un número positivo. Inténtalo de nuevo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")

# Solicitar objetivo físico
while True:
    objetivo = input("Ingrese su objetivo físico (Ganar masa muscular, Perder grasa, Mejorar salud): ").strip().lower()
    if objetivo in ['ganar masa muscular', 'perder grasa', 'mejorar salud']:
        break
    else:
        print("Entrada inválida. Por favor, ingrese uno de los siguientes objetivos: Ganar masa muscular, Perder grasa, Mejorar salud.")

# Imprimir los datos ingresados 
print("\nDatos ingresados:")
print(f"Nombre: {nombre.capitalize()}")
print(f"Edad: {edad} años")
print(f"Sexo: {'Masculino' if sexo == 'M' else 'Femenino'}")
print(f"Altura: {altura:.2f} metros")
print(f"Peso actual: {peso_actual} kg")
print(f"Objetivo físico: {objetivo.capitalize()}")

# Guardar los datos en un diccionario
datos_usuario = {
    'nombre': nombre.capitalize(),
    'edad': edad,
    'sexo': 'Masculino' if sexo == 'M' else 'Femenino',
    'altura': altura,
    'peso_actual': peso_actual,
    'objetivo': objetivo.capitalize()
}

# Recomendaciones basadas en el objetivo
proteina_diaria = peso_actual * 2.2  # Aproximación de gramos de proteína por kg de peso corporal
perder_grasa_diaria = peso_actual * 0.5  # Aproximación de gramos de grasa por kg de peso corporal

# Funcion por objetivo de ganar masa muscular
def masa_muscular(objetivo):
    if objetivo == 'ganar masa muscular':
        return f"""
            La alimentación para aumentar la masa muscular se basa en el consumo adecuado de macronutrientes: proteínas, carbohidratos y grasas saludables.
            Las proteínas son esenciales para la reparación y crecimiento de las fibras musculales, mientras que los carbohidratos proporcionan la energía necesaria para los entrenamientos y las grasas saludables apoyan funciones corporales vitales.
            Aporte proteico adecuado: Se recomienda consumir entre 1.6 y 2.4 gramos de proteína por kilogramo de peso corporal al día. Fuentes de proteínas de alta calidad incluyen carnes magras, pollo o pescado. 
            El aporte proteico segun el peso actual es de: {proteina_diaria} gramos diarios.
            Se recomienda consumir entre 4 y 6 comidas al día, distribuyendo las proteínas en cada una de ellas. (Cada 3 o 4 horas)
        """

# Funcion por objetivo de perder grasa
def perder_grasa(objetivo):
    if objetivo == 'perder grasa':
        return f"""
            Se recomienda enforcarse en una dieta equilibrada que incluya frutas, verduras, granos integrales, proteínas magras y grasas saludables.
            Se recomienda reducir el consumo de alimentos procesados, azucares añadidos y grasas saturadas. 
            Es importante tambien controlar las porciones y mantener una hidratacion adecuada.
            Se recomienda un déficit calórico moderado, lo que significa consumir menos calorías de las que se queman diariamente para promover la pérdida de grasa de manera saludable.
            Se recomiendan alimentos como aceite de oliva, carne magra, frutos secos, pescado, avena, arroz integral.
            Una forma saludable de bajar de peso es perder entre 0.5 y 1 kg por semana.
            El aporte de grasa segun el peso actual es de: {perder_grasa_diaria} gramos diarios.
            """

# Funcion por objetivo de mejorar salud
def mejorar_salud(objetivo):
    if objetivo == 'mejorar salud':
        return """
            Para una alimentación saludable, se recomienda incluir alimentos de todos los grupos: frutas, verduras, cereales integrales, lácteos bajos en grasa y proteínas. 
            Es importante limitar el consumo de grasas saturadas y trans, azúcar, y sodio. 
            La alimentación saludable enfatiza las frutas, las verduras, los cereales integrales, los productos lácteos y las proteínas. 
            Las recomendaciones de lácteos incluyen leche baja en grasa o sin grasa, leche sin lactosa y bebidas de soya fortificadas. 
            Otras bebidas de origen vegetal no tienen las mismas propiedades nutricionales que la leche de origen animal y las bebidas de soya. 
            Las recomendaciones de proteínas incluyen mariscos, carnes y aves magras, huevos, legumbres (frijoles, guisantes y lentejas), productos de soya, nueces y semillas.
            """

# Imprimir recomendaciones basadas en el objetivo
if objetivo == 'ganar masa muscular':
    print(masa_muscular(objetivo)) # Imprime recomendaciones para ganar masa muscular

elif objetivo == 'perder grasa':
    print(perder_grasa(objetivo)) # Imprime recomendaciones para perder grasa

elif objetivo == 'mejorar salud':
    print(mejorar_salud(objetivo)) # Imprime recomendaciones para mejorar salud
