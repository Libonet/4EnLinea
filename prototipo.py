
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

secuencia = [1, 2, 3, 1]
dibujarTablero(
    completarTableroEnOrden(
        secuencia, tableroVacio()
    )
)