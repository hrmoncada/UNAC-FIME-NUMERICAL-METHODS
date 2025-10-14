import numpy as np
class Jacobi:
    def __init__(self):
        self.xns = []
        self.A = [[]]
        self.b = []
        self.n = 0
        self.etapas = []

    def jacobi(self, A, b, n, x0, iteraciones, tolerancia, alpha):

        self.A = A
        self.b = b
        self.n = n
        iteraciones += 1
        contador = 1

        error = tolerancia + 1
        x = [0.0] * n
        self.etapas.append(np.copy(x0))
        print(x0)
        while (error > tolerancia) & (contador < iteraciones):
            for i in range(1, n + 1):
                suma = 0
                for j in range(1, n + 1):
                    if i != j:
                        suma = suma + self.A[i - 1][j - 1] * x0[j - 1]
                x[i - 1] = (self.b[i - 1] - suma) / self.A[i - 1][i - 1]
                x[i - 1] = alpha * (x[i - 1]) + (1 - alpha) * (x0[i - 1])
            error = self.norma(x, x0)
            for i in range(1, n + 1):
                x0[i - 1] = x[i - 1]
            contador += 1
            self.etapas.append(np.copy(x))
            print(x)
        self.xns = x

        if error < tolerancia:
            print("Vector X")
            print(self.xns)
            print(" Es una aproximacion con una tolerancia de ", str(tolerancia))
        else:
            print("Fracaso en", str(iteraciones), "iteraciones")

    def norma(self, x, x0):
        mayor = -1
        for i in range(1, self.n):
            if abs(x[i - 1] - x0[i - 1]) > mayor:
                mayor = abs(x[i - 1] - x0[i - 1])
        return mayor

    def getEtapas(self):
        return self.etapas

    def reset(self):
        self.xns = []
        self.Ab = [[]]
        self.n = 0


#gausi = Jacobi()
q = [45, 13, -4, 8]
r = [-5, -28, 4, -14]
p = [9, 15, 63, -7]
s = [2, 3, -8, -42]
#
a = [q, r, p, s]
#
b = [-25, 82, 75, -43]
#
x0 = [2, 2, 2, 2]
#
## def jacobi(self, A, b, n, x0, iteraciones, tolerancia, alpha):
#
#gausi.jacobi(a, b, 4, x0, 13, 10e-5, 1)
#print("JOCO")
