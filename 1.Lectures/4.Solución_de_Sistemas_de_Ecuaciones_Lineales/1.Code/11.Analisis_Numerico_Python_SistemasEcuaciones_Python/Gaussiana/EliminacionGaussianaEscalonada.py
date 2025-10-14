import numpy as np


class EliminacionGaussianaEscalonado:
    def __init__(self):
        self.xns = []
        self.Ab = [[]]
        self.n = 0
        self.unica = True  # Este bool cuando es verdad podemos calcular la solucion, cuando es falsa, no se puede calcular nada
        self.etapas = []
        self.beforeordenar = []
        self.s = []

    def eliminacionGaussianaEscalonado(self, n, Ab):
        self.Ab = Ab
        self.n = n


        self.etapas.append(np.copy(self.Ab))
        self.xns = [0.0] * n
        self.s = [0.0] * self.n
        # self.arregloMarcas.append(np.arange(1,n+1).tolist())
        print("Matriz Original")

        self.imprimirMatriz()
        self.busquedaMayorFila()

        print("Vector de mayores de cada fila: ")
        print(self.s)

        a = [[None for i in range(self.n)] for j in range(self.n)]

        for i in range(0, self.n):
            for j in range(0, self.n):
                a[i][j] = float(self.Ab[i][j])

        if (np.linalg.det(a) == 0):
            self.unica = False
            print("El sistema no tiene solución unica porque el determinante de A es 0")
            return

        for k in range(1, n):
            print("Etapa " + str(k))
            self.pivoteoEscalonado(k)
            print("Objetivo: Poner ceros debajo del elemento A" + str(k) + "," + str(k) + "= " + str(
                self.Ab[k - 1][k - 1]))



            if self.unica == False:
                return

            print("Multiplicadores:")
            for i in range(k + 1, n + 1):
                if self.Ab[k - 1][k - 1] == 0:
                    print("No tiene solucion unica")
                    self.unica = False
                    return

                multiplicador = np.copy(self.Ab[i - 1][k - 1]) / np.copy(self.Ab[k - 1][k - 1])

                for j in range(k, n + 2):
                    self.Ab[i - 1][j - 1] = np.copy(self.Ab[i - 1][j - 1] - multiplicador * self.Ab[k - 1][j - 1])
                print("Multiplicador" + str(i) + "," + str(k) + " : " + str(multiplicador))
            print(" ")
            self.etapas.append(np.copy(self.Ab))
            self.imprimirMatriz()


        print("Sustitución Regresiva")



        for i in range(n, 0, -1):
            sumatoria = 0
            for p in range(i + 1, n + 1):
                sumatoria = sumatoria + self.Ab[i - 1][p - 1] * self.xns[p - 1]
            temp = (np.copy(self.Ab[i - 1][n]) - sumatoria) / np.copy(self.Ab[i - 1][i - 1])
            self.xns[i - 1] = temp
            print("X" + str(i) + " = " + str(self.xns[i - 1]))

        print("Uno", self.xns)
        print(self.xns)

    def pivoteoEscalonado(self, k):
        max = 0
        filaMax = k - 1
        cocientes = [0.0] * self.n

        for i in range(k,self.n+1):
            cocientes[i-1] = abs(self.Ab[i-1][k-1]/self.s[i-1])

        print("")
        print("Vector de cocientes")
        print(cocientes)

        for i in range (k-1,self.n):
            if cocientes[i] > max:
                max = cocientes[i]
                filaMax = i

        print("El cociente mayor es: ", str(max), "de la fila ",
              str(filaMax+1))
        if max ==0:
            print("El sistema no tiene solucion unica")
            self.unica = False
            return
        else:
            if filaMax != k-1:
                print("")
                print("Cambio de fila", str(k), "con fila", str(filaMax+1))

                for i in range(0, len(self.Ab[0])):
                    aux = self.Ab[k-1][i]
                    self.Ab[k - 1][i] = self.Ab[filaMax][i];
                    self.Ab[filaMax][i] = aux;

                aux2 = self.s[k - 1];
                self.s[k - 1] = self.s[filaMax];
                self.s[filaMax] = aux2;

                print("Matriz A")
                self.imprimirMatriz()
                print("Vector de mayores de cada fila")
                print(self.s)

    def imprimirMatriz(self):
        print('\n'.join(['     '.join(['{:4}'.format(item, 2) for item in row]) for row in self.Ab]))

    def imprimirMatrizEtapas(self):
        for i in self.etapas:
            print('\n'.join(['     '.join(['{:4}'.format(item, 2) for item in row]) for row in i]))
            print(" ")

    def getXns(self):
        return self.xns

    def getAb(self):
        return self.Ab

    def getEtapas(self):
        return self.etapas
    def getS(self):
        return self.s

    def busquedaMayorFila(self):

        for i in range(1,self.n+1):
            for j in range(1, self.n +1):
                if abs(self.Ab[i-1][j-1]) > self.s[i-1]:
                    self.s[i-1] = abs(self.Ab[i-1][j-1])




    def reset(self):
        self.xns = []
        self.Ab = [[]]
        self.n = 0
        self.arregloMarcas = []
        self.etapas = []


#gausi = EliminacionGaussianaEscalonado()
#a = [1, -2, 0.5, -5]
#b = [-2, 5, -1.5, 0]
#c = [-0.2, 1.75, -1, 10]

#e = [a, b, c]

#gausi.eliminacionGaussianaEscalonado(3, e)
#print("JOCO")
#print(gausi.arregloMarcas)
