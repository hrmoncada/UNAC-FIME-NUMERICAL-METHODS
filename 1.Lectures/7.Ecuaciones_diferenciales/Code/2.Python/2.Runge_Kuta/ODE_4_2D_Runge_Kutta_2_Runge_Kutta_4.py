'''==============================
 Sistema 1D
 dx/dt = y 
 dy/dt = -x

==============================
Compilar
python ODE_4_2D_Runge_Kutta_2_Runge_Kutta_4.py
'''
import numpy as np
import matplotlib.pyplot as plt

# Sistema de ecuaciones
def system(t, x, y):
    dxdt = y
    dydt = -x
    return dxdt, dydt

# Parámetros
t0, tf, h = 0.0, 20.0, 0.05
t = np.arange(t0, tf + h, h)

# Condiciones iniciales
x0, y0 = 1.0, 0.0

# =========================
# Método de Runge-Kutta 2
# =========================
x_rk2 = np.zeros(len(t))
y_rk2 = np.zeros(len(t))
x_rk2[0], y_rk2[0] = x0, y0

for i in range(len(t) - 1):
    k1x, k1y = system(t[i], x_rk2[i], y_rk2[i])
    k2x, k2y = system(
        t[i] + h,
        x_rk2[i] + h * k1x,
        y_rk2[i] + h * k1y
    )
    x_rk2[i+1] = x_rk2[i] + (h/2)*(k1x + k2x)
    y_rk2[i+1] = y_rk2[i] + (h/2)*(k1y + k2y)

# =========================
# Método de Runge-Kutta 4
# =========================
x_rk4 = np.zeros(len(t))
y_rk4 = np.zeros(len(t))
x_rk4[0], y_rk4[0] = x0, y0

for i in range(len(t) - 1):
    k1x, k1y = system(t[i], x_rk4[i], y_rk4[i])
    k2x, k2y = system(
        t[i] + h/2,
        x_rk4[i] + h*k1x/2,
        y_rk4[i] + h*k1y/2
    )
    k3x, k3y = system(
        t[i] + h/2,
        x_rk4[i] + h*k2x/2,
        y_rk4[i] + h*k2y/2
    )
    k4x, k4y = system(
        t[i] + h,
        x_rk4[i] + h*k3x,
        y_rk4[i] + h*k3y
    )

    x_rk4[i+1] = x_rk4[i] + (h/6)*(k1x + 2*k2x + 2*k3x + k4x)
    y_rk4[i+1] = y_rk4[i] + (h/6)*(k1y + 2*k2y + 2*k3y + k4y)

# =========================
# Gráficos
# =========================

# Espacio de fases
plt.figure()
plt.plot(x_rk2, y_rk2, label="RK2")
plt.plot(x_rk4, y_rk4, label="RK4")
plt.xlabel("x(t)")
plt.ylabel("y(t)")
plt.title("Espacio fase – Sistema 2D")
plt.legend()
plt.grid()
plt.show()

# Evolución temporal
plt.figure()
plt.plot(t, x_rk2, label="x(t) RK2")
plt.plot(t, x_rk4, label="x(t) RK4")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("Evolución temporal de x(t)")
plt.legend()
plt.grid()
plt.show()

