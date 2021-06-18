from src.prototipo import contenidoColumna, columnas

tablero_ejemplo = [
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 1, 0, 0, 0],
        ]

def test_contenido_columna():
    assert [1,2,1,2,1,2] == contenidoColumna(3, tablero_ejemplo)

def test_columnas():
    assert [[0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [1,2,1,2,1,2],
            [0,0,0,0,0,1],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0]] == columnas(tablero_ejemplo)

def test_columnas_falso():
    assert [[0,1,1,1,0,0],
            [0,0,2,2,0,0],
            [1,1,2,2,1,2],
            [0,0,0,0,0,1],
            [0,0,2,1,1,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0]] != columnas(tablero_ejemplo)
