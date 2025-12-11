import numpy as np
import matplotlib.pyplot as plt

def euler_forward(f, y0, t):
    y = np.zeros(len(t))
    y[0] = y0
    dt = t[1] - t[0]

    for n in range(len(t)-1):
        y[n+1] = y[n] + dt * f(y[n], t[n])

    return y

def euler_backward(lambda_, y0, t):
    y = np.zeros(len(t))
    y[0] = y0
    dt = t[1] - t[0]

    for n in range(len(t)-1):
        y[n+1] = y[n] / (1 + lambda_ * dt)

    return y

def euler_centered(f, y0, t):
    y = np.zeros(len(t))
    dt = t[1] - t[0]

    # Paso inicial con Euler Forward
    y[0] = y0
    y[1] = y[0] + dt * f(y[0], t[0])

    for n in range(1, len(t)-1):
        y[n+1] = y[n-1] + 2 * dt * f(y[n], t[n])

    return y


# Parámetros
lambda_ = 1.0
y0 = 1.0
t = np.linspace(0, 10, 200)

f = lambda y, t: -lambda_ * y

# Solución exacta
y_exact = y0 * np.exp(-lambda_ * t)

# Métodos numéricos
y_fe = euler_forward(f, y0, t)
y_be = euler_backward(lambda_, y0, t)
y_ce = euler_centered(f, y0, t)

# Gráfica
plt.figure()
plt.plot(t, y_exact, label="Exacta")
plt.plot(t, y_fe, linestyle='--', label="Euler Forward")
plt.plot(t, y_be, linestyle='--', label="Euler Backward")
plt.plot(t, y_ce, linestyle='--', label="Euler Centered")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.legend()
plt.title("Métodos Euler 1D")
plt.show()

