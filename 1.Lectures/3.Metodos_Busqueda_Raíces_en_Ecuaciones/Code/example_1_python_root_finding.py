import math

# ----------------------------
# Método de Bisección
# ----------------------------
def biseccion(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("La función debe cambiar de signo en [a, b]")
    
    for i in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c, i+1
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, max_iter

# ----------------------------
# Método de Regla Falsa (Falsa Posición)
# ----------------------------
def falsa_posicion(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("La función debe cambiar de signo en [a, b]")

    for i in range(max_iter):
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))
        if abs(f(c)) < tol:
            return c, i+1
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, max_iter

# ----------------------------
# Método de Punto Fijo
# ----------------------------
def punto_fijo(g, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_next = g(x)
        if abs(x_next - x) < tol:
            return x_next, i+1
        x = x_next
    return x, max_iter

# ----------------------------
# Método de Newton-Raphson
# ----------------------------
def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        if df(x) == 0:
            raise ZeroDivisionError("La derivada se anuló")
        x_next = x - f(x)/df(x)
        if abs(x_next - x) < tol:
            return x_next, i+1
        x = x_next
    return x, max_iter

# ----------------------------
# Método de la Secante
# ----------------------------
def secante(f, x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        if f(x1) - f(x0) == 0:
            raise ZeroDivisionError("Denominador cero en secante")
        x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        if abs(x2 - x1) < tol:
            return x2, i+1
        x0, x1 = x1, x2
    return x2, max_iter

# ----------------------------
# Ejemplo de uso
# ----------------------------
if __name__ == "__main__":
    f = lambda x: x**3 - x - 2  # raíz real ~ 1.521
    df = lambda x: 3*x**2 - 1
    g = lambda x: (x+2)**(1/3)  # función para punto fijo

    print("Bisección:", biseccion(f, 1, 2))
    print("Falsa Posición:", falsa_posicion(f, 1, 2))
    print("Punto Fijo:", punto_fijo(g, 1.5))
    print("Newton-Raphson:", newton_raphson(f, df, 1.5))
    print("Secante:", secante(f, 1, 2))

