def guardar_en_archivo(usuario, comidas, ruta="registro_dieta.txt"):
    with open(ruta, "a") as archivo:
        archivo.write(f"Usuario: {usuario['nombre']} - Objetivo: {usuario['objetivo']}\n")
        for c in comidas:
            archivo.write(f"{c['nombre']} | {c['porcion']} | {c['calorías']} kcal | {c['proteínas']}g P | {c['carbohidratos']}g C | {c['grasas']}g G\n")
        archivo.write("\n")
