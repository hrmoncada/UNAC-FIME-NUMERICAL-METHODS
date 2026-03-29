import math

import numpy as np


class FactorizacionLUCholesky:
    def __init__(self):
        self.xns = []
        self.A = [[]]
        self.b = []
        self.L = [[]]
        self.U = [[]]
        self.n = 0
        self.etapasL = []
        self.etapasU = []
        self.z = []
        self.unica = True

    def factorizacionLUCholesky(self, A, b, n):
        if (any(elem < 0 for elem in np.diag(A))) | (np.linalg.det(A) == 0):
            self.unica = False
            return

        self.L = [[None] * n for i in range(n)]
        self.U = [[None] * n for i in range(n)]
        self.A = A
        self.b = b
        self.n = n
        for i in range(0, n):
            for j in range(0, n):
                if i < j:
                    self.U[i][j] = 0.0
                    self.L[i][j] = 0.0
                elif i > j:
                    self.L[i][j] = 0.0
                    self.U[i][j] = 0.0
                elif i == j:
                    self.L[i][j] = 0.0
                    self.U[i][j] = 0.0
        print("Etapa 0")
        print("Matriz A")
        self.imprimirMatrizA()
        print("Matriz L")
        self.imprimirMatrizL()
        print("Matriz U")
        self.imprimirMatrizU()
        for k in range(1, self.n + 1):
            print("Etapa: ", str(k))
            print("Encontrar la columna: ", str(k), " de L y la fila", str(k), " de U")
            print("Matriz A:")
            self.imprimirMatrizA()
            suma = 0
            for p in range(0, k - 1):
                suma += self.L[k - 1][p] * self.U[p][k - 1]

            print(self.A[k - 1][k - 1])
            self.U[k - 1][k - 1] = math.sqrt((self.A[k - 1][k - 1] - suma))
            self.L[k - 1][k - 1] = self.U[k - 1][k - 1]

            for j in range(k + 1, n + 1):
                suma = 0
                for p in range(0, k - 1):
                    suma += self.L[j - 1][p] * self.U[p][k - 1]
                self.L[j - 1][k - 1] = (self.A[j - 1][k - 1] - suma) / self.L[k - 1][k - 1]
            print("Matriz L:")
            self.imprimirMatrizL()
            for i in range(k + 1, n + 1):
                suma = 0
                for p in range(0, k - 1):
                    suma += self.L[k - 1][p] * self.U[p][i - 1]
                self.U[k - 1][i - 1] = (self.A[k - 1][i - 1] - suma) / self.U[k - 1][k - 1]
            print("Matriz U:")
            self.imprimirMatrizU()
            self.etapasL.append(np.copy(self.L))
            self.etapasU.append(np.copy(self.U))
        print("Sustición progresiva Lz = b:")
        self.z = self.sustitucionProgresiva()
        print("z:", str(self.z))
        print("Sustición regresiva Ux = z")
        self.xns = self.sustitucionRegresiva(self.z)
        for i in range(0, len(self.xns)):
            print("X", i + 1, " = ", self.xns[i])

    def sustitucionProgresiva(self):
        m = len(self.L)
        z = [0] * m
        for i in range(1, m + 1):
            suma = 0
            for p in range(i - 1, 0, -1):
                suma += self.L[i - 1][p - 1] * z[p - 1]
            z[i - 1] = (self.b[i - 1] - suma) / self.L[i - 1][i - 1]
        return z

    def sustitucionRegresiva(self, z):
        m = len(self.U)
        x = [0] * m
        for i in range(m - 1, -1, -1):
            suma = 0
            for j in range(i + 1, m):
                suma += self.U[i][j] * x[j]
            x[i] = (z[i] - suma) / self.U[i][i]
        return x

    def imprimirMatrizAb(self):

        # print('     '.join(str(self.marcas)))
        print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in self.Ab]))

    def imprimirMatrizA(self):

        # print('     '.join(str(self.marcas)))
        print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in self.A]))

    def imprimirMatrizB(self):

        # print('     '.join(str(self.marcas)))
        print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in self.b]))

    def imprimirMatrizL(self):

        # print('     '.join(str(self.marcas)))
        print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in self.L]))

    def imprimirMatrizU(self):

        # print('     '.join(str(self.marcas)))
        print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in self.U]))

    def getXns(self):
        return self.xns

    def getAb(self):
        return self.Ab

    def getEtapasL(self):
        return self.etapasL

    def getEtapasU(self):
        return self.etapasU

    def getZns(self):
        return self.z

    def reset(self):
        self.xns = []
        self.Ab = [[]]
        self.n = 0


#gausi = FactorizacionLUCholesky()
#a = [1,-2,0.5]
#b = [-2,5,-1.5]
#c = [-0.2,1.75,-1]

#bb = [-5,0,10]

#e = [a, b, c]

#gausi.factorizacionLUCholesky(e, bb, 3)
