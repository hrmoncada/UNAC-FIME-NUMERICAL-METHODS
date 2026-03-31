'''==============================
 Sistema 1D
 dy/dt = -y + sin(t)
 y(0) = 1
==============================
Compilar

python ODE_3_1D_Runge_Kutta_2_Runge_Kutta_4.py
'''

import numpy as np
import matplotlib.pyplot as plt

# Definición de la EDO 1D
def f(t, y):
    return -y + np.sin(t)

# -------------------------
# Runge-Kutta de orden 2
# -------------------------
def rk2(f, t0, y0, h, n):
    t = np.zeros(n + 1)
    y = np.zeros(n + 1)

    t[0] = t0
    y[0] = y0

    for i in range(n):
        k1 = f(t[i], y[i])
        k2 = f(t[i] + h, y[i] + h * k1)

        y[i + 1] = y[i] + (h / 2) * (k1 + k2)
        t[i + 1] = t[i] + h

    return t, y

# -------------------------
# Runge-Kutta de orden 4
# -------------------------
def rk4(f, t0, y0, h, n):
    t = np.zeros(n + 1)
    y = np.zeros(n + 1)

    t[0] = t0
    y[0] = y0

    for i in range(n):
        k1 = f(t[i], y[i])
        k2 = f(t[i] + h / 2, y[i] + h * k1 / 2)
        k3 = f(t[i] + h / 2, y[i] + h * k2 / 2)
        k4 = f(t[i] + h, y[i] + h * k3)

        y[i + 1] = y[i] + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        t[i + 1] = t[i] + h

    return t, y

# Parámetros
t0 = 0.0
y0 = 1.0
h = 0.1
n = 100

# Soluciones
t_rk2, y_rk2 = rk2(f, t0, y0, h, n)
t_rk4, y_rk4 = rk4(f, t0, y0, h, n)

# Gráfica
plt.figure()
plt.plot(t_rk2, y_rk2, label="Runge-Kutta 2")
plt.plot(t_rk4, y_rk4, label="Runge-Kutta 4")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("EDO 1D resuelta con RK2 y RK4")
plt.legend()
plt.show()

