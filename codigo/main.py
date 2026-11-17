import operaciones

def main():
    conjunto_lineas = set()

    try:
        with open("configuracion.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                for dato in datos:
                    if dato.strip() != "":
                        conjunto_lineas.add(dato.strip().upper())
    except IOError:
        print("Error: No se encontró el archivo 'configuracion.txt'.")
        return

    if not conjunto_lineas:
        print("Error: El archivo 'configuracion.txt' está vacío o no contiene líneas válidas.")
        return

    usuario_actual = operaciones.Menu_Autenticacion()
    
    if not usuario_actual:
        print("Saliendo del programa...")
        return

    estado = "0"

    while estado != "4":
        estado = operaciones.Ver_Menu()

        if estado == "1":
            operaciones.Gestionar_Resenas(usuario_actual, conjunto_lineas)
        elif estado == "2":
            operaciones.Consultas(usuario_actual, conjunto_lineas)
        elif estado == "3":
            operaciones.Estadisticas(conjunto_lineas)
        elif estado == "4":
            print("Cerrando sesión y saliendo de Subtexd...")
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()