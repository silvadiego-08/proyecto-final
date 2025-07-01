
from dao.autenticacion import inicio_sesion
from main.entrada_datos import entrada_usuario
from main.recomendaciones import mostrar_recomendacion
from models.usuario import Usuario

def main():
    if not inicio_sesion():
        print("No se puede acceder al sistema.")
        return

    nombre, edad, sexo, altura, peso_actual, objetivo = entrada_usuario()
    usuario = Usuario(nombre, edad, sexo, altura, peso_actual, objetivo)

    print("\nDatos ingresados:")
    print(usuario.resumen())

    mostrar_recomendacion(objetivo.lower(), peso_actual)

if __name__ == "__main__":
    main()
