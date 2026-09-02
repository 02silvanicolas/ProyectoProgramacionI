
print("Primer programa del Proyecto Integrador/n")

print("Grupo Torneos El Producto. Alumnos: Nicolas Silva, Perez Lautaro, Martín Saffioti, Fabricio Pato")

import perfil_equipo

def main():
    nombreEquipo = input("Ingrese el nombre del equipo: ")
    comision = int(input("Ingrese la comisión del equipo: "))
    nombreIntegrantes = []
    roles = []
    cantidadIntegrantes = int(input("Ingrese la cantidad de integrantes del equipo: "))
    for i in range(cantidadIntegrantes):
        nombreIntegrante=input("Ingrese el nombre del integrante:")
        nombreIntegrantes.append(nombreIntegrante)
        rol=input("Ingrese el rol del integrante:")
        roles.append(rol)
    perfil_equipo.normalizarTitle(nombreIntegrantes)
    print("Nombres normalizados:")
    for i in range(len(nombreIntegrantes)):
        if nombreIntegrantes[i] == nombreIntegrantes[-1]:
            print(nombreIntegrantes[i])
        else:
            print(nombreIntegrantes[i], end=", ")
    perfil_equipo.convertirMayusculas(nombreEquipo)
    print("Nombre del equipo en mayúsculas:", nombreEquipo)
    cantidad=perfil_equipo.cantidadCaracteres(nombreEquipo)
    print("Cantidad de caracteres del nombre del equipo:", cantidad)
    sigla=perfil_equipo.generarSigla(nombreEquipo)
    print("Sigla del nombre del equipo:", sigla)
    tiene=perfil_equipo.verificarDigito(nombreEquipo)
    if tiene:
        print("El nombre del equipo contiene dígitos.")
    else:
        print("El nombre del equipo no contiene dígitos.")

    perfil_equipo.mostrarDatos(nombreEquipo, comision, nombreIntegrantes, roles)



if __name__ == "__main__":
    main()
