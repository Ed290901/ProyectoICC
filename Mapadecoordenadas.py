def crear_cuadro(filas,columnas,cuadro):
    for i in range(filas):
        row = []
        for j in range(columnas):
            if j == 0 or i == 0 or i == filas - 1 or j == columnas - 1:
                row.append(".")
            else:
                row.append(" ")
        cuadro.append(row)
    return cuadro
def imprimir_cuadro(cuadro):
    for row in cuadro:
        for elementos in row:
            print(elementos,end=" ")
        print( )