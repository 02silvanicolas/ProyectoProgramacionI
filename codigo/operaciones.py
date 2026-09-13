def Ver_Menu():

    print("====Subtexd====")
    print("1. Gestionar usuarios")
    print("2. Gestion de Resenas")
    print("3. Consultas")
    print("4. Estadisticas")
    print("5. Salir")


    opcion = input("Ingrese una opcion: ")
    return opcion

def Gestionar_Usuarios(ListaUsuarios, MatrizResenas, TuplaLineas):
    opcion=""
    while opcion!="0":
        print("====Gestion de usuarios====")
        print("1. Agregar usuario")
        print("2. Buscar usuario")
        print("0. Volver al menu")

        opcion=input("Ingrese una opcion: ")
        if opcion == "1":
            agregar_Usuario(ListaUsuarios, MatrizResenas, TuplaLineas)
        elif opcion == "2":
            buscar_Usuario(ListaUsuarios)   
        elif opcion=="0":
            print("Volviendo al menu")
        else:
            print("Opción no válida. Intente nuevamente.")

def Gestionar_Resenas(ListaUsuarios, MatrizResenas, TuplaLineas):
    opcion=""
    while opcion!="0":
        print("====Gestion de resenas====")
        print("1. Cargar resena")
        print("2. Editar resena")
        #print("3. Consultar resena") Está en el alcance, pero coincide con la opción de Consultas, por lo que se omite para evitar confusión.
        print("0. Volver al menu")

        opcion=input("Ingrese una opcion: ")
        if opcion == "1":
            agregar_Resena(ListaUsuarios, MatrizResenas, TuplaLineas)
        elif opcion == "2":
            editar_Resena(ListaUsuarios, MatrizResenas, TuplaLineas)
        elif opcion=="0":
            print("Volviendo al menu")
        #elif opcion=="3":
            #consultar_Resena(ListaUsuarios, MatrizResenas, TuplaLineas)
        else:
            print("Opción no válida. Intente nuevamente.")


def Consultas(ListaUsuarios, MatrizResenas, TuplaLineas):
    opcion=""
    while opcion!="0":
        print("====Consultas====")
        print("1. Consultar resenas por usuario")
        print("2. Consultar resenas por linea")
        print("3. Consultar resena de usuario para linea")
        print("0. Volver al menu")

        opcion=input("Ingrese una opcion: ")
        if opcion == "1":
            consultar_Resenas_Usuario(ListaUsuarios, MatrizResenas, TuplaLineas)
        elif opcion == "2":
            consultar_Resenas_Linea(TuplaLineas, MatrizResenas, ListaUsuarios)
        elif opcion == "3":
            consultar_Resena_UsuarioLinea(ListaUsuarios, MatrizResenas, TuplaLineas)
        elif opcion=="0":
            print("Volviendo al menu")
        else:
            print("Opción no válida. Intente de nuevo")

def Estadisticas(ListaUsuarios, MatrizResenas, TuplaLineas):
    opcion=""
    while opcion!="0":
        print("====Estadisticas====")
        print("1. Mayor y menor satisfaccion")
        print("2. Usuario con mejor y peor experiencia")
        print("3. Lineas mas limpias")
        print("4. Linea mas reseniada")
        print("5. Lineas con valoracion critica de espera")
        print("6. Ranking por categoria")
        print("7. Top 3 rankings por categoria")
        print("0. Volver al menú")

        opcion=input("Ingrese una opcion: ")
    
        if opcion == "1":
            promedio_Satisfaccion(ListaUsuarios, MatrizResenas, TuplaLineas)
        elif opcion == "2":
            promedio_ExperienciaUsuario(ListaUsuarios, MatrizResenas, TuplaLineas)
        elif opcion == "3":
            lineas_Mas_Limpias(TuplaLineas, MatrizResenas)
        elif opcion == "4":
            linea_Mas_Resenas(TuplaLineas, MatrizResenas)
        elif opcion == "5":
            lineas_Valoracion_Critica(TuplaLineas, MatrizResenas)
        elif opcion == "6":
            ranking_Por_Categoria(TuplaLineas, MatrizResenas)
        elif opcion == "7":
            top3_Ranking_Por_Categoria(TuplaLineas, MatrizResenas)
        elif opcion== "0":
            print("Volviendo al menú")
        else:
            print("Opción no válida. Intente nuevamente.")

def agregar_Usuario(listaUsuarios, matrizResenas, tuplaLineas):
    usuario = input("Ingrese el nombre de usuario deseado:")
    codigo = verificarCodigo(usuario, listaUsuarios)
    if codigo != -1:
        print("El usuario ya existe. No se puede agregar.")
    else:
        listaUsuarios.append(usuario.upper())
        matrizResenas.append([[] for _ in range(len(tuplaLineas))])
        print("Usuario agregado exitosamente.")

def buscar_Usuario(listaUsuario):
    usuario = input("Ingrese el nombre de usuario que desea buscar:")
    codigo = verificarCodigo(usuario, listaUsuario)
    if codigo == -1:
        print("El usuario no existe.")
    else:
        print(f"El usuario {usuario} se encuentra en la lista.")

verificarCodigo = lambda buscado, lugar: lugar.index(buscado.upper()) if (buscado.upper()) in lugar else -1

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
        print(f"Resena actual: limpieza: {mostrar_Resena[0]}, espera: {mostrar_Resena[1]}, ocupacion: {mostrar_Resena[2]}")
        resena = ingresar_Resena()
        agregar_Resena_Matriz(MatrizResenas, usuario, linea, resena)
    # Aca deberia agregarse la logica para editar la resena en MatrizResenas
    print("Resena editada exitosamente.")


def ingresar_Resena():
    resena = []
    validar_Rango = False

    while not validar_Rango:
        
        limpieza = int(input("Ingrese la calificacion de Limpieza (1-5): "))
        validar_Rango = 1 <= limpieza <= 5
        if not validar_Rango:
            print("La calificacion debe estar entre 1 y 5. Intente nuevamente.")

    validar_Rango = False
    while not validar_Rango:
            espera = int(input("Ingrese la calificacion de Espera (1-5): "))
            validar_Rango = 1 <= espera <= 5
            if not validar_Rango:
                print("La calificacion debe estar entre 1 y 5. Intente nuevamente.")

    validar_Rango = False
    while not validar_Rango:
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
    codigo_usuario = usuario[0]
    for i in range(len(MatrizResenas[codigo_usuario])):
        if MatrizResenas[codigo_usuario][i] != []:
            print(f"\nReseña de {ListaUsuarios[codigo_usuario]} para la línea {TuplaLineas[i]}:")
            print(f"  Limpieza: {MatrizResenas[codigo_usuario][i][0]}, Espera: {MatrizResenas[codigo_usuario][i][1]}, Ocupación: {MatrizResenas[codigo_usuario][i][2]}, Comentario: {MatrizResenas[codigo_usuario][i][3]}")
        else:
            print(f"No hay reseña de {ListaUsuarios[codigo_usuario]} para la línea {TuplaLineas[i]}.")
            

def consultar_Resenas_Linea(TuplaLineas, MatrizResenas, ListaUsuarios):
    linea = pedirDatos(False, True, [], TuplaLineas)
    linea = linea[0]
    print(f"Resenas para la linea {TuplaLineas[linea]}:")

    cantidad_resenas = 0

    for u in range(len(MatrizResenas)):
        
        if MatrizResenas[u][linea] != []:
            cantidad_resenas += 1
            print(f"\nReseña de {ListaUsuarios[u]} para la línea {TuplaLineas[linea]}:")
            print(f"  Limpieza: {MatrizResenas[u][linea][0]}, Espera: {MatrizResenas[u][linea][1]}, Ocupación: {MatrizResenas[u][linea][2]}, Comentario: {MatrizResenas[u][linea][3]}")

    if cantidad_resenas == 0:
                print(f"No hay reseñas para la línea {TuplaLineas[linea]}.")


def consultar_Resena_UsuarioLinea(ListaUsuarios, MatrizResenas, TuplaLineas):
    usuario, linea = pedirDatos(True, True, ListaUsuarios, TuplaLineas)
    resena = MatrizResenas[usuario][linea]
    if resena != []:
        print("Resena encontradas:")
        print(f"  Limpieza: {resena[0]}, Espera: {resena[1]}, Ocupacion: {resena[2]}, Comentario: {resena[3]}")
    else:
        print(f"No hay resena de {ListaUsuarios[usuario]} para la linea {TuplaLineas[linea]}.")


def promedio_Satisfaccion(ListaUsuarios, MatrizResenas, TuplaLineas):
    promedios = []
    for l in range(len(TuplaLineas)):
        suma = 0
        cantidad = 0
        for u in range(len(MatrizResenas)):
            resena = MatrizResenas[u][l]
            if resena != []:
                satisfaccion = (resena[0] + resena[1] + resena[2]) / 3
                suma += satisfaccion
                cantidad += 1
        promedios.append(suma / cantidad if cantidad > 0 else None)

    lineas_con_datos = [(TuplaLineas[i], promedios[i]) for i in range(len(promedios)) if promedios[i] is not None]

    if lineas_con_datos == []:
        print("No hay resenas cargadas para calcular la satisfaccion.")
        return

    linea_mayor = max(lineas_con_datos, key=lambda x: x[1])
    linea_menor = min(lineas_con_datos, key=lambda x: x[1])

    print(f"Linea con mayor satisfaccion: {linea_mayor[0]} (Promedio: {linea_mayor[1]:.2f})")
    print(f"Linea con menor satisfaccion: {linea_menor[0]} (Promedio: {linea_menor[1]:.2f})")


def promedio_ExperienciaUsuario(ListaUsuarios, MatrizResenas, TuplaLineas):
    promedios = []
    for u in range(len(ListaUsuarios)):
        suma = 0
        cantidad = 0
        for l in range(len(TuplaLineas)):
            resena = MatrizResenas[u][l]
            if resena != []:
                experiencia = (resena[0] + resena[1] + resena[2]) / 3
                suma += experiencia
                cantidad += 1
        promedios.append(suma / cantidad if cantidad > 0 else None)

    usuarios_con_datos = [(ListaUsuarios[i], promedios[i]) for i in range(len(promedios)) if promedios[i] is not None]

    if usuarios_con_datos == []:
        print("No hay resenas cargadas para calcular la experiencia de usuario.")
        return

    usuario_mejor = max(usuarios_con_datos, key=lambda x: x[1])
    usuario_peor = min(usuarios_con_datos, key=lambda x: x[1])

    print(f"Usuario con mejor experiencia: {usuario_mejor[0]} (Promedio: {usuario_mejor[1]:.2f})")
    print(f"Usuario con peor experiencia: {usuario_peor[0]} (Promedio: {usuario_peor[1]:.2f})")

def lineas_Mas_Limpias(TuplaLineas, MatrizResenas):
    promedios=[]

    for i in range(len(TuplaLineas)):
        suma=0
        cant=0
        for j in range(len(MatrizResenas)):
            resena=MatrizResenas[j][i]
            if resena!=None and resena[0]!=None:
                suma+=resena[0]
                cant+=1

        if cant>0:
            promedios.append(suma/cant)
        else:
            promedios.append(-1)

    maxPromedios=max(promedios)

    if maxPromedios==-1:
        print("No se registraron reseñas de limpieza")    

    else:
        print(f"--- Línea(s) más limpia(s) (Promedio: {maxPromedios:.2f}) ---")
        for j in range(len(TuplaLineas)):
            if promedios[j] == maxPromedios:
                print(f"- Línea {TuplaLineas[j]}")

def linea_Mas_Resenas(TuplaLineas, MatrizResenas):
    cantidades=[]
    for i in range(len(TuplaLineas)):
        cant=0

        for j in range(len(MatrizResenas)):
            if MatrizResenas[j][i]!=[None,None,None,None] and MatrizResenas[j][i]!=None:
                cant+=1
        cantidades.append(cant)

    maxCantidad=max(cantidades)

    if maxCantidad==0:
        print("No se registraron reseñas")
    else:
        print(f"--- Linea(s) con mas reseñas (Cantidad: {maxCantidad}) ---")
        for j in range(len(TuplaLineas)):
            if cantidades[j]==maxCantidad:
                print(f"- Linea {TuplaLineas[j]}")

def lineas_Valoracion_Critica(TuplaLineas, MatrizResenas):
    lineasCriticas=[]

    for i in range(len(TuplaLineas)):
        cant=0
        cant1=0

        for j in range(len(MatrizResenas)):
            resena=MatrizResenas[j][i]
            if resena!=None and resena[1]!=None:
                cant+=1
                if resena[1]==1:
                    cant1+=1
        if cant>=5:
            porcentaje=(cant1/cant)*100
            if porcentaje>75:
                lineasCriticas.append(TuplaLineas[i])

    if len(lineasCriticas)>0:
        print(f"Las lineas con valoraciones críticas en espera son:")
        for r in range(len(lineasCriticas)):
            print(lineasCriticas[r])
    else:
        print("No hay lineas con valoración critica en espera")


def ranking_Por_Categoria(TuplaLineas, MatrizResenas):
    cat=pedirCategoria()
    ranking=obtenerDatos(cat,TuplaLineas,MatrizResenas)

    if len(ranking)==0:
        print("No hay reseñas")
    else:
        print("---Ranking Completo---")
        for i in range(len(ranking)):
            print(f"{i+1}-Linea: {ranking[i][0]} Promedio: {ranking[i][1]:.2f} Cantidad de reseñas: {ranking[i][2]}")


def top3_Ranking_Por_Categoria(TuplaLineas, MatrizResenas):
    cat=pedirCategoria()
    ranking=obtenerDatos(cat,TuplaLineas,MatrizResenas)
    if len(ranking)<3:
        print("No hay suficientes reseñas para hacer un top 3")
    else:
        top=ranking[:3]
        print("---TOP 3---")
        for i in range(len(top)):
            print(f"{i+1}- Linea: {top[i][0]} Promedio: {top[i][1]:.2f} Cantidad de reseñas: {top[i][2]}")



def pedirCategoria():
    cat=input("Ingrese la categoria (0:Limpeiza, 1:Espera, 2:Ocupación 3:Promedio General):")
    while not cat.isdigit() or int(cat)<0 or int(cat)>3:
        print("Opcion no valida, debe ser un numero entre 0 y 3")
        cat=input("Ingrese la categoria (0:Limpeiza, 1:Espera, 2:Ocupación, 3:Promedio General):")
    return int(cat)


def obtenerDatos(cat,TuplaLineas,MatrizResenas):
    datos=[]

    for i in range(len(TuplaLineas)):
        if cat in(0, 1, 2):
            puntajes=[MatrizResenas[j][i][cat] for j in range(len(MatrizResenas)) if MatrizResenas[j][i]!=None and MatrizResenas[j][i][cat]!=None]
        else:
            puntajes = [
                (MatrizResenas[j][i][0] + MatrizResenas[j][i][1] + MatrizResenas[j][i][2]) / 3
                for j in range(len(MatrizResenas))
                if MatrizResenas[j][i] != None and None not in (MatrizResenas[j][i][0], MatrizResenas[j][i][1], MatrizResenas[j][i][2])
            ]

        cant=len(puntajes)

        if cant>0:
            promedio=sum(puntajes)/cant
            datos.append((TuplaLineas[i], promedio, cant))

    datos.sort(key=lambda x: (x[1], x[2]), reverse=True)

    return datos