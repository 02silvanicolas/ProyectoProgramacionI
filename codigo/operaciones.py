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
    if not re.match(r"^[a-zA-Z0-9]+$", usuario):
        print("Error: Formato de usuario inválido (solo letras y números, sin espacios).")
        return None

    password = input("Ingrese su contraseña: ")
    if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z0-9]{6,}$", password):
        print("Error: Formato de contraseña inválido (mínimo 6 caracteres, con letras y números).")
        return None
    
    try:
        with open("usuarios.csv", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) == 2:
                    if datos[0].strip().lower() == usuario.lower() and datos[1].strip() == password:
                        usuario_registrado = datos[0].strip() 
                        print(f"\n¡Bienvenido/a al sistema, {usuario_registrado}!")
                        return usuario_registrado
    except IOError:
        print("Error: No se pudo acceder al archivo de usuarios o aún no hay usuarios registrados.")
        return None
        
    print("Error: Usuario o contraseña incorrectos.")
    return None


def Registrar_Usuario():
    usuario_valido = False
    while not usuario_valido:
        usuario = input("Ingrese nuevo usuario (solo letras y números, sin espacios): ")
        
        if not re.match(r"^[a-zA-Z0-9]+$", usuario):
            print("Error: El usuario solo puede contener letras y números, sin espacios.")
            continue

        usuario_existe = False
        try:
            with open("usuarios.csv", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")
                    if len(datos) > 0 and datos[0].strip().lower() == usuario.lower():
                        usuario_existe = True
                        break
        except IOError:
            print("No se encontró el archivo de usuarios. Se creará uno nuevo al registrar el usuario.")
            usuario_existe = False

        if usuario_existe:
            print("Error: El usuario ya se encuentra registrado.")
        else:
            usuario_valido = True

    password_valida = False
    while not password_valida:
        password = input("Ingrese contraseña (mínimo 6 caracteres, con letras y números): ")
        
        if re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z0-9]{6,}$", password):
            password_valida = True
        else:
            print("Error: La contraseña debe tener al menos 6 caracteres e incluir letras y números (sin símbolos ni espacios).")

    try:
        with open("usuarios.csv", "a", encoding="utf-8") as archivo:
            archivo.write(f"{usuario},{password}\n")
        print("Usuario registrado exitosamente. Ahora puede iniciar sesión.")
    except IOError:
        print("Error: No se pudo acceder al archivo de usuarios para guardar el registro.")
            
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

def Consultas(usuario_actual, conjunto_lineas):
    opcion = ""
    while opcion != "0":
        print("\n==== Consultas ====")
        print("1. Consultar mis reseñas")
        print("2. Consultar reseñas por línea")
        print("0. Volver al menú")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            consultar_Resenas_Usuario_CSV(usuario_actual)
        elif opcion == "2":
            consultar_Resenas_Linea_CSV(conjunto_lineas)
        elif opcion == "0":
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida. Intente de nuevo.")

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
            espera = int(input("Ingrese la calificación de Espera (1-5): "))
            validar_Rango = 1 <= espera <= 5
        except ValueError:
            validar_Rango = False
            if not validar_Rango:
                print("La calificación debe ser un número entre 1 y 5. Intente nuevamente.")
        

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
            ocupacion = int(input("Ingrese la calificación de Ocupación (1-5): "))
            validar_Rango = 1 <= ocupacion <= 5
        except ValueError:
            validar_Rango = False
        if not validar_Rango:
            print("La calificación debe ser un número entre 1 y 5. Intente nuevamente.")

    comentario = input("Ingrese un comentario (opcional): ").strip().upper().replace(",", ";")

    diccionario_resena = {
        "espera": espera,
        "limpieza": limpieza,
        "ocupacion": ocupacion,
        "comentario": comentario
    }
    
    return diccionario_resena

def existe_Resena(usuario, linea, resenas_memoria):
    if linea in resenas_memoria:
        for usr in resenas_memoria[linea]:
            if usr.lower() == usuario.lower():
                return True
    return False

def agregar_Resena_CSV(usuario_actual, conjunto_lineas):
    linea = pedirLinea(conjunto_lineas)
    resenas = {}
    archivo_existe = True
    
    try:
        with open("registros.csv", "r", encoding="utf-8") as archivo:
            for fila in archivo:
                datos = fila.strip().split(",")
                if len(datos) >= 6 and datos[0] != "usuario":
                    try:
                        esp = int(datos[2])
                        lim = int(datos[3])
                        ocu = int(datos[4])
                        if not (1 <= esp <= 5 and 1 <= lim <= 5 and 1 <= ocu <= 5):
                            continue
                    except ValueError:
                        continue

                    usr = datos[0]
                    lin = datos[1].upper()
                    if lin not in resenas:
                        resenas[lin] = {}
                    resenas[lin][usr] = {
                        "espera": datos[2],
                        "limpieza": datos[3],
                        "ocupacion": datos[4],
                        "comentario": datos[5]
                    }
    except IOError:
        archivo_existe = False

    if archivo_existe and existe_Resena(usuario_actual, linea, resenas):
        print(f"Error: Ya has realizado una reseña para la línea {linea}. Utiliza la opción de editar.")
        return

    print(f"\n--- Nueva reseña para la línea {linea} ---")
    nueva_resena = ingresar_Resena()

    try:
        modo = "a" if archivo_existe else "w"
        with open("registros.csv", modo, encoding="utf-8") as archivo:
            if not archivo_existe:
                archivo.write("usuario,linea,espera,limpieza,ocupacion,comentario\n")
            archivo.write(f"{usuario_actual},{linea},{nueva_resena['espera']},{nueva_resena['limpieza']},{nueva_resena['ocupacion']},{nueva_resena['comentario']}\n")
        print("Reseña guardada exitosamente.")
    except IOError:
        print("Error: No se pudo guardar la reseña en el archivo de registros.")

def editar_Resena_CSV(usuario_actual, conjunto_lineas):
    linea = pedirLinea(conjunto_lineas)
    resenas = {}
    
    try:
        with open("registros.csv", "r", encoding="utf-8") as archivo:
            for fila in archivo:
                datos = fila.strip().split(",")
                if len(datos) >= 6 and datos[0] != "usuario":
                    try:
                        esp = int(datos[2])
                        lim = int(datos[3])
                        ocu = int(datos[4])
                        if not (1 <= esp <= 5 and 1 <= lim <= 5 and 1 <= ocu <= 5):
                            continue
                    except ValueError:
                        continue

                    usr = datos[0]
                    lin = datos[1].upper()
                    if lin not in resenas:
                        resenas[lin] = {}
                    resenas[lin][usr] = {
                        "espera": datos[2],
                        "limpieza": datos[3],
                        "ocupacion": datos[4],
                        "comentario": datos[5]
                    }
    except IOError:
        print("Error: El archivo de registros no existe. No hay reseñas para editar.")
        return

    if not existe_Resena(usuario_actual, linea, resenas):
        print(f"Error: No tienes ninguna reseña registrada para la línea {linea}.")
        return

    # Buscar la clave exacta del usuario en el diccionario (por si difieren mayúsculas/minúsculas)
    usuario_clave = usuario_actual
    for usr in resenas[linea]:
        if usr.lower() == usuario_actual.lower():
            usuario_clave = usr
            break

    actual = resenas[linea][usuario_clave]
    print(f"\nReseña actual - Espera: {actual['espera']}, Limpieza: {actual['limpieza']}, Ocupación: {actual['ocupacion']}, Comentario: {actual['comentario']}")
    print("--- Ingresa los nuevos valores ---")
    
    nueva_resena = ingresar_Resena()
    
    resenas[linea][usuario_clave] = {
        "espera": str(nueva_resena["espera"]),
        "limpieza": str(nueva_resena["limpieza"]),
        "ocupacion": str(nueva_resena["ocupacion"]),
        "comentario": nueva_resena["comentario"]
    }
    
    try:
        with open("registros.csv", "w", encoding="utf-8") as archivo:
            archivo.write("usuario,linea,espera,limpieza,ocupacion,comentario\n")
            for lin in resenas:
                for usr in resenas[lin]:
                    datos_resena = resenas[lin][usr]
                    archivo.write(f"{usr},{lin},{datos_resena['espera']},{datos_resena['limpieza']},{datos_resena['ocupacion']},{datos_resena['comentario']}\n")
        print("Reseña editada y archivo actualizado exitosamente.")
    except IOError:
        print("Error: No se pudo actualizar el archivo de registros.")

def consultar_Resenas_Usuario_CSV(usuario_actual):
    print(f"\n--- Reseñas de {usuario_actual} ---")
    encontradas = False
    
    try:
        with open("registros.csv", "r", encoding="utf-8") as archivo:
            for fila in archivo:
                datos = fila.strip().split(",")
                if len(datos) >= 6 and datos[0] != "usuario":
                    try:
                        esp = int(datos[2])
                        lim = int(datos[3])
                        ocu = int(datos[4])
                        if not (1 <= esp <= 5 and 1 <= lim <= 5 and 1 <= ocu <= 5):
                            continue
                    except ValueError:
                        continue

                    if datos[0].lower() == usuario_actual.lower():
                        print(f"Línea {datos[1].upper()} -> Limpieza: {lim}, Espera: {esp}, Ocupación: {ocu}, Comentario: {datos[5]}")
                        encontradas = True
    except IOError:
        print("Aún no hay reseñas registradas en el sistema.")
        return
        
    if not encontradas:
        print("No has realizado ninguna reseña todavía.")

def consultar_Resenas_Linea_CSV(conjunto_lineas):
    linea = pedirLinea(conjunto_lineas) 
    print(f"\n--- Reseñas para la Línea {linea} ---")
    encontradas = False
    
    try:
        with open("registros.csv", "r", encoding="utf-8") as archivo:
            for fila in archivo:
                datos = fila.strip().split(",")
                if len(datos) >= 6 and datos[0] != "usuario":
                    try:
                        esp = int(datos[2])
                        lim = int(datos[3])
                        ocu = int(datos[4])
                        if not (1 <= esp <= 5 and 1 <= lim <= 5 and 1 <= ocu <= 5):
                            continue
                    except ValueError:
                        continue

                    if datos[1].upper() == linea:
                        print(f"Usuario {datos[0]} -> Limpieza: {lim}, Espera: {esp}, Ocupación: {ocu}, Comentario: {datos[5]}")
                        encontradas = True
    except IOError:
        print("Aún no hay reseñas registradas en el sistema.")
        return
        
    if not encontradas:
        print(f"No hay reseñas para la línea {linea}.")

def Estadisticas(conjunto_lineas):
    print("\n==== Estadísticas y Generación de Reporte ====")
    
    estadisticas = {}
    for linea in conjunto_lineas:
        estadisticas[linea] = {
            "limpieza_altas": 0,     
            "espera_total": 0,
            "limpieza_total": 0,
            "ocupacion_total": 0,
            "total_reseñas": 0,
            "espera_1_estrella": 0    
        }
        
    try:
        with open("registros.csv", "r", encoding="utf-8") as archivo:
            for fila in archivo:
                datos = fila.strip().split(",")
                
                if len(datos) >= 6 and datos[0] != "usuario":
                    linea = datos[1].upper()
                    
                    if linea in estadisticas:
                        try:
                            espera = int(datos[2])
                            limpieza = int(datos[3])
                            ocupacion = int(datos[4])
                            if not (1 <= espera <= 5 and 1 <= limpieza <= 5 and 1 <= ocupacion <= 5):
                                print("Advertencia: Se omitió un registro histórico con calificaciones fuera de rango.")
                                continue
                        except ValueError:
                            print("Advertencia: Se omitió un registro histórico con formato numérico inválido.")
                            continue
                        
                        estadisticas[linea]["espera_total"] += espera
                        estadisticas[linea]["limpieza_total"] += limpieza
                        estadisticas[linea]["ocupacion_total"] += ocupacion
                        estadisticas[linea]["total_reseñas"] += 1
                        
                        if limpieza >= 4:
                            estadisticas[linea]["limpieza_altas"] += 1
                            
                        if espera == 1:
                            estadisticas[linea]["espera_1_estrella"] += 1
    except IOError:
        print("Error: No hay reseñas registradas para generar estadísticas.")
        return
        
    max_limpieza = 0
    for linea in estadisticas:
        if estadisticas[linea]["limpieza_altas"] > max_limpieza:
            max_limpieza = estadisticas[linea]["limpieza_altas"]

    lineas_mas_limpias = []
    if max_limpieza > 0:
        for linea in estadisticas:
            if estadisticas[linea]["limpieza_altas"] == max_limpieza:
                lineas_mas_limpias.append(linea)
        lineas_mas_limpias.sort()

    lineas_criticas_espera = []
    for linea in estadisticas:
        cant = estadisticas[linea]["total_reseñas"]
        if cant >= 5:
            porcentaje_unos = (estadisticas[linea]["espera_1_estrella"] / cant) * 100
            if porcentaje_unos > 75:
                lineas_criticas_espera.append((linea, porcentaje_unos))
                
    promedios_generales = []
    for linea in estadisticas:
        cant = estadisticas[linea]["total_reseñas"]
        if cant > 0:
            suma_total_estrellas = estadisticas[linea]["espera_total"] + estadisticas[linea]["limpieza_total"] + estadisticas[linea]["ocupacion_total"]
            prom_general = suma_total_estrellas / (cant * 3)
            promedios_generales.append((linea, prom_general))
            
    promedios_generales.sort(key=lambda x: x[1], reverse=True)
    top_3 = promedios_generales[:3]
    try:
        with open("reporte.txt", "w", encoding="utf-8") as archivo_reporte:
            titulo = "=== REPORTE DE ESTADISTICAS Y ANALISIS DE SUBTEXD ==="
            print(f"\n{titulo}")
            archivo_reporte.write(f"{titulo}\n\n")
            
            texto_limpieza = "-- 1. Lineas mas limpias (Mayor cantidad de valoraciones de 4 o 5 estrellas) --"
            print(f"\n{texto_limpieza}")
            archivo_reporte.write(texto_limpieza + "\n")
            
            if lineas_mas_limpias:
                for l in lineas_mas_limpias:
                    altas = estadisticas[l]["limpieza_altas"]
                    t_res = estadisticas[l]["total_reseñas"]
                    linea_txt = f"Linea {l}: {altas} valoracion(es) altas (sobre {t_res} reseñas totales)"
                    print(linea_txt)
                    archivo_reporte.write(linea_txt + "\n")
            else:
                msg_nl = "Aún no hay líneas con valoraciones altas de limpieza (4 o 5 estrellas)."
                print(msg_nl)
                archivo_reporte.write(msg_nl + "\n")
                
            texto_criticas = "\n-- 2. Lineas con valoracion critica de espera (>75% de 1 estrella, min. 5 reseñas) --"
            print(texto_criticas)
            archivo_reporte.write(texto_criticas + "\n")
            if lineas_criticas_espera:
                for l, porc in lineas_criticas_espera:
                    linea_txt = f"¡ALERTA! Linea {l}: {porc:.1f}% de calificaciones de 1 estrella en espera."
                    print(linea_txt)
                    archivo_reporte.write(linea_txt + "\n")
            else:
                msg_nc = "No hay líneas que cumplan con el criterio crítico de espera."
                print(msg_nc)
                archivo_reporte.write(msg_nc + "\n")
                
            texto_top3 = "\n-- 3. Top 3 de valoracion general --"
            print(texto_top3)
            archivo_reporte.write(texto_top3 + "\n")
            if top_3:
                for i, (l, prom) in enumerate(top_3, 1):
                    linea_txt = f"{i}. Linea {l} - Promedio General: {prom:.2f} estrellas"
                    print(linea_txt)
                    archivo_reporte.write(linea_txt + "\n")
            else:
                msg_nt = "No hay suficientes datos para calcular el ranking."
                print(msg_nt)
                archivo_reporte.write(msg_nt + "\n")
                
            print("\nEl reporte oficial ha sido exportado exitosamente a 'reporte.txt'.")
    except IOError:
        print("Error: No se pudo crear el archivo de reporte.")