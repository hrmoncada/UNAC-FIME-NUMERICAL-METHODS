def sor(A,b,x0,w,tol,maxiter):
    """
    Vamos a desarrollar el método de resolución de ecuaciones por método SOR. 
    INPUT:
        - A: Matriz del sistema lineal
        - b: Vector de términos independientes
        - x0: Estimación inicial del sistema
        - tol: Tolerancia de error cometido
        - maxiter: Número máximo de iteraciones en el método.
    OUTPUT:
        - x: Solución del sistema
        - i: Número de iteraciones utilizadas.
    """
    from numpy import diag, tril, triu, matmul, inf, zeros
    from numpy.linalg import  inv, norm
    k = 1 
    stop = tol+1
    L = tril(A, -1)
    D = diag(diag(A))
    U = triu(A,1)
    M = D+w*L
    N = (-w*U + (1-w)*D)
    n = len(x0)
    while k < maxiter and stop > tol:
        x = zeros([n,1])
        d = w*b+matmul(N,x0)
        B = M
        x[0] = d[0]/M[0,0]
        for i in range(1,n):
            s = 0
            for j in range(0,n-1):
                s = s+B[i,j]*x[j]
            x[i] = (d[i]-s)/B[i,i]
        k += 1
        stop = norm(x-x0, ord= inf)/norm(x0, ord=inf)
        x0 = x
    return(x, k)


from numpy import array, matrix

A = matrix([[4,3,0],[3,4,-1],[0,-1,4]])
b = array([[24],[30],[-24]])
x0 = array([[0],[0],[0]])
tol = 10**(-7)
w = 1.25
maxiter = 100
print(sor(A,b,x0,w,tol,maxiter))