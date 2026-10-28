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

def existe_Resena(usuario, linea):
    try:
        archivo = open("registros.csv", "r")
    except IOError:
        return False
    else:
        for fila in archivo:
            datos = fila.strip().split(",")
            if len(datos) >= 2 and datos[0] == usuario and datos[1] == linea:
                archivo.close()
                return True
        archivo.close()
        return False

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

def agregar_Resena_CSV(usuario_actual, conjunto_lineas):

    linea = pedirLinea(conjunto_lineas)
    
    if existe_Resena(usuario_actual, linea):
        print(f"Error: Ya has realizado una reseña para la línea {linea}. Utiliza la opción de editar.")
        return

    print(f"\n--- Nueva reseña para la línea {linea} ---")
    resena = ingresar_Resena() 
    
    archivo_nuevo = False

    try:
        archivo_prueba = open("registros.csv", "r")
    except IOError:
        archivo_nuevo = True
    else:
        archivo_prueba.close()
        
    try:
        archivo_escritura = open("registros.csv", "a")
    except IOError:
        print("Error: No se pudo guardar la reseña.")
    else:
        if archivo_nuevo:
            archivo_escritura.write("usuario,linea,espera,limpieza,ocupacion,comentario\n")
        
        archivo_escritura.write(f"{usuario_actual},{linea},{resena['espera']},{resena['limpieza']},{resena['ocupacion']},{resena['comentario']}\n")
        archivo_escritura.close()
        print("Reseña guardada exitosamente.")

def editar_Resena_CSV(usuario_actual, conjunto_lineas):
    linea = pedirLinea(conjunto_lineas)
    
    if not existe_Resena(usuario_actual, linea):
        print(f"Error: No tienes ninguna reseña registrada para la línea {linea}.")
        return

    registros_actualizados = []
    editado = False
    
    try:
        archivo = open("registros.csv", "r")
    except IOError:
        print("Error al leer el archivo para edición.")
        return
    else:
        for fila in archivo:
            datos = fila.strip().split(",")
            
            if len(datos) >= 6 and datos[0] == "usuario" and datos[1] == "linea":
                registros_actualizados.append(fila)
                continue

            if len(datos) >= 6:
                registro_dicc = {
                    "usuario": datos[0],
                    "linea": datos[1],
                    "espera": datos[2],
                    "limpieza": datos[3],
                    "ocupacion": datos[4],
                    "comentario": datos[5]
                }

                if registro_dicc["usuario"] == usuario_actual and registro_dicc["linea"] == linea:
                    print(f"\nReseña actual - Espera: {registro_dicc['espera']}, Limpieza: {registro_dicc['limpieza']}, Ocupación: {registro_dicc['ocupacion']}, Comentario: {registro_dicc['comentario']}")
                    print("--- Ingresa los nuevos valores ---")
                    
                    nueva_resena = ingresar_Resena()
                    
                    fila_nueva = f"{usuario_actual},{linea},{nueva_resena['espera']},{nueva_resena['limpieza']},{nueva_resena['ocupacion']},{nueva_resena['comentario']}\n"
                    registros_actualizados.append(fila_nueva)
                    editado = True
                else:
                    registros_actualizados.append(fila)
            else:
                registros_actualizados.append(fila)
                
        archivo.close()

    if editado:
        try:
            archivo_escritura = open("registros.csv", "w")
        except IOError:
            print("Error al reescribir el archivo de registros.")
        else:
            for registro in registros_actualizados:
                if not registro.endswith("\n"):
                    registro += "\n"
                archivo_escritura.write(registro)
            archivo_escritura.close()
            print("Reseña editada y archivo actualizado exitosamente.")