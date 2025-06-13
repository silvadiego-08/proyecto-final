#Control de dieta nutricional
#Pantalla de input
name = input("Ingrese su nombre o un apodo: ")
age_or_dob = input("Ingrese su edad (número entero) o su fecha de nacimiento (YYYY-MM-DD): ")
try:
	if "-" in age_or_dob:
		dob = age_or_dob  # Assuming the user entered a date of birth
		print("Fecha de nacimiento registrada:", dob)
except Exception as e:
	print("Error al procesar la fecha de nacimiento o edad:", e)

while True:
	try:
		act_fisica = int(input("Ingrese su nivel de actividad física (sedentario=1, ligero=2, moderado=3, alto=4, atleta=5): "))
		if 1 <= act_fisica <= 5:
			break
		else:
			print("Por favor, ingrese un número válido entre 1 y 5.")
	except ValueError:
		print("Entrada inválida. Por favor, ingrese un número entre 1 y 5.")
gen = input("Ingrese su género (M/F): ")
high = float(input("Ingrese su altura en metros: "))
act_weight = float(input("Ingrese su peso actual (kg): "))
obj_weight = float(input("Ingrese su peso objetivo (kg): "))
print("Hola, " + str(name) + " Bienvenido a su control de dieta nutricional.")

#Objetivos y preferencias alimenticias
print("Por favor, ingrese sus objetivos y preferencias alimenticias.")
obj_principal = input("Ingrese su objetivo principal (pérdida de peso, ganancia muscular, mantenimiento, mejorar salud general): ").lower()
alergias = input("¿Tiene alguna alergia alimentaria? (sí/no): ").lower()
if alergias == "sí":
	alergia_list = input("Por favor, enumere sus alergias alimentarias separadas por comas: ").split(",")
else:
	alergia_list = []

intolerancias = input("¿Tiene alguna intolerancia alimentaria? (sí/no): ").lower()
if intolerancias == "sí":
	intolerancia_list = input("Por favor, enumere sus intolerancias alimentarias separadas por comas: ").split(",")
else:
	intolerancia_list = []
    
comidas_por_dia = input("¿Cuántas comidas realiza al día? (número entero): ")
print("Gracias por proporcionar su información, " + str(name) + ".")
print("Resumen de su información:")
print(f"Nombre: {name}, edad o fecha de nacimiento: {age_or_dob}, género: {gen}, altura: {high} m, peso actual: {act_weight} kg, peso objetivo: {obj_weight} kg")
print(f"Nivel de actividad física: {act_fisica}, objetivo principal: {obj_principal}, comidas por día: {comidas_por_dia}, intolerancias: {intolerancias}, alergias: {alergias}")
