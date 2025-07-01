
CLAVE = "duran2025"  # Contraseña fija para acceso

def inicio_sesion():
    print("=== BIENVENIDO A TU CONTROL DE DIETA NUTRICIONAL ===")
    print("=== Favor inicia sesion en tu cuenta ===")
    intento = input("Ingresa la contraseña: ")
    if intento == CLAVE:
        print("Acceso permitido\n")
        return True
    else:
        print("Contraseña incorrecta. Acceso denegado.\n")
        return False
