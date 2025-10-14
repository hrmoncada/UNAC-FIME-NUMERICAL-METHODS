# -*- coding: utf-8 -*-
import numpy as np
import math
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size
def eliminacionGaussianaSimple(n, Ab):
    rank = comm.rank
    size = comm.size
    distribuidas = []
    pivote = 0
    nuevasFilas = []
    if rank == 0:
        a = [[None for i in range(n)] for j in range(n)]
        for i in range(0, n):
            for j in range(0, n):
                a[i][j] = float(Ab[i][j])
        if (np.linalg.det(a) == 0):
            print("El sistema no tiene solución unica!")
            return
    for k in range(1, n):
        if (rank == 0):
            if(k == 1):
                print('\n'.join(['     '.join(['{:4}'.format(item, 2) for item in row]) for row in Ab]))
                print(" ")
                distribuidas = repartirEquitativamente(n, Ab, k)
                pivote = Ab[k-1]
            else:
                Ab = rehacerAb(Ab,n,nuevasFilas,k)
                pivote = Ab[k-1]
                distribuidas = repartirEquitativamente(n, Ab, k)
        arreglofilas = comm.scatter(distribuidas, root=0)
        filaPivote = comm.bcast(pivote, root = 0)
        for i in range(0, len(arreglofilas)):
            multiplicador = float(float(arreglofilas[i][k-1]) / float(filaPivote[k-1])) #Ab[i - 1][k - 1] / Ab[k - 1][k - 1]
            for j in range(0, len(arreglofilas[i])):
                multiplicacion = multiplicador*filaPivote[j]
                arreglofilas[i][j] = float(arreglofilas[i][j] - multiplicacion)
        nuevasFilas = comm.gather(arreglofilas,root=0)
    if rank == 0:
        for i in range(n):
            if(i!=n-1):
                Ab[i] = Ab[i]
            else:
                Ab[i] = nuevasFilas[0][0]
        xns = [0.0] * n
        for i in range(n, 0, -1):
            sumatoria = 0
            for p in range(i + 1, n + 1):
                sumatoria = sumatoria + Ab[i - 1][p - 1] * xns[p - 1]
            temp = (Ab[i - 1][n] - sumatoria) / Ab[i - 1][i - 1]
            xns[i - 1] = temp
            print("X" + str(i) + " = " + str(xns[i - 1]))

def eliminacionGaussianaParcial(n, Ab):
    rank = comm.rank
    size = comm.size
    distribuidas = []
    pivote = 0
    nuevasFilas = []
    if rank == 0:
        a = [[None for i in range(n)] for j in range(n)]
        for i in range(0, n):
            for j in range(0, n):
                a[i][j] = float(Ab[i][j])
        if (np.linalg.det(a) == 0):
            print("El sistema no tiene solución unica!")
            return
    for k in range(1, n):
        if (rank == 0):
            if (k == 1):
                print('\n'.join(['     '.join(['{:4}'.format(item, 2) for item in row]) for row in Ab]))
                print(" ")
                Ab = pivoteoParcial(k,Ab,n)
                distribuidas = repartirEquitativamente(n, Ab, k)
                pivote = Ab[k - 1]
            else:
                Ab = rehacerAb(Ab, n, nuevasFilas, k)
                Ab = pivoteoParcial(k,Ab,n)
                pivote = Ab[k - 1]
                distribuidas = repartirEquitativamente(n, Ab, k)

        arreglofilas = comm.scatter(distribuidas, root=0)
        filaPivote = comm.bcast(pivote, root=0)
        for i in range(0, len(arreglofilas)):
            multiplicador = float(
                float(arreglofilas[i][k - 1]) / float(filaPivote[k - 1]))  # Ab[i - 1][k - 1] / Ab[k - 1][k - 1]
            for j in range(0, len(arreglofilas[i])):
                multiplicacion = multiplicador * filaPivote[j]
                arreglofilas[i][j] = float(arreglofilas[i][j] - multiplicacion)
        nuevasFilas = comm.gather(arreglofilas, root=0)
    if rank == 0:
        for i in range(n):
            if (i != n - 1):
                Ab[i] = Ab[i]
            else:
                Ab[i] = nuevasFilas[0][0]
        print('\n'.join(['     '.join(['{:4}'.format(item, 2) for item in row]) for row in Ab]))
        print(" ")
        xns = [0.0] * n
        for i in range(n, 0, -1):
            sumatoria = 0
            for p in range(i + 1, n + 1):
                sumatoria = sumatoria + Ab[i - 1][p - 1] * xns[p - 1]
            temp = (Ab[i - 1][n] - sumatoria) / Ab[i - 1][i - 1]
            xns[i - 1] = temp
            print("X" + str(i) + " = " + str(xns[i - 1]))

def eliminacionGaussianaTotal(n, Ab):
    xns = []
    rank = comm.rank
    size = comm.size
    distribuidas = []
    pivote = 0
    nuevasFilas = []
    marcas = np.arange(1, n + 1)
    arregloMarcas = []
    arregloMarcas.append(np.copy(marcas))
    if rank == 0:
        a = [[None for i in range(n)] for j in range(n)]
        for i in range(0, n):
            for j in range(0, n):
                a[i][j] = float(Ab[i][j])
        if (np.linalg.det(a) == 0):
            print("El sistema no tiene solución unica!")
            return
    for k in range(1, n):
        if (rank == 0):
            if (k == 1):
                print(marcas)
                print('\n'.join(['     '.join(['{:4}'.format(item, 2) for item in row]) for row in Ab]))
                print(" ")
                Ab, marcas = pivoteoTotal(n,Ab,k, marcas)
                distribuidas = repartirEquitativamente(n, Ab, k)
                pivote = Ab[k - 1]
            else:
                Ab = rehacerAb(Ab, n, nuevasFilas, k)
                Ab, marcas = pivoteoTotal(n,Ab,k,marcas)
                pivote = Ab[k - 1]
                distribuidas = repartirEquitativamente(n, Ab, k)
            print(marcas)
        arreglofilas = comm.scatter(distribuidas, root=0)
        filaPivote = comm.bcast(pivote, root=0)
        for i in range(0, len(arreglofilas)):
            multiplicador = float(
                float(arreglofilas[i][k - 1]) / float(filaPivote[k - 1]))  # Ab[i - 1][k - 1] / Ab[k - 1][k - 1]
            for j in range(0, len(arreglofilas[i])):
                multiplicacion = multiplicador * filaPivote[j]
                arreglofilas[i][j] = float(arreglofilas[i][j] - multiplicacion)
        nuevasFilas = comm.gather(arreglofilas, root=0)
        arregloMarcas.append(np.copy(marcas).tolist())
    if rank == 0:
        for i in range(n):
            if (i != n - 1):
                Ab[i] = Ab[i]
            else:
                Ab[i] = nuevasFilas[0][0]
        print('\n'.join(['     '.join(['{:4}'.format(item, 2) for item in row]) for row in Ab]))
        print(" ")
        xns = [0.0] * n
        for i in range(n, 0, -1):
            sumatoria = 0
            for p in range(i + 1, n + 1):
                sumatoria = sumatoria + Ab[i - 1][p - 1] * xns[p - 1]
            temp = (np.copy(Ab[i - 1][n]) - sumatoria) / np.copy(Ab[i - 1][i - 1])
            xns[i - 1] = temp
        xns, marcas = organizarX(xns,marcas)
        for i in range(n):
            print("X" + str(marcas[i]) + " = " + str(xns[i]))
    return xns

def pivoteoTotal(n, Ab,k, marcas):
    max = 0
    filaMax = k - 1
    colMax = k - 1
    for i in range(k - 1, n):
        for j in range(k - 1, n):
            if abs(Ab[i][j]) > max:
                max = np.copy(abs(Ab[i][j]))
                filaMax = i
                colMax = j
    if filaMax != (k - 1):
        for i in range(0, len(Ab[0])):
            aux = np.copy(Ab[k - 1][i])
            Ab[k - 1][i] = np.copy(Ab[filaMax][i])
            Ab[filaMax][i] = np.copy(aux)
    if colMax != k - 1:
        for j in range(0, len(Ab[0]) - 1):
            aux = np.copy(Ab[j][k - 1])
            Ab[j][k - 1] = np.copy(Ab[j][colMax])
            Ab[j][colMax] = np.copy(aux)
        aux2 = np.copy(marcas[colMax])
        marcas[colMax] = np.copy(marcas[k - 1])
        marcas[k - 1] = np.copy(aux2)
    return Ab, marcas

def repartirEquitativamente(n, Ab, k):
    numeroDeNucleos = comm.size #4
    filasPorNucleo = int((n-k)/numeroDeNucleos)
    sobrantes = (n-k)%numeroDeNucleos
    filasDistribuidasPorNucleo = []
    if(sobrantes==0):
        for i in range(0,numeroDeNucleos):
            filasDeNucleoActual = []
            for j in range(filasPorNucleo*i,filasPorNucleo*i+filasPorNucleo):
                filasDeNucleoActual.append(Ab[j+k])
            filasDistribuidasPorNucleo.append(filasDeNucleoActual)
    else:
        for i in range(0,numeroDeNucleos):
            filasDeNucleoActual = []
            for j in range(filasPorNucleo*i,filasPorNucleo*i+filasPorNucleo):
                filasDeNucleoActual.append(Ab[j+k])
            filasDistribuidasPorNucleo.append(filasDeNucleoActual)
        for x in range(0, sobrantes):
            filasDistribuidasPorNucleo[x].append(Ab[numeroDeNucleos*filasPorNucleo+x+k])
    return filasDistribuidasPorNucleo

def rehacerAb(Ab,n,filasDistribuidasPorNucleo,k):
    k = k-1
    numeroDeNucleos = comm.size
    filasPorNucleo = int((n - k) / numeroDeNucleos)
    sobrantes = (n - k) % numeroDeNucleos
    if(sobrantes == 0):
        for i in range(0,numeroDeNucleos):
            filasDeNucleoActual = filasDistribuidasPorNucleo[i]
            for j in range(filasPorNucleo*i,filasPorNucleo*i+filasPorNucleo):
                Ab[j+k] = filasDeNucleoActual[j-filasPorNucleo*i]
        print('\n'.join(['     '.join(['{:4}'.format(item, 2) for item in row]) for row in Ab]))
    else:
        for i in range(0,numeroDeNucleos):
            filasDeNucleoActual = filasDistribuidasPorNucleo[i]
            for j in range(filasPorNucleo*i,filasPorNucleo*i+filasPorNucleo):
                Ab[j+k] = filasDeNucleoActual[j-filasPorNucleo*i]
        for x in range(0, sobrantes):
            Ab[numeroDeNucleos*filasPorNucleo+x+k] = filasDistribuidasPorNucleo[x][-1]
        print('\n'.join(['     '.join(['{:4}'.format(item, 2) for item in row]) for row in Ab]))
    print(" ")
    return Ab

def pivoteoParcial(k,Ab,n):
    elementoMax = abs(Ab[k - 1][k - 1])
    filaMax = k - 1
    for i in range(k - 1, n):
        temp = abs(Ab[i][k - 1])
        if temp > elementoMax:
            elementoMax = temp
            filaMax = i
    if filaMax != k - 1:
        for i in range(0, len(Ab[0])):
            temp = Ab[k - 1][i]
            Ab[k - 1][i] = Ab[filaMax][i]
            Ab[filaMax][i] = temp
    return Ab

def organizarX(xns,marcas):
    marcas1 = [0 for i in range(len(marcas))]
    xns1 = [0 for j in range(len(marcas))]

    for index, s in enumerate(marcas):
        s = s - 1
        temp = xns[index]
        temp1 = marcas[index]
        marcas[index] = marcas[s]
        xns[index] = xns[s]
        marcas1[s] = temp1
        xns1[s] = temp
    marcas = np.copy(marcas1)
    xns = np.copy(xns1)
    return(xns,marcas)

def jacobi(AB, n, x0, iteraciones, tolerancia, alpha):
    iteraciones += 1
    error = tolerancia + 1
    contador = 1
    rank = comm.rank
    distribuidas = []
    numeroDeNucleos = comm.size #4
    filasPorNucleo = int((n)/numeroDeNucleos)
    sobrantes = (n)%numeroDeNucleos
    #etapas.append(np.copy
    if(rank == 0):
        distribuidas = repartirEquitativamente(n,AB,0)
        print(distribuidas)
    arregloDeFilas = comm.scatter(distribuidas,root= 0)
    x = [0.0] * len(arregloDeFilas)
    while (error > tolerancia) & (contador < iteraciones):
        for i in range(0, filasPorNucleo):
            suma = float(0)
            for j in range(0, n):
                if (filasPorNucleo*rank)+i != j:
                    suma = suma + float(arregloDeFilas[i][j]) * float(x0[j])
            x[i] = (float(arregloDeFilas[i][-1]) - suma) / float(arregloDeFilas[i][len(arregloDeFilas)*rank+i])
            x[i] = alpha * (x[i]) + (1 - alpha) * (x0[i])
        for i in range(sobrantes):
            if i == rank:
                suma = float(0)
                for j in range(0, n):
                    if  n-sobrantes+i  != j:
                        suma = suma + float(arregloDeFilas[-1][j]) * float(x0[j])
                x[-1] = (float(arregloDeFilas[-1][-1]) - suma) / float(arregloDeFilas[-1][n-sobrantes+rank])
                x[-1] = alpha * (x[-1]) + (1 - alpha) * (x0[-1])
        nuevasFilas = comm.gather(x,root=0)
        if rank == 0:
            xns = [0.0] * (n-sobrantes)
            for i in range(len(nuevasFilas)):
                for j in range(len(nuevasFilas[i])):
                    xns[j+len(nuevasFilas[i])*i]= nuevasFilas[i][j]
            for jo in range(0, sobrantes):
                xns.append(nuevasFilas[jo][-1])
            print(xns)
            error = norma(xns, x0, n)
            #print(xns)
            x0 = np.copy(xns)
        error = comm.bcast(error,root=0)
        x0 = comm.bcast(x0,root= 0)
        contador += 1
        #etapas.append(np.copy(x))
    if(rank == 0):
        if error < tolerancia:
            print("Vector X")
            print(xns)
            print(" Es una aproximacion con una tolerancia de ", str(tolerancia))
        else:
            print("Fracaso en", str(iteraciones), "iteraciones")

def norma(x, x0,n):
    mayor = -1
    for i in range(1, n):
        if abs(x[i - 1] - x0[i - 1]) > mayor:
            mayor = abs(x[i - 1] - x0[i - 1])
    return mayor

def sustitucionProgresiva(L, b):
    m = len(L)
    z = [0] * m
    for i in range(1, m + 1):
        suma = 0
        for p in range(i - 1, 0, -1):
            suma += L[i - 1][p - 1] * z[p - 1]
        z[i - 1] = (b[i - 1] - suma) / L[i - 1][i - 1]
    return z

def sustitucionRegresiva(U, z):
    m = len(U)
    x = [0] * m
    for i in range(m - 1, -1, -1):
        suma = 0
        for j in range(i + 1, m):
            suma += U[i][j] * x[j]
        x[i] = (z[i] - suma) / U[i][i]
    return x

def imprimirMatriz(m):
    print('\n'.join(['     '.join(['{:4}'.format(item, 2) for item in row]) for row in m]))

def factorizacionLUDoolittle(A, b, n):
    distribuidasL = []
    distribuidasU = []
    distribuidasA = []
    distribuidasTransA = []
    L = []
    U = []
    if rank == 3:
        if np.linalg.det(A) == 0:
            return
        L = [[0.0] * n for i in range(n)]
        U = [[0.0] * n for i in range(n)]
        distribuidasL = repartirEquitativamente(n, L, 0)
    myL = comm.scatter(distribuidasL, root=3)
    for it in range(len(myL)):
        myL[it][rank + (it * size)] = 1.0
    temp = comm.gather(myL, root=3)
    if rank == 3:
        for i in range(0, len(temp)):
            for j in range(len(temp[i])):
                L[i + (j * size)] = temp[i][j]

    for k in range(0, n - 1):
        if rank == 3:
            suma = 0.0
            transU = np.transpose(U).tolist()
            for p in range(0, k + 1):
                suma += L[k][p] * transU[p][k]
            U[k][k] = A[k][k] - suma
            transA = np.transpose(A)
            distribuidasU = repartirEquitativamente(n, U, k + 1)
            distribuidasTransA = repartirEquitativamente(n, transA[k], k + 1)
            distribuidasA = repartirEquitativamente(n, A[k], k + 1)

        if k == 0:
            myL = [0.0] * n
        else:
            if rank == 3:
                distribuidasL = L[k]
            myL = comm.bcast(distribuidasL, root=3)
        # U
        myU = comm.scatter(distribuidasU, root=3)
        myTransA = comm.scatter(distribuidasTransA, root=3)
        myA = comm.scatter(distribuidasA, root=3)
        actualDiag = comm.bcast(U, root=3)
        d = actualDiag[k][k]
        suma = 0.0
        for it in range(0, len(myU)):
            for p in range(0, k + 1):
                suma += myU[it][p] * myL[p]
            myU[it][k] = myA[it] - suma
        temp = comm.gather(myU, root=3)
        if rank == 3:
            for i in range(0, k + 1):
                temp.pop()
            for i in range(0, len(temp)):
                for j in range(len(temp[i])):
                    U[i + (k + 1)] = temp[i][j]
            distribuidasL = repartirEquitativamente(n, L, k + 1)
        # L
        myL = comm.scatter(distribuidasL, root=3)
        if k == 0:
            if len(myL) == 0:
                myU = [0.0] * len(myL)
            else:
                myU = [0.0] * len(myL[0])
        else:
            if rank == 3:
                distribuidasU = U[k]
            myU = comm.bcast(distribuidasU, root=3)
        suma = 0.0
        print(myU,myL)
        for it in range(0, len(myL)):
            for p in range(0, k + 1):
                suma += myU[p] * myL[it][p]
            result = (myTransA[it] - suma) / d
            myL[it][k] = result

        temp = comm.gather(myL, root=3)
        if rank == 3:
            for i in range(k + 1):
                temp.pop()
            for i in range(0, len(temp)):
                for j in range(len(temp[i])):
                    L[i + (k + 1)] = temp[i][j]
    if rank == 3:
        suma = 0.0
        for p in range(0, n):
            suma += L[n - 1][p] * U[n - 1][p]
        U[n - 1][n - 1] = A[n - 1][n - 1] - suma
        U = np.transpose(U).tolist()
        imprimirMatriz(L)
        print("-----")
        imprimirMatriz(U)
        z = sustitucionProgresiva(L, b)
        x = sustitucionRegresiva(U, z)
        for i in range(0, len(x)):
            print("X", i + 1, " = ", x[i])

def factorizacionLUCrout(A, b, n):
    distribuidasL = []
    distribuidasU = []
    distribuidasA = []
    distribuidasTransA = []
    L = []
    U = []
    if rank == 3:
        if np.linalg.det(A) == 0:
            print("JOCO")
            return
        L = [[0.0] * n for i in range(n)]
        U = [[0.0] * n for i in range(n)]
        distribuidasU = repartirEquitativamente(n, U, 0)
    myU = comm.scatter(distribuidasU, root=3)
    for it in range(len(myU)):
        myU[it][rank + (it * size)] = 1.0
    temp = comm.gather(myU, root=3)
    if rank == 3:
        for i in range(0, len(temp)):
            for j in range(len(temp[i])):
                U[i + (j * size)] = temp[i][j]

    for k in range(0, n - 1):
        if rank == 3:
            suma = 0.0
            transU = np.transpose(U).tolist()
            for p in range(0, k + 1):
                suma += L[k][p] * transU[p][k]
            L[k][k] = A[k][k] - suma
            transA = np.transpose(A)
            distribuidasL = repartirEquitativamente(n, L, k + 1)
            distribuidasTransA = repartirEquitativamente(n, transA[k], k + 1)
            distribuidasA = repartirEquitativamente(n, A[k], k + 1)

        if k == 0:
            myU = [0.0] * n
        else:
            if rank == 3:
                distribuidasU = U[k]
            myU = comm.bcast(distribuidasU, root=3)
        # L
        myL = comm.scatter(distribuidasL, root=3)
        myTransA = comm.scatter(distribuidasTransA, root=3)
        myA = comm.scatter(distribuidasA, root=3)
        actualDiag = comm.bcast(L, root=3)
        d = actualDiag[k][k]
        suma = 0.0
        for it in range(0, len(myL)):
            for p in range(0, k + 1):
                suma += myL[it][p] * myU[p]
            myL[it][k] = myTransA[it] - suma
        temp = comm.gather(myL, root=3)
        if rank == 3:
            for i in range(0, k + 1):
                temp.pop()
            for i in range(0, len(temp)):
                for j in range(len(temp[i])):
                    L[i + (k + 1)] = temp[i][j]
            distribuidasU = repartirEquitativamente(n, U, k + 1)
        # U
        myU = comm.scatter(distribuidasU, root=3)
        if k == 0:
            if len(myU) == 0:
                myL = [0.0] * len(myU)
            else:
                myL = [0.0] * len(myU[0])
        else:
            if rank == 3:
                distribuidasL = L[k]
            myL = comm.bcast(distribuidasL, root=3)
        suma = 0.0
        for it in range(0, len(myU)):
            for p in range(0, k + 1):
                suma += myL[p] * myU[it][p]
            result = (myA[it] - suma) / d
            myU[it][k] = result

        temp = comm.gather(myU, root=3)
        if rank == 3:
            for i in range(k + 1):
                temp.pop()
            for i in range(0, len(temp)):
                for j in range(len(temp[i])):
                    U[i + (k + 1)] = temp[i][j]
    if rank == 3:
        suma = 0.0
        for p in range(0, n):
            suma += L[n - 1][p] * U[n - 1][p]
        L[n - 1][n - 1] = A[n - 1][n - 1] - suma
        U = np.transpose(U).tolist()
        imprimirMatriz(L)
        print("-----")
        imprimirMatriz(U)
        z = sustitucionProgresiva(L, b)
        x = sustitucionRegresiva(U, z)
        for i in range(0, len(x)):
            print("X", i + 1, " = ", x[i])

def factorizacionLUCholesky(A, b, n):
    distribuidasL = []
    distribuidasU = []
    distribuidasA = []
    distribuidasTransA = []
    L = []
    U = []
    myU = []
    transA = []
    actualVal = 0.0
    transU = []
    if rank == 3:
        if (any(elem < 0 for elem in np.diag(A))) | (np.linalg.det(A) == 0):
            return
        L = [[0.0] * n for i in range(n)]
        U = [[0.0] * n for i in range(n)]
        transA = np.transpose(A)

    for k in range(0, n - 1):
        if rank == 3:
            suma = 0.0
            transU = np.transpose(U).tolist()
            for p in range(0, k + 1):
                suma += L[k][p] * transU[p][k]
            L[k][k] = math.sqrt((A[k][k] - suma))
            U[k][k] = L[k][k]
            distribuidasL = repartirEquitativamente(n, L, k + 1)
            # print(distribuidasL,k)

            distribuidasTransA = repartirEquitativamente(n, transA[k], k + 1)
            distribuidasA = repartirEquitativamente(n, A[k], k + 1)

        if k == 0:
            myU = [0.0] * n
        else:
            if rank == 3:
                distribuidasU = U[k]
            myU = comm.bcast(distribuidasU, root=3)

        myL = comm.scatter(distribuidasL, root=3)
        myTransA = comm.scatter(distribuidasTransA, root=3)
        myA = comm.scatter(distribuidasA, root=3)
        actualDiag = comm.bcast(U, root=3)
        d = actualDiag[k][k]
        suma = 0.0
        for it in range(0, len(myL)):
            for p in range(0, k + 1):
                suma += myL[it][p] * myU[p]
            myL[it][k] = (myTransA[it] - suma) / d
        temp = comm.gather(myL, root=3)
        if rank == 3:
            for i in range(0, k + 1):
                temp.pop()
            for i in range(0, len(temp)):
                for j in range(len(temp[i])):
                    L[i + (k + 1)] = temp[i][j]
            distribuidasU = repartirEquitativamente(n, U, k + 1)
        myU = comm.scatter(distribuidasU, root=3)
        if k == 0:
            if len(myU) == 0:
                myL = [0.0] * len(myU)
            else:
                myL = [0.0] * len(myU[0])
        else:
            if rank == 3:
                distribuidasL = L[k]
            myL = comm.bcast(distribuidasL, root=3)
        suma = 0.0
        for it in range(0, len(myU)):
            for p in range(0, k + 1):
                suma += myL[p] * myU[it][p]
            result = (myA[it] - suma) / d
            myU[it][k] = result

        temp = comm.gather(myU, root=3)
        if rank == 3:
            for i in range(k + 1):
                temp.pop()
            for i in range(0, len(temp)):
                for j in range(len(temp[i])):
                    U[i + (k + 1)] = temp[i][j]
    if rank == 3:
        suma = 0.0
        for p in range(0, n):
            suma += L[n - 1][p] * U[n - 1][p]
        L[n - 1][n - 1] = math.sqrt((A[n - 1][n - 1] - suma))
        U[n - 1][n - 1] = L[n - 1][n - 1]
        U = np.transpose(U).tolist()
        z = sustitucionProgresiva(L, b)
        x = sustitucionRegresiva(U, z)
        for i in range(0, len(x)):
            print("X", i + 1, " = ", x[i])




#a = [34, -5, 6, 12,37]
#b = [-9,43,21,8,123]
#c = [-12, 4, 75, 22,16]
#d = [7,5,13,65,9]
# = [a,b,c,d]

#a = [-7, 2, -3, 4, -12]
#b = [5, -1, 14, -1, 13]
#c = [1, 9, -7, 5, 31]
#d = [-12, 13, -8, -4, -32]
#e = [a, c, b, d]

#a = [-4,-4,1,-1,7,-4,1,-37]
#b = [8,5,-4,3,-6,7,1,16]
#c = [1,7,8,7,-9,-1,3,100]
#d = [-6,2,-9,1,-1,-2,-8,-72]
#e = [6,-8,-3,8,2,6,-6,-81]
#f = [2,-2,1,-1,2,-7,4,9]
#g = [-2,7,-2,-5,3,3,4,20]
#e = [a, b, c, d,e,f,g]

#a = [12, 3, -8, 9,23]
#b = [2, -3, 5, 12,-45]
#c = [2, -5, 3, -8,34]
#e = [3,-8,45,29,34]
#d = [a, b, c, e]


a = [1, -2, 0.5, -5]
b = [-2, 5, -1.5, 0]
c = [-0.2, 1.75, -1, 10]

e = [a, b, c]
eliminacionGaussianaSimple(3, e)
#print(eliminacionGaussianaTotal(4, d))
#eliminacionGaussianaSimple(7, e)

#a = [[13,-3,4,-8,-20],[5,-15,-6,-4,-32],[7,-3,14,5,-36],[6,-4,-9,-17,-40]]
#jacobi(a,4,[6,5,-7,7],100,10e-6,1)