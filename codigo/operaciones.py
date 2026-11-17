import re

def validar_usuario(usuario):
    if not isinstance(usuario, str):
        return False
    return re.fullmatch(r"[a-zA-Z0-9]{3,20}", usuario) is not None

def validar_contrasena(password):
    if not isinstance(password, str):
        return False
    return re.fullmatch(r"(?=.*[A-Za-z])(?=.*\d)[A-Za-z0-9]{6,20}", password) is not None

def leer_usuarios_CSV():
    usuarios = {}
    archivo_existe = True
    archivo_vacio = True
    termina_en_salto = True

    try:
        with open("usuarios.csv", "r", encoding="utf-8") as archivo:
            for num_linea, linea in enumerate(archivo, 1):
                if linea.strip() == "":
                    continue
                archivo_vacio = False
                termina_en_salto = linea.endswith("\n")
                datos = linea.strip().split(",")
                if len(datos) != 2:
                    print(f"Advertencia: Fila {num_linea} malformada en 'usuarios.csv' omitida.")
                    continue
                usr = datos[0].strip()
                pwd = datos[1].strip()
                if not validar_usuario(usr) or not validar_contrasena(pwd):
                    print(f"Advertencia: Credenciales históricas inválidas en fila {num_linea} de 'usuarios.csv' omitidas.")
                    continue
                usuarios[usr.lower()] = (usr, pwd)
    except FileNotFoundError:
        archivo_existe = False
    except (IOError, UnicodeDecodeError):
        print("Error: No se pudo leer 'usuarios.csv' (problema de permisos o codificación).")
        return None, False, True, True

    return usuarios, archivo_existe, archivo_vacio, termina_en_salto


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
    if not validar_usuario(usuario):
        print("Error: Formato de usuario inválido (3 a 20 caracteres, solo letras y números, sin espacios).")
        return None

    password = input("Ingrese su contraseña: ")
    if not validar_contrasena(password):
        print("Error: Formato de contraseña inválido (6 a 20 caracteres, con letras y números).")
        return None

    usuarios, archivo_existe, _, _ = leer_usuarios_CSV()
    if usuarios is None:
        return None
    if not archivo_existe:
        print("Error: Aún no hay usuarios registrados en el sistema.")
        return None

    clave = usuario.lower()
    if clave in usuarios and usuarios[clave][1] == password:
        usuario_registrado = usuarios[clave][0]
        print(f"\n¡Bienvenido/a al sistema, {usuario_registrado}!")
        return usuario_registrado

    print("Error: Usuario o contraseña incorrectos.")
    return None

def Registrar_Usuario():
    usuarios, archivo_existe, archivo_vacio, termina_en_salto = leer_usuarios_CSV()
    if usuarios is None:
        print("No se puede registrar un usuario mientras 'usuarios.csv' no sea legible.")
        return

    usuario_valido = False
    while not usuario_valido:
        usuario = input("Ingrese nuevo usuario (3 a 20 caracteres, solo letras y números, sin espacios): ")
        if not validar_usuario(usuario):
            print("Error: El usuario debe tener entre 3 y 20 caracteres alfanuméricos, sin espacios.")
            continue

        if usuario.lower() in usuarios:
            print("Error: El usuario ya se encuentra registrado.")
        else:
            usuario_valido = True

    password_valida = False
    while not password_valida:
        password = input("Ingrese contraseña (6 a 20 caracteres, con letras y números): ")
        if validar_contrasena(password):
            password_valida = True
        else:
            print("Error: La contraseña debe tener entre 6 y 20 caracteres e incluir letras y números (sin símbolos ni espacios).")

    try:
        modo = "a" if archivo_existe else "w"
        with open("usuarios.csv", modo, encoding="utf-8") as archivo:
            if archivo_existe and not archivo_vacio and not termina_en_salto:
                archivo.write("\n")
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
            consultar_Resenas_Usuario_CSV(usuario_actual, conjunto_lineas)
        elif opcion == "2":
            consultar_Resenas_Linea_CSV(conjunto_lineas)
        elif opcion == "0":
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida. Intente de nuevo.")

def pedirLinea(TuplaLineas):
    linea = input("Ingrese el nombre de la línea: ").strip().upper()
    while linea not in TuplaLineas:
        print("La línea no existe o no es válida.")
        linea = input("Ingrese el nombre de la línea nuevamente: ").strip().upper()
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

def cargar_resenas_CSV(conjunto_lineas):
    resenas = {}
    archivo_existe = True
    archivo_vacio = True
    termina_en_salto = True

    try:
        with open("registros.csv", "r", encoding="utf-8") as archivo:
            for num_linea, fila in enumerate(archivo, 1):
                if fila.strip() == "":
                    continue
                archivo_vacio = False
                termina_en_salto = fila.endswith("\n")
                datos = fila.strip().split(",")

                if datos[0].strip().lower() == "usuario" and datos[1].strip().lower() == "linea":
                    continue

                if len(datos) < 6:
                    print(f"Advertencia: Registro histórico incompleto en fila {num_linea} omitido.")
                    continue

                usr = datos[0].strip()
                lin = datos[1].strip().upper()

                if not validar_usuario(usr) or lin not in conjunto_lineas:
                    print(f"Advertencia: Registro histórico con usuario o línea inválida en fila {num_linea} omitido.")
                    continue

                try:
                    esp = int(datos[2].strip())
                    lim = int(datos[3].strip())
                    ocu = int(datos[4].strip())
                    if not (1 <= esp <= 5 and 1 <= lim <= 5 and 1 <= ocu <= 5):
                        print(f"Advertencia: Calificaciones fuera de rango en fila {num_linea} omitidas.")
                        continue
                except ValueError:
                    print(f"Advertencia: Formato numérico inválido en fila {num_linea} omitido.")
                    continue

                comentario = ";".join(c.strip() for c in datos[5:])
                if lin not in resenas:
                    resenas[lin] = {}
                resenas[lin][usr.lower()] = {
                    "usuario": usr,
                    "espera": esp,
                    "limpieza": lim,
                    "ocupacion": ocu,
                    "comentario": comentario
                }
    except FileNotFoundError:
        archivo_existe = False
    except (IOError, UnicodeDecodeError):
        print("Error: No se pudo leer 'registros.csv' (problema de permisos o codificación).")
        return None, False, True, True

    return resenas, archivo_existe, archivo_vacio, termina_en_salto

def agregar_Resena_CSV(usuario_actual, conjunto_lineas):
    linea = pedirLinea(conjunto_lineas)
    resenas, archivo_existe, archivo_vacio, termina_en_salto = cargar_resenas_CSV(conjunto_lineas)

    if resenas is None:
        print("Operación cancelada para evitar pérdida de datos en 'registros.csv'.")
        return

    if existe_Resena(usuario_actual, linea, resenas):
        print(f"Error: Ya has realizado una reseña para la línea {linea}. Utiliza la opción de editar.")
        return

    print(f"\n--- Nueva reseña para la línea {linea} ---")
    nueva_resena = ingresar_Resena()

    try:
        modo = "a" if (archivo_existe and not archivo_vacio) else "w"
        with open("registros.csv", modo, encoding="utf-8") as archivo:
            if modo == "w":
                archivo.write("usuario,linea,espera,limpieza,ocupacion,comentario\n")
            elif not termina_en_salto:
                archivo.write("\n")
            archivo.write(
                f"{usuario_actual},{linea},{nueva_resena['espera']},"
                f"{nueva_resena['limpieza']},{nueva_resena['ocupacion']},{nueva_resena['comentario']}\n"
            )
        print("Reseña guardada exitosamente.")
    except IOError:
        print("Error: No se pudo guardar la reseña en el archivo de registros.")

def editar_Resena_CSV(usuario_actual, conjunto_lineas):
    linea = pedirLinea(conjunto_lineas)
    resenas, archivo_existe, _, _ = cargar_resenas_CSV(conjunto_lineas)

    if resenas is None or not archivo_existe:
        print("Error: No se pudo acceder a 'registros.csv' o aún no existen reseñas para editar.")
        return

    if not existe_Resena(usuario_actual, linea, resenas):
        print(f"Error: No tienes ninguna reseña registrada para la línea {linea}.")
        return

    clave_usr = usuario_actual.lower()
    actual = resenas[linea][clave_usr]
    print(f"\nReseña actual - Espera: {actual['espera']}, Limpieza: {actual['limpieza']}, Ocupación: {actual['ocupacion']}, Comentario: {actual['comentario']}")
    print("--- Ingresa los nuevos valores ---")

    nueva_resena = ingresar_Resena()

    resenas[linea][clave_usr] = {
        "usuario": actual["usuario"],
        "espera": nueva_resena["espera"],
        "limpieza": nueva_resena["limpieza"],
        "ocupacion": nueva_resena["ocupacion"],
        "comentario": nueva_resena["comentario"]
    }

    lineas_salida = ["usuario,linea,espera,limpieza,ocupacion,comentario\n"]
    for lin in resenas:
        for usr_key in resenas[lin]:
            reg = resenas[lin][usr_key]
            lineas_salida.append(
                f"{reg['usuario']},{lin},{reg['espera']},{reg['limpieza']},{reg['ocupacion']},{reg['comentario']}\n"
            )

    try:
        with open("registros.csv", "w", encoding="utf-8") as archivo:
            for fila_salida in lineas_salida:
                archivo.write(fila_salida)
        print("Reseña editada y archivo actualizado exitosamente.")
    except IOError:
        print("Error: No se pudo actualizar el archivo de registros.")

def consultar_Resenas_Usuario_CSV(usuario_actual, conjunto_lineas):
    print(f"\n--- Reseñas de {usuario_actual} ---")
    resenas, archivo_existe, _, _ = cargar_resenas_CSV(conjunto_lineas)
    if resenas is None or not archivo_existe:
        print("Aún no hay reseñas válidas registradas en el sistema.")
        return

    encontradas = False
    clave_usr = usuario_actual.lower()
    for lin in sorted(resenas):
        if clave_usr in resenas[lin]:
            reg = resenas[lin][clave_usr]
            print(f"Línea {lin} -> Limpieza: {reg['limpieza']}, Espera: {reg['espera']}, Ocupación: {reg['ocupacion']}, Comentario: {reg['comentario']}")
            encontradas = True

    if not encontradas:
        print("No has realizado ninguna reseña todavía.")

def consultar_Resenas_Linea_CSV(conjunto_lineas):
    linea = pedirLinea(conjunto_lineas)
    print(f"\n--- Reseñas para la Línea {linea} ---")
    resenas, archivo_existe, _, _ = cargar_resenas_CSV(conjunto_lineas)
    if resenas is None or not archivo_existe:
        print("Aún no hay reseñas válidas registradas en el sistema.")
        return

    if linea not in resenas or not resenas[linea]:
        print(f"No hay reseñas para la línea {linea}.")
        return

    for reg in resenas[linea].values():
        print(f"Usuario {reg['usuario']} -> Limpieza: {reg['limpieza']}, Espera: {reg['espera']}, Ocupación: {reg['ocupacion']}, Comentario: {reg['comentario']}")

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
        
    resenas, archivo_existe, _, _ = cargar_resenas_CSV(conjunto_lineas)
    if not resenas:
        print("Error: No hay reseñas válidas registradas para generar estadísticas.")
        return

    for linea in resenas:
        for reg in resenas[linea].values():
            espera = reg["espera"]
            limpieza = reg["limpieza"]
            ocupacion = reg["ocupacion"]

            estadisticas[linea]["espera_total"] += espera
            estadisticas[linea]["limpieza_total"] += limpieza
            estadisticas[linea]["ocupacion_total"] += ocupacion
            estadisticas[linea]["total_reseñas"] += 1

            if limpieza >= 4:
                estadisticas[linea]["limpieza_altas"] += 1
            if espera == 1:
                estadisticas[linea]["espera_1_estrella"] += 1
        
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