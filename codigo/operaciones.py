import re

def Menu_Autenticacion():
    usuario_logueado = None
    while not usuario_logueado:
        print("\n==== Menú de Acceso ====")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Salir")
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            usuario_logueado = Iniciar_Sesion()
        elif opcion == "2":
            Registrar_Usuario()
        elif opcion == "3":
            return None
        else:
            print("Opción inválida. Intente nuevamente.")
            
    return usuario_logueado

def Iniciar_Sesion():
    usuario = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    
    try:
        archivo = open("usuarios.csv", "r")
    except IOError:
        print("Error: No se pudo acceder al archivo de usuarios o aún no hay usuarios registrados.")
        return None
    else:
        for linea in archivo:
            datos = linea.strip().split(",")
            if len(datos) == 2:
                if datos[0] == usuario and datos[1] == password:
                    print(f"\n¡Bienvenido/a al sistema, {usuario}!")
                    archivo.close()
                    return usuario
        archivo.close()
        print("Error: Usuario o contraseña incorrectos.")
        return None


def Registrar_Usuario():
    
    usuarios_existentes = []
    try:
        archivo = open("usuarios.csv", "r", encoding="utf-8")
    except IOError:
        # Si el archivo no existe aún, la lista queda vacía y continuará normalmente
        pass
    else:
        for linea in archivo:
            datos = linea.strip().split(",")
            if len(datos) > 0 and datos[0]:
                usuarios_existentes.append(datos[0])
        archivo.close()

    usuario_valido = False
    while not usuario_valido:
        usuario = input("Ingrese nuevo usuario (solo letras y números, sin espacios): ")
        
        # Validar formato con Regex
        if not re.match(r"[a-zA-Z0-9]+", usuario):
            print("Error: El usuario solo puede contener letras y números, sin espacios.")
            continue  # Vuelve a pedir el usuario
            
        if usuario in usuarios_existentes:
            print("Error: El usuario ya se encuentra registrado.")
        else:
            usuario_valido = True

    password_valida = False
    while not password_valida:
        password = input("Ingrese contraseña (mínimo 6 caracteres, SOLO letras y números): ")
        
        if re.match(r"[A-Za-z0-9]{6,}", password):
            password_valida = True
        else:
            print("Error: La contraseña debe tener al menos 6 caracteres y solo puede contener letras y números.")

    try:
        archivo_escritura = open("usuarios.csv", "a", encoding="utf-8")
    except IOError:
        print("Error: No se pudo guardar el usuario en el archivo.")
    else:
        archivo_escritura.write(f"{usuario},{password}\n")
        archivo_escritura.close()
        print("Usuario registrado exitosamente. Ahora puede iniciar sesión.")


def Ver_Menu():
    print("\n==== Menú Principal Subtexd ====")
    print("1. Gestión de Reseñas")
    print("2. Consultas")
    print("3. Estadísticas y generación de reporte")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")
    return opcion