from src.prototipo import tableroVacio, detectarError, completarTableroEnOrden

secuencia = [1,2,3,4,1,1,2]

def test_tablero_vacio_tiene_6_filas():
    tablero = tableroVacio()
    assert len(tablero) == 6

def test_tablero_vacio_tiene_7_columnas():
    tablero = tableroVacio()
    assert len(tablero[0]) == 7

def test_secuencia_valida():
    assert detectarError(secuencia)

def test_error_detectado():
    assert detectarError([1,2,9,7,3,2]) == False

def test_completar_tablero_funciona():
    assert completarTableroEnOrden(secuencia, tableroVacio()) == [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0],
        [1, 2, 1, 2, 0, 0, 0],
    ]