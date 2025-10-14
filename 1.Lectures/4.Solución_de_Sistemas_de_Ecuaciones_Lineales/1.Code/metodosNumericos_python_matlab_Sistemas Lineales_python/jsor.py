def jsor(A,b,x0,w,tol,maxiter):
    """
    Vamos a desarrollar el método de resolución de ecuaciones por método JSOR. 
    INPUT:
        - A: Matriz del sistema lineal
        - b: Vector de términos independientes
        - x0: Estimación inicial del sistema
        - w: Parámetro de relajación. Debe estar en [0,1]
        - tol: Tolerancia de error cometido
        - maxiter: Número máximo de iteraciones en el método.
    OUTPUT:
        - x: Solución del sistema
        - i: Número de iteraciones utilizadas.
    """
    from numpy import diag, matmul, inf
    from numpy.linalg import norm
    i = 1
    stop = tol+1
    iM = diag(diag(1/A))

    while i < maxiter and stop > tol:
        r = b - matmul(A,x0)
        x = x0 + w*matmul(iM,r)
        i += 1
        stop = norm(x-x0, ord= inf)/norm(x0, ord=inf)
        x0 = x
    return(x, i)


from numpy import array, matrix, matmul

A = matrix([[4,3,0],[3,4,-1],[0,-1,4]])
b = array([[24],[30],[-24]])
x0 = array([[0],[0],[0]])
tol = 10**(-7)
w = 0.9
maxiter = 100
print(jsor(A,b,x0,w,tol,maxiter))