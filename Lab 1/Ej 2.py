# Crear dos matrices solicitando los datos por consola (cantidad de filas y columnas), y los
# elementos de estas matrices deben ser aleatorios del 1 al 5, no se deben ingresar por
# consola. Luego se deben sumar en una función las matrices, y en otra función restarlas. En
# este caso no se puede utilizar numpy, solo estructuras propias de Python.


import numpy

print("Creación de matriz 1")
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

m = numpy.zeros((filas, columnas))
for i in range(filas):
    filas = []
    for j in range(columnas):
        columnas= []
        # intento de append a matriz con valores random
        m[i][j] = (filas.append((hash("semilla") % 6)), columnas.append((hash("semilla") % 6)))


print("\nCreación de matriz 2")
filas2 = int(input("Ingrese la cantidad de filas: "))
columnas2 = int(input("Ingrese la cantidad de columnas: "))

m2 = numpy.zeros((filas2, columnas2))
for i in range(filas2):
    filas2 = []
    for j in range(columnas2):
        m2[i][j] = int(input(f"Elemento ({i + 1}, {j + 1}): "))

if filas == filas2 and columnas == columnas2:
    print(f"Suma matrices:\n{m+m2}'")
    print(f"Resta matrices:\n{m-m2}'")
else: print("Las matrices no son iguales en medida")

