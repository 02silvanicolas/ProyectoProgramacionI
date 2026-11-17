import re
import operaciones

def main():
    conjunto_lineas = set()

    try:
        with open("configuracion.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                for dato in datos:
                    codigo = dato.strip().upper()
                    if codigo != "":
                        if re.fullmatch(r"[A-Z0-9]{1,10}", codigo):
                            conjunto_lineas.add(codigo)
                        else:
                            print(f"Advertencia: Se omitió una línea inválida en 'configuracion.txt': '{codigo}'.")
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'configuracion.txt'.")
        return
    except (IOError, UnicodeDecodeError):
        print("Error: No se pudo leer 'configuracion.txt' por un problema de acceso o codificación.")
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