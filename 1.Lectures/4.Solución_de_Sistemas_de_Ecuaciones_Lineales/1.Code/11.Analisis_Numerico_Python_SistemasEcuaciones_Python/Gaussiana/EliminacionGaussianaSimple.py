import numpy as np


class EliminacionGaussianaSimple:
    def __init__(self):
        self.xns = []
        self.Ab = [[]]
        self.n = 0
        self.etapas = []
        self.unica = True  # Este bool cuando es verdad podemos calcular la solucion, cuando es falsa, no se puede calcular nada

    def eliminacionGaussianaSimple(self, n, Ab):
        self.Ab = Ab
        self.n = n
        self.xns = [0.0] * n
        a = [[None for i in range(self.n)] for j in range(self.n)]
        for i in range(0, self.n):
            for j in range(0, self.n):
                a[i][j] = float(self.Ab[i][j])
        if(np.linalg.det(a) == 0):
            self.unica = False
            print("El sistema no tiene solución unica!")
            return
        print("Matriz Original")
        self.etapas.append(np.copy(self.Ab))
        self.imprimirMatriz()
        for k in range(1, n):
            print("Etapa " + str(k))
            if self.Ab[k - 1][k - 1] == 0:
                print("El sistema no tiene solución unica!")
                self.unica = False
                return
            print("Objetivo: Poner ceros debajo del elemento Ab" + str(k) + "," + str(k) + "= " + str(
                self.Ab[k - 1][k - 1]))
            print("Multiplicadores:")
            for i in range(k + 1, n + 1):
                multiplicador = self.Ab[i - 1][k - 1] / self.Ab[k - 1][k - 1]
                for j in range(k, n + 2):
                    self.Ab[i - 1][j - 1] = self.Ab[i - 1][j - 1] - multiplicador * self.Ab[k - 1][j - 1]
                print("Multiplicador" + str(i) + "," + str(k) + " : " + str(multiplicador))
            print(" ")
            self.etapas.append(np.copy(self.Ab))
            print("Etapa:  ", str(k))
            print(self.etapas[k - 1])
            print("")
            self.imprimirMatriz()
        print("Sustitución Regresiva")
        for i in range(n, 0, -1):
            sumatoria = 0
            for p in range(i + 1, n + 1):
                sumatoria = sumatoria + self.Ab[i - 1][p - 1] * self.xns[p - 1]
            temp = (self.Ab[i - 1][n] - sumatoria) / self.Ab[i - 1][i - 1]
            self.xns[i - 1] = temp
            print("X" + str(i) + " = " + str(self.xns[i - 1]))

    def getXns(self):
        return self.xns

    def getAb(self):
        return self.Ab

    def getEtapas(self):
        return self.etapas

    def imprimirMatriz(self):
        print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in self.Ab]))

    def imprimirMatrizEtapas(self):
        print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in self.etapas]))

    def reset(self):
        self.xns = []
        self.Ab = [[]]
        self.n = 0
        self.etapas = []

#gausi = EliminacionGaussianaSimple()
a = [1, -2, 0.5, -5]
b = [-2, 5, -1.5, 0]
c = [-0.2, 1.75, -1, 10]

e = [a, b, c]
gausi.eliminacionGaussianaSimple(3, e)

