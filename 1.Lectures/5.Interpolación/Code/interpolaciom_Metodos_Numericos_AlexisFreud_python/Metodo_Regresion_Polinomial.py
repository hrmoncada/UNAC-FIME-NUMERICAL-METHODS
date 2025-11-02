# Alexis Mendoza Valencia
# Estudiante Tecnológico de Monterrey, campus guadalajara

# Metodo Regresion polinomial

"""
Este método lo que busca es encontrar una linea que modele
con cierto error todos los valores posibles en una grafica.
El método funcionara aun cuando los valores tiendan a
infinito, pero siempre tendra cierto error.

Para el correcto uso de este metodo, es importante contar
con las librerias matplotlib y numpy.

Si no los tienes, te recomiendo utilizar una pagina
llamada cocalc. Abre un cuaderno de Jupyter Notebook
y el codigo funcionara a la perfeccion.


"""

import matplotlib.pyplot as plt
import numpy as np


def createMatrix(m,n,v):
    C = []
    for i in range(m):
        C.append([v]*n)
    return C


def getDimensions(A):
    return (len(A),len(A[0]))


def copyMatrix(B):
    m,n = getDimensions(B)
    A = createMatrix(m,n,0)
    for i in range(m):
        for j in range(n):
            A[i][j] = B[i][j]
    return A


def sumaMatrix(A,B):
    Am,An = getDimensions(A)
    Bm,Bn = getDimensions(B)
    if Am != Bm or An != Bn:
        print("Error las dimensiones deben ser iguales")
        return []
    C = createMatrix(Am,An,0)
    for i in range(Am):
        for j in range(An):
            C[i][j] = A[i][j] + B[i][j]
    return C


def restaMatrix(A,B):
    Am,An = getDimensions(A)
    Bm,Bn = getDimensions(B)
    if Am != Bm or An != Bn:
        print("Error las dimensiones deben ser iguales")
        return []
    C = createMatrix(Am,An,0)
    for i in range(Am):
        for j in range(An):
            C[i][j] = A[i][j] - B[i][j]
    return C


def multMatrix(A,B):
    Am,An = getDimensions(A)
    Bm,Bn = getDimensions(B)
    if An != Bm:
        print("Error las dimensiones deben ser conformable")
        return []
    C = createMatrix(Am,Bn,0)
    for i in range(Am):
        for j in range(Bn):
            for k in range(An):
                    C[i][j] += A[i][k] * B[k][j]
    return C


def getAdyacente(A,r,c):
    Am,An = getDimensions(A)
    C = createMatrix(Am-1,An-1,0)
    for i in range(Am):
        if i == r:
            continue
        for j in range(An):
            if j == c:
                continue
            ci = 0
            cj = 0
            if(i < r):
                ci = i
            else:
                ci = i - 1
            if(j < c):
                cj = j
            else:
                cj = j - 1
            C[ci][cj] = A[i][j]
    return C


def detMatrix(A):
    m,n = getDimensions(A)
    if m != n:
        print("La matriz no es cuadrada")
        return []
    if m == 1:
        return A[0][0]
    if m == 2:
        return A[0][0]*A[1][1] - A[1][0]*A[0][1]
    det = 0
    for j in range(m):
        det += ((-1)**j)*A[0][j]*detMatrix(getAdyacente(A,0,j))
    return det


def getMatrizTranspuesta(A):
    m,n = getDimensions(A)
    C = createMatrix(n,m,0)
    for i in range(m):
        for j in range(n):
            C[j][i] = A[i][j]
    return C


def getMatrizAdjunta(A):
    m,n = getDimensions(A)
    if m != n:
        print("La matriz no es cuadrada")
        return []
    C = createMatrix(m,n,0)
    for i in range(m):
        for j in range(n):
            C[i][j] = ((-1)**(i+j))*detMatrix(getAdyacente(A,i,j))
    return C


def getMatrizInversa(A):
    m,n = getDimensions(A)
    if m != n:
        print("La matriz no es cuadrada")
        return []
    detA = detMatrix(A)
    if detA == 0:
        print("La matriz no tiene inversa")
        return []
    At = getMatrizTranspuesta(A)
    adjA = getMatrizAdjunta(At)
    invDetA = 1/detA
    C = createMatrix(m,n,0)
    for i in range(m):
        for j in range(n):
            C[i][j] = invDetA * adjA[i][j]
    return C


x = [  0,  1,   2,   3,   4,   5]
y = [2.1,7.7,13.6,27.2,40.9,61.1]
plt.plot(x,y,'rx')


def regPolinominal(grado,x,y):
    grado += 1
    A = createMatrix(grado,grado,0)
    for i in range(grado):
        for j in range(grado):
            A[i][j] = sum ( xi ** (i+j) for xi in x)
    C = createMatrix(grado,1,0)
    for i in range(grado):
        C[i][0] = sum ((xi**(i))*yi  for xi,yi in zip(x,y))
    invA = getMatrizInversa(A)
    return multMatrix(invA, C)


def evalPolinomio(coef,x):
    y = []
    coef = np.asarray(coef)
    for i in range(len(x)):
        y.append(0)
        for c in range(len(coef)):
            y[i] += (x[i]**c) * coef[c]
    return y


coef = regPolinominal(2,x,y)
print("coeficientes",coef)
x2 = np.linspace(0, 5, 100)
y2 = evalPolinomio(coef,x2)
plt.plot(x2,y2)
plt.show()
