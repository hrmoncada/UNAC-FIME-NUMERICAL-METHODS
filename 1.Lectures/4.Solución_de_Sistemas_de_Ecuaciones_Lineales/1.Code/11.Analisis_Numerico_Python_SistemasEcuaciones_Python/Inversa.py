import numpy as np


class Inversa:
    def __init__(self):
        self.xns = []
        self.A = [[]]
        self.identidad = [[]]
        self.L = [[]]
        self.U = [[]]
        self.n = 0
        self.zs = []
        self.inv = [[]]
        self.unica = True

    def inversa(self, L, U, n):
        self.L = L
        self.U = U
        self.n = n
        self.identidad = [[0.0] * n for i in range(0,n)]
        self.inv = np.array([[0.0] * n for i in range(0,n)])

        for i in range(0, n):
            for j in range(0, n):
                if i == j:
                    self.identidad[i][j] = 1
                else:
                    self.identidad[i][j] = 0

        for i in range(0, n):
            self.inv[i] = (self.sustitucionRegresiva(self.sustitucionProgresiva(self.identidad[i])))
        self.inv = self.inv.transpose()
        return self.inv

    def sustitucionProgresiva(self, b):
        m = len(self.L)
        print("tamaño L ", str(m))
        z = [0] * m
        for i in range(1, m + 1):
            suma = 0
            for p in range(i - 1, 0, -1):
                suma += self.L[i - 1][p - 1] * z[p - 1]

            print(i - 1)
            z[i - 1] = (b[i - 1] - suma) / self.L[i - 1][i - 1]
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


#gausi = Inversa()
#L = [[36, 0.0, 0.0, 0.0],
#     [5.0, -45.42, 0.0, 0.0],
#     [6.0, 7.5, 59.41, 0.0],
#     [2.0, 2.83, -7.12, -42.0]]
#U = [[1.0, 0.08, -0.11, 0.14],
#     [0.0, 1.0, -0.23, 0.06],
#     [0.0, 0.0, 1.0, 0.06],
#     [0.0, 0.0, 0.0, 1.0]]
#gausi.inversa(L,U,4)
