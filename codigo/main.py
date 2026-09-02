import operaciones
import datos

def main():

    estado = 0

    while estado != "5":

        estado = operaciones.Ver_Menu()

        match estado:
            case "1":
                operaciones.Gestionar_Usuarios(datos.usuarios)
            case "2":
                operaciones.Gestionar_Resenas(datos.usuarios, datos.resenas, datos.lineas)
            case "3":
                operaciones.Consultas(datos.usuarios, datos.resenas, datos.lineas)
            case "4":
                operaciones.Estadisticas(datos.usuarios, datos.resenas, datos.lineas)
            case "5":
                print("Saliendo del programa...")
            case _:
                print("Opcion invalida. Intente nuevamente.")



if __name__ == "__main__":
    main()
