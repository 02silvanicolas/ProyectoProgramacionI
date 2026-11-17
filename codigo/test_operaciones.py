from operaciones import existe_Resena, validar_usuario, validar_contrasena

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
    assert validar_usuario("Martin123") == True
    assert validar_usuario("martin s") == False
    assert validar_usuario("martin_1") == False

def test_regex_contrasena_valida():
    assert validar_contrasena("clave123") == True
    assert validar_contrasena("abc1") == False
    assert validar_contrasena("sololetras") == False
    assert validar_contrasena("1234567") == False
    
def test_calculo_promedio_general_formula():
    espera_total = 8
    limpieza_total = 6
    ocupacion_total = 8
    cant = 2
    
    suma_total_estrellas = espera_total + limpieza_total + ocupacion_total
    prom_general = suma_total_estrellas / (cant * 3)
    
    assert 3.66 < prom_general < 3.68