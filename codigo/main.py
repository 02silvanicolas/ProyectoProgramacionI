import operaciones

def main():
    conjunto_lineas = set()

    try:
        archivo = open("configuracion.txt", "r")
    except IOError:
        print("Error: No se encontró el archivo 'configuracion.txt'.")
        return
    else:
        for linea in archivo:
            datos = linea.strip().split(",")
            for dato in datos:
                if dato.strip() != "":
                    conjunto_lineas.add(dato.strip().upper())
        archivo.close()

    if not conjunto_lineas:
        print("Error: El archivo 'configuracion.txt' está vacío o no contiene líneas válidas.")
        return

    usuario_actual = operaciones.Menu_Autenticacion()
    
    if not usuario_actual:
        print("Saliendo del programa...")
        return

    estado = 0

    while estado != "4":
        estado = operaciones.Ver_Menu()

        if estado == "1":
            operaciones.Gestionar_Resenas(usuario_actual, conjunto_lineas)
        elif estado == "2":
            # Para el paso 3 (Consultas)
            operaciones.Consultas(usuario_actual, conjunto_lineas)
        elif estado == "3":
            # Para el paso 4 (Estadísticas)
            operaciones.Estadisticas(usuario_actual, conjunto_lineas)
        elif estado == "4":
            print("Cerrando sesión y saliendo del programa...")
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()