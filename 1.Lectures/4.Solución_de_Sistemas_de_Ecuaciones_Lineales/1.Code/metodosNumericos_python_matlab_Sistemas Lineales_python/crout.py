def Crout(dP ,dS ,dI ,b):
    import numpy as np
    """
    Función para resolver un sistema de una matriz tridiagonal.
    Necesitamos las tres diagonales y el vector independiente.
        -dP diag of matrix to solve
        -dS diag sup mtrix to solve
        -dI diag Inf matrix to solve
        -b vector independent
    
    Como output, vamos a obtener el resultado de la solución. 
    """

    
    n = len(b)
    l = np.zeros(n)
    u = np.zeros(n)
    z = np.zeros(n)
    x = np.zeros(n)
    # 1. Obtención de las matrices L y U tales que A = LU
    l[0] = dP[0]
    u[0] = dS[0]/l[0]

    for i in range(1,n-2):
        l[i] = dP[i]-dI[(i-1)]*u[(i-1)]
        u[i] = dS[i]/l[i]
    

    l[(n-1)] = dP[(n-1)]-dI[(n-2)]*u[(n-2)]

    z[0]  = b[0]/l[0]

    for i in range(1,n-1):
        z[i]  <- (1/l[i])*(b[i]-dI[(i-2)]*z[(i-2)])
    

    x[(n-1)]  <- z[(n-1)]

    for i in range(n-2,0,-1):
        x[i]  <- z[i]-u[i]*x[(i)]
    
    return(x)

