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

    try:
            archivo = open("usuarios.csv", "a+")
    except IOError:
        print("Error: No se pudo acceder al archivo de usuarios.")
        return
    else:
        usuario_valido = False
        while not usuario_valido:
            usuario = input("Ingrese nuevo usuario (solo letras y números, sin espacios): ")
            
            # Validar formato con Regex estricto (inicio ^ y fin $)
            if not re.match(r"^[a-zA-Z0-9]+$", usuario):
                print("Error: El usuario solo puede contener letras y números, sin espacios.")
                continue

            archivo.seek(0)
            
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) > 0 and datos[0] == usuario:
                    print("Error: El usuario ya se encuentra registrado.")
                    break
            else:
                usuario_valido = True

        password_valida = False
        while not password_valida:
            password = input("Ingrese contraseña (mínimo 6 caracteres, SOLO letras y números): ")
            
            # Validar formato con Regex estricto (inicio ^ y fin $)
            if re.match(r"^[A-Za-z0-9]{6,}$", password):
                password_valida = True
            else:
                print("Error: La contraseña debe tener al menos 6 caracteres y solo puede contener letras y números.")

        archivo.write(f"{usuario},{password}\n")
        archivo.close()
        print("Usuario registrado exitosamente. Ahora puede iniciar sesión.")
            
def Ver_Menu():
    print("\n==== Menú Principal Subtexd ====")
    print("1. Gestión de Reseñas")
    print("2. Consultas")
    print("3. Estadísticas y generación de reporte")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")
    return opcion

def Gestionar_Resenas(usuario_actual, TuplaLineas):
    opcion = ""
    while opcion != "0":
        print("\n==== Gestión de reseñas ====")
        print("1. Cargar reseña")
        print("2. Editar reseña")
        print("0. Volver al menú")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            agregar_Resena_CSV(usuario_actual, TuplaLineas)
        elif opcion == "2":
            editar_Resena_CSV(usuario_actual, TuplaLineas)
        elif opcion == "0":
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida. Intente nuevamente.")


def pedirLinea(TuplaLineas):
    linea = input("Ingrese el nombre de la línea: ").upper()
    while linea not in TuplaLineas:
        print("La línea no existe o no es válida.")
        linea = input("Ingrese el nombre de la línea nuevamente: ").upper()
    return linea

def ingresar_Resena():

    validar_Rango = False
    while not validar_Rango:
        try:
            limpieza = int(input("Ingrese la calificación de Limpieza (1-5): "))
            validar_Rango = 1 <= limpieza <= 5
        except ValueError:
            validar_Rango = False
        if not validar_Rango:
            print("La calificación debe ser un número entre 1 y 5. Intente nuevamente.")

    validar_Rango = False
    while not validar_Rango:
        try:
            espera = int(input("Ingrese la calificación de Espera (1-5): "))
            validar_Rango = 1 <= espera <= 5
        except ValueError:
            validar_Rango = False
        if not validar_Rango:
            print("La calificación debe ser un número entre 1 y 5. Intente nuevamente.")

    validar_Rango = False
    while not validar_Rango:
        try:
            ocupacion = int(input("Ingrese la calificación de Ocupación (1-5): "))
            validar_Rango = 1 <= ocupacion <= 5
        except ValueError:
            validar_Rango = False
        if not validar_Rango:
            print("La calificación debe ser un número entre 1 y 5. Intente nuevamente.")

    comentario = input("Ingrese un comentario (opcional): ").strip().upper()

    diccionario_resena = {
        "limpieza": limpieza,
        "espera": espera,
        "ocupacion": ocupacion,
        "comentario": comentario
    }
    
    return diccionario_resena

def existe_Resena(usuario, linea, resenas_memoria):

    if linea in resenas_memoria and usuario in resenas_memoria[linea]:
        return True
    return False


def agregar_Resena_CSV(usuario_actual, conjunto_lineas):
    linea = pedirLinea(conjunto_lineas)
    resenas = {}
    archivo_nuevo = False
    
    try:
        archivo = open("registros.csv", "r+")
    except IOError:
        archivo_nuevo = True
    else:
        for fila in archivo:
            datos = fila.strip().split(",")
            if len(datos) >= 6 and datos[0] != "usuario":
                usr = datos[0]
                lin = datos[1]
                
                if lin not in resenas:
                    resenas[lin] = {}
                    
                resenas[lin][usr] = {
                    "espera": datos[2],
                    "limpieza": datos[3],
                    "ocupacion": datos[4],
                    "comentario": datos[5]
                }
                
    if not archivo_nuevo and existe_Resena(usuario_actual, linea, resenas):
        print(f"Error: Ya has realizado una reseña para la línea {linea}. Utiliza la opción de editar.")
        archivo.close()
        return

    print(f"\n--- Nueva reseña para la línea {linea} ---")
    nueva_resena = ingresar_Resena()

    if linea not in resenas:
        resenas[linea] = {}
        
    resenas[linea][usuario_actual] = {
        "espera": str(nueva_resena["espera"]),
        "limpieza": str(nueva_resena["limpieza"]),
        "ocupacion": str(nueva_resena["ocupacion"]),
        "comentario": nueva_resena["comentario"]
    }

    if archivo_nuevo:
        try:
            archivo = open("registros.csv", "w+")
        except IOError:
            print("Error: No se pudo crear el archivo de registros.")
            return

    archivo.seek(0)
    archivo.truncate()
    archivo.write("usuario,linea,espera,limpieza,ocupacion,comentario\n")
    
    for lin in resenas:
        for usr in resenas[lin]:
            datos_resena = resenas[lin][usr]
            archivo.write(f"{usr},{lin},{datos_resena['espera']},{datos_resena['limpieza']},{datos_resena['ocupacion']},{datos_resena['comentario']}\n")
            
    archivo.close()
    print("Reseña guardada exitosamente.")


def editar_Resena_CSV(usuario_actual, conjunto_lineas):
    linea = pedirLinea(conjunto_lineas)
    resenas = {}
    
    try:
        archivo = open("registros.csv", "r+")
    except IOError:
        print("Error: El archivo de registros no existe. No hay reseñas para editar.")
        return
    else:
        for fila in archivo:
            datos = fila.strip().split(",")
            if len(datos) >= 6 and datos[0] != "usuario":
                usr = datos[0]
                lin = datos[1]
                
                if lin not in resenas:
                    resenas[lin] = {}
                    
                resenas[lin][usr] = {
                    "espera": datos[2],
                    "limpieza": datos[3],
                    "ocupacion": datos[4],
                    "comentario": datos[5]
                }
                
        if not existe_Resena(usuario_actual, linea, resenas):
            print(f"Error: No tienes ninguna reseña registrada para la línea {linea}.")
            archivo.close()
            return
            
        actual = resenas[linea][usuario_actual]
        print(f"\nReseña actual - Espera: {actual['espera']}, Limpieza: {actual['limpieza']}, Ocupación: {actual['ocupacion']}, Comentario: {actual['comentario']}")
        print("--- Ingresa los nuevos valores ---")
        
        nueva_resena = ingresar_Resena()
        
        # Modificamos directamente en el diccionario anidado en memoria
        resenas[linea][usuario_actual] = {
            "espera": str(nueva_resena["espera"]),
            "limpieza": str(nueva_resena["limpieza"]),
            "ocupacion": str(nueva_resena["ocupacion"]),
            "comentario": nueva_resena["comentario"]
        }
        
        archivo.seek(0)
        archivo.truncate()
        archivo.write("usuario,linea,espera,limpieza,ocupacion,comentario\n")
        
        for lin in resenas:
            for usr in resenas[lin]:
                datos_resena = resenas[lin][usr]
                archivo.write(f"{usr},{lin},{datos_resena['espera']},{datos_resena['limpieza']},{datos_resena['ocupacion']},{datos_resena['comentario']}\n")
                
        archivo.close()
        print("Reseña editada y archivo actualizado exitosamente.")