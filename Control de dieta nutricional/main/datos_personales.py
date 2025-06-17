def obtener_datos_usuario():
    print("\nBienvenido al sistema de control de dieta\n")

    while True:
        nombre = input("Ingrese su nombre: ")
        if nombre.strip():
            break
        print("El nombre no puede estar vacío.")

    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad > 0:
                break
            print("Edad inválida.")
        except ValueError:
            print("Debe ser un número.")

    while True:
        sexo = input("Ingrese su sexo (M/F): ").strip().upper()
        if sexo in ['M', 'F']:
            break
        print("Debe ingresar M o F.")

    while True:
        try:
            altura = float(input("Altura en metros (ej. 1.75): "))
            if altura > 0:
                break
            print("Altura inválida.")
        except ValueError:
            print("Debe ser un número.")

    while True:
        try:
            peso = float(input("Peso en kg: "))
            if peso > 0:
                break
            print("Peso inválido.")
        except ValueError:
            print("Debe ser un número.")

    while True:
        objetivo = input("Objetivo (Ganar masa muscular / Perder grasa / Mejorar salud): ").strip().lower()
        if objetivo in ['ganar masa muscular', 'perder grasa', 'mejorar salud']:
            break
        print("Objetivo no válido.")

    return {
        "nombre": nombre,
        "edad": edad,
        "sexo": 'Masculino' if sexo == 'M' else 'Femenino',
        "altura": altura,
        "peso": peso,
        "objetivo": objetivo.capitalize()
    }
