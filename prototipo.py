
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

def contenidoFila(nro_fila, tablero):
    fila = tablero[6-nro_fila]
    return fila

def columnas(tablero):
    tableroVacio = []
    for nro_columna in range(1,7):
        columna = contenidoColumna(nro_columna, tablero)
        tableroVacio.append(columna)
    return tableroVacio

def filas(tablero):
    tableroVacio = []
    for nro_fila in range(1,7):
        fila = contenidoFila(nro_fila, tablero)
        tableroVacio.append(fila)
    return tableroVacio


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

buscarColumna = 2
resultado = "\nEl contenido de la columna {} es {}"
print(resultado.format(buscarColumna, contenidoColumna(buscarColumna, tablero)))

buscarFila = 1
resultado = "\nEl contenido de la fila {} es {}"
print(resultado.format(buscarFila, contenidoFila(buscarFila, tablero)))

tableroColumnas = columnas(tablero)
print("\nEl contenido de las columnas es")
print(tableroColumnas)

tableroFilas = filas(tablero)
print("\El contenido de las filas es")
print(tableroFilas)