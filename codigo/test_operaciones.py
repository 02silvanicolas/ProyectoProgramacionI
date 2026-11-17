import re
from operaciones import existe_Resena

def test_existe_Resena_positivo():
    resenas_memoria = {
        "A": {
            "martin": {"espera": "4", "limpieza": "5", "ocupacion": "3", "comentario": "BUEN SERVICIO"}
        }
    }
    assert existe_Resena("martin", "A", resenas_memoria) == True

def test_existe_Resena_negativo():
    resenas_memoria = {
        "A": {
            "martin": {"espera": "4", "limpieza": "5", "ocupacion": "3", "comentario": "BUEN SERVICIO"}
        }
    }
    assert existe_Resena("fabricio", "A", resenas_memoria) == False
    assert existe_Resena("martin", "B", resenas_memoria) == False

def test_regex_usuario_valido():
    patron_usuario = r"^[a-zA-Z0-9]+$"
    assert re.match(patron_usuario, "Martin123") is not None
    assert re.match(patron_usuario, "martin s") is None

def test_regex_contrasena_valida():
    patron_password = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z0-9]{6,}$"
    assert re.match(patron_password, "clave123") is not None
    assert re.match(patron_password, "abc1") is None
    assert re.match(patron_password, "sololetras") is None
    assert re.match(patron_password, "1234567") is None
    
def test_calculo_promedio_general_formula():
    espera_total = 8
    limpieza_total = 6
    ocupacion_total = 8
    cant = 2
    
    suma_total_estrellas = espera_total + limpieza_total + ocupacion_total
    prom_general = suma_total_estrellas / (cant * 3)
    
    # En lugar de round(), si querés verificar que el resultado sea aproximadamente 
    # el esperado sin lidiar con los decimales infinitos de punto flotante:
    assert 3.66 < prom_general < 3.68