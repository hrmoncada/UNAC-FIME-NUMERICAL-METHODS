import numpy as np
import matplotlib.pyplot as plt

# ==============================
# Sistema 2D
# dx/dt = -y
# dy/dt = x
# ==============================
def f(state):
    x, y = state
    return np.array([-y, x])

# Parámetros
dt = 0.1
T = 10
N = int(T / dt)

# Condición inicial
x0 = np.array([1.0, 0.0])

# ==============================
# Euler Forward
# ==============================
xf = np.zeros((N + 1, 2))
xf[0] = x0

for n in range(N):
    xf[n + 1] = xf[n] + dt * f(xf[n])

# ==============================
# Euler Backward (implícito)
# (I - dtA) x_{n+1} = x_n
# ==============================
xb = np.zeros((N + 1, 2))
xb[0] = x0

A = np.array([[1, dt],
              [-dt, 1]])
A_inv = np.linalg.inv(A)

for n in range(N):
    xb[n + 1] = A_inv @ xb[n]

# ==============================
# Euler Centered (Leapfrog)
# ==============================
xc = np.zeros((N + 1, 2))
xc[0] = x0
xc[1] = xc[0] + dt * f(xc[0])

for n in range(1, N):
    xc[n + 1] = xc[n - 1] + 2 * dt * f(xc[n])

# ==============================
# Gráficos
# ==============================
plt.figure()
plt.plot(xf[:, 0], xf[:, 1], label="Euler Forward")
plt.plot(xb[:, 0], xb[:, 1], label="Euler Backward")
plt.plot(xc[:, 0], xc[:, 1], label="Euler Centered")
plt.scatter(x0[0], x0[1])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Comparación de métodos de Euler en 2D")
plt.legend()
plt.axis("equal")
plt.grid(True)
plt.show()

