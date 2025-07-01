from main.datos_personales import obtener_datos_usuario
from main.registro_comidas import registrar_comidas
from models.resumen import mostrar_resumen
from models.recomendaciones import recomendaciones_personalizadas

def main():
    intentos = 3
    while intentos > 0:
        password = input("Ingrese la contraseña para acceder al sistema: ")
        if password == "duran2025":
            break
        else:
            intentos -= 1
            print(f"Contraseña incorrecta. Intentos restantes: {intentos}")
    else:
        print("Acceso denegado. Ha superado el número de intentos.")
        return
    
    usuario = obtener_datos_usuario()
    comidas = registrar_comidas()
    mostrar_resumen(comidas)
    print(recomendaciones_personalizadas(usuario['objetivo'], usuario['peso']))

if __name__ == "__main__":
    main()

