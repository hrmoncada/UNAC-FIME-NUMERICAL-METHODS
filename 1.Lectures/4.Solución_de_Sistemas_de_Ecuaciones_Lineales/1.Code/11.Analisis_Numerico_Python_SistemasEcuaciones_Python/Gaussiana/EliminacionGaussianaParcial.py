import numpy as np


class EliminacionGaussianaParcial:
    def __init__(self):
        self.xns = []
        self.Ab = [[]]
        self.n = 0
        self.unica = True  # Este bool cuando es verdad podemos calcular la solucion, cuando es falsa, no se puede calcular nada
        self.etapas = []

    def eliminacionGaussianaParcial(self, n, Ab):
        self.Ab = Ab
        self.n = n
        self.xns = [0.0] * n
        a = [[None for i in range(self.n)] for j in range(self.n)]
        for i in range(0, self.n):
            for j in range(0, self.n):
                a[i][j] = float(self.Ab[i][j])
        if (np.linalg.det(a) == 0):
            self.unica = False
            print("El sistema no tiene solución unica!")
            return
        print("Matriz Original")
        self.etapas.append(np.copy(self.Ab))
        self.imprimirMatriz()
        for k in range(1, n):
            print("Etapa " + str(k))
            print("Objetivo: Poner ceros debajo del elemento A" + str(k) + "," + str(k) + "= " + str(
                self.Ab[k - 1][k - 1]))
            print("Multiplicadores:")
            self.pivoteoParcial(k)
            if self.unica == False:
                return
            for i in range(k + 1, n + 1):
                multiplicador = self.Ab[i - 1][k - 1] / self.Ab[k - 1][k - 1]
                for j in range(k, n + 2):
                    self.Ab[i - 1][j - 1] = self.Ab[i - 1][j - 1] - multiplicador * self.Ab[k - 1][j - 1]
                print("Multiplicador" + str(i) + "," + str(k) + " : " + str(multiplicador))
            print(" ")
            print(k - 1)
            self.etapas.append(np.copy(self.Ab))
            self.imprimirMatriz()
        print("Sustitución Regresiva")
        for i in range(n, 0, -1):
            sumatoria = 0
            for p in range(i + 1, n + 1):
                sumatoria = sumatoria + self.Ab[i - 1][p - 1] * self.xns[p - 1]
            temp = (self.Ab[i - 1][n] - sumatoria) / self.Ab[i - 1][i - 1]
            print("ESTA ES I: ", i)
            self.xns[i - 1] = temp
            print("X" + str(i) + " = " + str(self.xns[i - 1]))

    def pivoteoParcial(self, k):
        elementoMax = abs(self.Ab[k - 1][k - 1])
        filaMax = k - 1
        for i in range(k - 1, self.n):
            temp = abs(self.Ab[i][k - 1])
            if temp > elementoMax:
                elementoMax = temp
                filaMax = i
        print("Elemento mayor: ", str(elementoMax), " en la fila: ", str(filaMax + 1))
        if elementoMax == 0:
            print("El sistema no tiene solución unica!")
            self.unica = False
            return
        elif filaMax != k - 1:
            print("Cambio de fila: ", k, " con fila: ", str(filaMax + 1))
            for i in range(0, len(self.Ab[0])):
                temp = self.Ab[k - 1][i]
                self.Ab[k - 1][i] = self.Ab[filaMax][i]
                self.Ab[filaMax][i] = temp
            self.imprimirMatriz()

    def imprimirMatriz(self):
        print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in self.Ab]))

    def getXns(self):
        return self.xns

    def getAb(self):
        return self.Ab

    def getEtapas(self):
        return self.etapas

    def imprimirMatrizEtapas(self):
        for i in self.etapas:
            print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in i]))

    def reset(self):
        self.xns = []
        self.Ab = [[]]
        self.n = 0


#gausi = EliminacionGaussianaParcial()
a = [1, -2, 0.5, -5]
b = [-2, 5, -1.5, 0]
c = [-0.2, 1.75, -1, 10]

e = [a, b, c]
#gausi.eliminacionGaussianaParcial(3, e)
