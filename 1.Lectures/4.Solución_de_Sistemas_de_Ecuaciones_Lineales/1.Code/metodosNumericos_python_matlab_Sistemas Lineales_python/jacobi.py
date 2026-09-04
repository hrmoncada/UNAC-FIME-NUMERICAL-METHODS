def jacobi(A,b,x0,tol,maxiter):
    """
    Vamos a desarrollar el método de resolución de ecuaciones por método Jacobi. 
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
    from numpy import diag, tril, triu, matmul, inf
    from numpy.linalg import  inv, norm
    i = 1
    stop = tol+1
    L = tril(A, -1)
    U = triu(A,1)
    iM = diag(diag(1/A))
    N = -(L+U)
    while i < maxiter and stop > tol:
        x = matmul(matmul(iM,N),x0) + matmul(iM,b)
        i += 1
        stop = norm(x-x0, ord= inf)/norm(x0, ord=inf)
        x0 = x
    return(x, i)


from numpy import array, matrix

A = matrix([[10 , -1, 2, 0], [-1, 11,-1,3],[2,-1,10,-1],[0,3,-1,8]])
b = array([[6],[25],[-11],[15]])
x0 = array([[0],[0],[0],[0]])
tol = 10**(-3)
maxiter = 100
print(A)
print(b)
print(jacobi(A,b,x0,tol,maxiter))