
def tableroVacio():
    return [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

def contenidoColumna(nro_columna, tablero):
    columna = []
    for fila in tablero:
        celda = fila[nro_columna - 1]
        columna.append(celda)
    return columna

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
    for columna in secuencia:
        if columna > 7 or columna < 1:
            return False
    return True

secuencia = [1, 2, 3, 1]

tablero = []
if detectarError(secuencia):
    tablero = completarTableroEnOrden(secuencia, tableroVacio())
    dibujarTablero(tablero)
else:
    print("la secuencia fue ingresada erroneamente...")

resultado = "El contenido de la columna es {}"
print(resultado.format(contenidoColumna(2, tablero)))