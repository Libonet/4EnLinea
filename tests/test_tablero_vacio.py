from src.prototipo import tableroVacio, detectarError

secuencia = [1,2,3,4,1,1,2]

def test_tablero_vacio_tiene_6_filas():
    tablero = tableroVacio()
    assert len(tablero) == 6

def test_tablero_vacio_tiene_7_columnas():
    tablero = tableroVacio()
    assert len(tablero[0]) == 7

def test_tablero_no_tiene_mas_de_7_columnas():
    tablero = tableroVacio()
    assert len(tablero[0]) <= 7 

def test_secuencia_valida():
    assert detectarError(secuencia)

def test_error_detectado():
    assert detectarError([1,2,9,7,3,2]) == False