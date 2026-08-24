
def normalizarTitle(nombreIntegrantes):
    for i in range(len(nombreIntegrantes)):
        nombreIntegrantes[i] = nombreIntegrantes[i].title()
    return nombreIntegrantes



def convertirMayusculas(nombreEquipo):
    nombreEquipo = nombreEquipo.upper()
    return nombreEquipo
    


def cantidadCaracteres(nombreEquipo):
    cantidad = len(nombreEquipo)
    return cantidad

def generarSigla(nombreEquipo):
    palabras = nombreEquipo.split()
    sigla = ""
    for palabra in palabras:
        sigla += palabra[0].upper()
    return sigla

def verificarDigito(nombreEquipo):
    val = False
    for caracter in nombreEquipo:
        if caracter.isdigit():
            val = True
    return val
    

def mostrarDatos(nombreEquipo, comision, nombreIntegrantes, roles):
    print("\nDatos del equipo:")
    print(f"Nombre del equipo: {nombreEquipo}")
    print(f"Comisión del equipo: {comision}")
    print("Integrantes del equipo:")
    for i in range(len(nombreIntegrantes)):
        print(f"Nombre: {nombreIntegrantes[i]}, Rol: {roles[i]}")
