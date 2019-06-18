import Rectangulo
import Mapadecoordenadas

cuadro = []
filas= 42
columnas= 82
mapa= Mapadecoordenadas.crear_cuadro(filas,columnas,cuadro)

altura=int(input("Número de filas: "))
base=int(input("Número de columnas: "))


Mapadecoordenadas.imprimir_cuadro(mapa)
Rectangulo.crear_rectangulo(altura, base)

