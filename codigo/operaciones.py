def Ver_Menu():

    print("====Subtexd====")
    print("1. Gestionar usuarios")
    print("2. Gestion de Resenas")
    print("3. Consultas")
    print("4. Estadisticas")
    print("5. Salir")


    opcion = input("Ingrese una opcion: ")
    return opcion

def Gestionar_Usuarios(ListaUsuarios):
    print("====Gestion de usuarios====")
    print("1. Agregar usuario")
    print("2. Buscar usuario")

    input("Ingrese una opcion: ")
    match input:
        case "1": agregar_Usuario(ListaUsuarios, MatrizResenas, TuplaLineas)
        case "2": buscar_Usuario(ListaUsuarios) 

def Gestionar_Resenas(ListaUsuarios, MatrizResenas, TuplaLineas):
    print("====Gestion de resenas====")
    print("1. Cargar resena")
    print("2. Editar resena")
    #print("3. Consultar resena") Está en el alcance, pero coincide con la opción de Consultas, por lo que se omite para evitar confusión.

    input("Ingrese una opcion: ")
    match input:
        case "1": agregar_Resena(ListaUsuarios, MatrizResenas, TuplaLineas)
        case "2": editar_Resena(ListaUsuarios, MatrizResenas, TuplaLineas)
        #case "3": consultar_Resena(ListaUsuarios, MatrizResenas, TuplaLineas)

def Consultas(ListaUsuarios, MatrizResenas, TuplaLineas):
    print("====Consultas====")
    print("1. Consultar resenas por usuario")
    print("2. Consultar resenas por linea")
    print("3. Consultar resena de usuario para linea")

    input("Ingrese una opcion: ")
    match input:   
        case "1": consultar_Resenas_Usuario(ListaUsuarios, MatrizResenas, TuplaLineas)
        case "2": consultar_Resenas_Linea(TuplaLineas, MatrizResenas)
        case "3": consultar_Resena_UsuarioLinea(ListaUsuarios, MatrizResenas, TuplaLineas)

def Estadisticas(ListaUsuarios, MatrizResenas, TuplaLineas):
    print("====Estadisticas====")
    print("1. Mayor y menor satisfaccion")
    print("2. Usuario con mejor y peor experiencia")
    print("3. Lineas mas limpias")
    print("4. Linea mas reseniada")
    print("5. Lineas con valoracion critica de espera")
    print("6. Ranking por categoria")
    print("7. Top 3 rankings por categoria")

    input("Ingrese una opcion: ")
    match input:
        case "1": promedio_Satisfaccion(ListaUsuarios, MatrizResenas, TuplaLineas)
        case "2": promedio_ExperienciaUsuario(ListaUsuarios, MatrizResenas, TuplaLineas)
        case "3": lineas_Mas_Limpias(TuplaLineas, MatrizResenas)
        case "4": linea_Mas_Resenas(TuplaLineas, MatrizResenas)
        case "5": lineas_Valoracion_Critica(TuplaLineas, MatrizResenas)
        case "6": ranking_Por_Categoria(TuplaLineas, MatrizResenas)
        case "7": top3_Ranking_Por_Categoria(TuplaLineas, MatrizResenas)

def agregar_Usuario(listaUsuarios, matrizResenas, tuplaLineas):
    usuario = input("Ingrese el nombre de usuario deseado:")
    codigo = verificarCodigo(usuario, listaUsuarios)
    if codigo != -1:
        print("El usuario ya existe. No se puede agregar.")
    else:
        listaUsuarios.append(usuario)
        matrizResenas.append([[] for _ in range(len(tuplaLineas))])
        print("Usuario agregado exitosamente.")

def buscar_Usuario(listaUsuario):
    usuario = input("Ingrese el nombre de usuario que desea buscar:")
    codigo = verificarCodigo(usuario, listaUsuario)
    if codigo == -1:
        print("El usuario no existe.")
    else:
        print(f"El usuario {usuario} se encuentra en la lista.")

verificarCodigo = lambda buscado, lugar: lugar.index(buscado) if buscado in lugar else -1

def pedirDatos(pedirUsuario, pedirLinea, ListaUsuarios, TuplaLineas):

    devolucion = ()
    if pedirUsuario:
        usuario = input("Ingrese el nombre de usuario:")
        codigo_usuario = verificarCodigo(usuario, ListaUsuarios)
        while codigo_usuario == -1:
            print("El usuario no existe.")
            usuario = input("Ingrese el nombre de usuario:")
            codigo_usuario = verificarCodigo(usuario, ListaUsuarios)
        devolucion += (codigo_usuario,)
    if pedirLinea:
        linea = input("Ingrese el nombre de la linea:")
        codigo_linea = verificarCodigo(linea, TuplaLineas)
        while codigo_linea == -1:
            print("La linea no existe.")
            linea = input("Ingrese el nombre de la linea:")
            codigo_linea = verificarCodigo(linea, TuplaLineas)
        devolucion += (codigo_linea,)

    return devolucion



def agregar_Resena(ListaUsuarios, MatrizResenas, TuplaLineas):
    usuario, linea = pedirDatos(True, True, ListaUsuarios, TuplaLineas)
    resena = ingresar_Resena()
    agregar_Resena_Matriz(MatrizResenas, usuario, linea, resena)
    print("Resena agregada exitosamente.")

def editar_Resena(ListaUsuarios, MatrizResenas, TuplaLineas):
    usuario, linea = pedirDatos(True, True, ListaUsuarios, TuplaLineas)
    mostrar_Resena = MatrizResenas[usuario][linea]
    if mostrar_Resena == []:
        print("No hay resena para editar.")
        return
    else:
        print(f"Resena actual: {mostrar_Resena}")
        resena = ingresar_Resena()
        agregar_Resena_Matriz(MatrizResenas, usuario, linea, resena)
    # Aca deberia agregarse la logica para editar la resena en MatrizResenas
    print("Resena editada exitosamente.")


def ingresar_Resena():
    resena = []

    while validar_Rango == False:
        limpieza = int(input("Ingrese la calificacion de Limpieza (1-5): "))
        validar_Rango = 1 <= limpieza <= 5
        if not validar_Rango:
            print("La calificacion debe estar entre 1 y 5. Intente nuevamente.")

    while validar_Rango == False:
            espera = int(input("Ingrese la calificacion de Espera (1-5): "))
            validar_Rango = 1 <= espera <= 5
            if not validar_Rango:
                print("La calificacion debe estar entre 1 y 5. Intente nuevamente.")

    while validar_Rango == False:
                ocupacion = int(input("Ingrese la calificacion de Ocupacion (1-5): "))
                validar_Rango = 1 <= ocupacion <= 5
                if not validar_Rango:
                    print("La calificacion debe estar entre 1 y 5. Intente nuevamente.")

    comentario = input("Ingrese un comentario (opcional): ")
    comentario = comentario.upper()
    
    resena.append(limpieza)
    resena.append(espera)
    resena.append(ocupacion)
    resena.append(comentario)
    return resena

def agregar_Resena_Matriz(MatrizResenas, usuario, linea, resena):
    MatrizResenas[usuario][linea] = resena



def consultar_Resenas_Usuario(ListaUsuarios, MatrizResenas, TuplaLineas):
    usuario = pedirDatos(True, False, ListaUsuarios, TuplaLineas)
    # Aca deberia agregarse la logica para consultar las resenas del usuario en MatrizResenas

def consultar_Resenas_Linea(TuplaLineas, MatrizResenas):
    linea = pedirDatos(False, True, [], TuplaLineas)
    # Aca deberia agregarse la logica para consultar las resenas de la linea en MatrizResenas

def consultar_Resena_UsuarioLinea(ListaUsuarios, MatrizResenas, TuplaLineas):
    usuario, linea = pedirDatos(True, True, ListaUsuarios, TuplaLineas)
    # Aca deberia agregarse la logica para consultar la resena en MatrizResenas

def promedio_Satisfaccion(ListaUsuarios, MatrizResenas, TuplaLineas):
    # Aca deberia agregarse la logica para calcular el promedio de satisfaccion
    pass

def promedio_ExperienciaUsuario(ListaUsuarios, MatrizResenas, TuplaLineas):
    # Aca deberia agregarse la logica para calcular el promedio de experiencia del usuario
    pass

def lineas_Mas_Limpias(TuplaLineas, MatrizResenas):
    # Aca deberia agregarse la logica para calcular las lineas mas limpias
    pass

def linea_Mas_Resenas(TuplaLineas, MatrizResenas):
    # Aca deberia agregarse la logica para calcular la linea con mas resenas
    pass

def lineas_Valoracion_Critica(TuplaLineas, MatrizResenas):
    # Aca deberia agregarse la logica para calcular las lineas con valoracion critica
    pass

def ranking_Por_Categoria(TuplaLineas, MatrizResenas):
    # Aca deberia agregarse la logica para calcular el ranking por categoria
    pass

def top3_Ranking_Por_Categoria(TuplaLineas, MatrizResenas):
    # Aca deberia agregarse la logica para calcular el top 3 del ranking por categoria
    pass