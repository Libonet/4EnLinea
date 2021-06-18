from src.prototipo import contenidoFila, filas

tablero_ejemplo = [
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 1, 0, 0, 0],
        ]

def test_contenido_fila():
    assert [0,0,2,1,0,0,0] == contenidoFila(1, tablero_ejemplo)

def test_contenido_fila_falso():
    assert [0,0,2,1,0,0,0] != contenidoFila(3, tablero_ejemplo)

def test_filas():
    assert [
        [0, 0, 2, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        ] == filas(tablero_ejemplo)

def test_filas_falso():
    assert [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 2, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 0, 0],
        [0, 0, 2, 1, 1, 0, 0],
        ] != filas(tablero_ejemplo)