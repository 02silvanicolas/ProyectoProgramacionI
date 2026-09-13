import operaciones
import datos

def main():

    estado = 0

    while estado != "5":

        estado = operaciones.Ver_Menu()

        if estado == "1":
            operaciones.Gestionar_Usuarios(datos.usuarios, datos.resenas, datos.lineas)
        elif estado == "2":
            operaciones.Gestionar_Resenas(datos.usuarios, datos.resenas, datos.lineas)
        elif estado == "3":
            operaciones.Consultas(datos.usuarios, datos.resenas, datos.lineas)
        elif estado == "4":
            operaciones.Estadisticas(datos.usuarios, datos.resenas, datos.lineas)
        elif estado == "5":
            print("Saliendo del programa...")
        else:
            print("Opción inválida. Intente nuevamente.")



if __name__ == "__main__":
    main()
