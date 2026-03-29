# Alexis Mendoza Valencia
# Estudiante Tecnológico de Monterrey, campus guadalajara

# Metodo Lagrange

"""
El metodo es basicamente una intrerpolacion.
Lo que hacemos es calcular tantos valores, denotados l,
como podamos, segun el numero de puntos, y esto nos
dara por resultado el punto que buscamos. Evaluamos
siempre sobre un punto X del cual buscamos saber un
valor de Y.
Utiliza dos funciones:
    funcion de l's:
        Segun el numero de variables que tengamos
        disponibles sera el metodo.
        Para dos variables el metodo es:
        l = (x-x2) / (x1-x2)

    funcion final:
    Sumatoria de y1*l1 + y2*l2 + y3*l3 + ... + y4*l4

Ejemplo:
Los datos correspondientes  al censo de una población (en miles de habitantes) se recogen en la siguiente tabla:
Año               1950.0  1960.0  1970.0  1980.0 1990.0 2000.0
Número habitantes  123.5   131.2   150.7   141.3  203.2  240.5
a) Utilizar interpolación polinómica para estimar el número de habitantes en el año 1965.
b) Utilizar el método de Lagrange para estimar el número de habitantes en el año 1965.
"""

def l_lagrange(x, x1, x2):
    return (x-x2) / (x1-x2)


def lagrange(x_array, y_array, x):
    pos_X = 0
    for i in range(len(x_array)):
        if x_array[i] > x:
            pos_X = i
            break
    l1 = l_lagrange(x, x_array[pos_X-1], x_array[pos_X])
    l2 = l_lagrange(x, x_array[pos_X], x_array[pos_X-1])
    return l1*y_array[pos_X-1] + l2*y_array[pos_X]


x_array = [1950, 1960, 1970, 1980, 1990, 2000]
y_array = [123.5, 131.2, 150.7, 141.3, 203.2, 240.5]

print("Metodo Lagrange")
resultado = lagrange(x_array, y_array, 1965)
print("Resultado:", resultado)
