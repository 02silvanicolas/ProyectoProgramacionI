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
    print("3. Consultar resena")

    input("Ingrese una opcion: ")
    match input:
        case "1": agregar_Resena(ListaUsuarios, MatrizResenas, TuplaLineas)
        case "2": editar_Resena(ListaUsuarios, MatrizResenas, TuplaLineas)
        case "3": consultar_Resena(ListaUsuarios, MatrizResenas, TuplaLineas)

def Consultas(ListaUsuarios, MatrizResenas, TuplaLineas):
    print("====Consultas====")
    print("1. Consultar resenas por usuario")
    print("2. Consultar resenas por linea")
    print("3. Consultar resena de usuario para linea")

    input("Ingrese una opcion: ")
    match input:   
        case "1": consultar_Resenas_Usuario(ListaUsuarios, MatrizResenas)
        case "2": consultar_Resenas_Linea(TuplaLineas, MatrizResenas)
        case "3": consultar_Resena_Usuario_Linea(ListaUsuarios, TuplaLineas, MatrizResenas)

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
        case "1": promedio_Satisfaccion(ListaUsuarios, MatrizResenas)
        case "2": promedio_ExperienciaUsuario(ListaUsuarios, MatrizResenas)
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
    resena = input("Ingrese la resena:")
    # Aca deberia agregarse la logica para agregar la resena a MatrizResenas
    print("Resena agregada exitosamente.")

def editar_Resena(ListaUsuarios, MatrizResenas, TuplaLineas):
    usuario, linea = pedirDatos(True, True, ListaUsuarios, TuplaLineas)
    # Aca deberia agregarse la logica para editar la resena en MatrizResenas
    print("Resena editada exitosamente.")

def consultar_Resena(ListaUsuarios, MatrizResenas, TuplaLineas):
    usuario, linea = pedirDatos(True, True, ListaUsuarios, TuplaLineas)
    # Aca deberia agregarse la logica para consultar la resena en MatrizResenas

