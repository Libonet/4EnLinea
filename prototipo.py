
def tableroVacio():
    return [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

def soltarFichaEnColumna(ficha, columna, tablero):
    for fila in range(6, 0, -1):
        if tablero[fila-1][columna-1] == 0:
            tablero[fila-1][columna-1] = ficha
            return

def completarTableroEnOrden(secuencia, tablero):
    ficha = 1
    for columna in secuencia:
        soltarFichaEnColumna(ficha, columna, tablero)
        if ficha == 1:
            ficha = 2
        else:
            ficha = 1
    return tablero

def dibujarTablero(tablero):
    for i in tablero:
        print(i)

def detectarError(secuencia):
    for x in secuencia:
        if x > 7 or x < 1:
            return -1
    else:
        return 0

secuencia = [1, 2, 3, 1]

error = detectarError(secuencia)
if error == 0:
    dibujarTablero(
        completarTableroEnOrden(
            secuencia, tableroVacio()
        )
    )
else:
    print("la secuencia fue ingresada erroneamente...")