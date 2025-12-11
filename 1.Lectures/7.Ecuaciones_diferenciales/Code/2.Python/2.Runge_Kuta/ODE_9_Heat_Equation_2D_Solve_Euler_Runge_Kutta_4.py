'''==============================
 Sistema 2D
 du/dt = alpha * (d^2u/dx^2 + d^2u/dy^2 )
 (x, y) \in [0,L] x [0,L] 
Condiciones de frontera: Dirichlet u = 0
Condición inicial: u(x,y,0) = sin(\pi x)sin( \pi y)
==============================
Compilar
python ODE_5_2D_Heat_Equation_Solve_Euler_Runge_Kutta_4.py
'''
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Parámetros físicos y numéricos
# -----------------------------
alpha = 1.0          # difusividad térmica
Lx, Ly = 1.0, 1.0    # tamaño del dominio
Nx, Ny = 30, 30      # puntos de la malla
dx = Lx / (Nx - 1)
dy = Ly / (Ny - 1)
dt = 0.0005          # paso temporal
nt = 200             # número de pasos de tiempo

# Condición de estabilidad (Euler explícito)
if dt > min(dx**2, dy**2) / (4 * alpha):
    raise ValueError("dt es demasiado grande (condición de estabilidad violada)")

# -----------------------------
# Malla 2D
# -----------------------------
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)

# -----------------------------
# Condición inicial
# -----------------------------
def initial_condition(X, Y):
    return np.exp(-50 * ((X - 0.5)**2 + (Y - 0.5)**2))

u0 = initial_condition(X, Y)

# -----------------------------
# Operador Laplaciano (diferencias finitas)
# -----------------------------
def laplacian(u):
    return (
        (np.roll(u, -1, axis=0) - 2*u + np.roll(u, 1, axis=0)) / dx**2 +
        (np.roll(u, -1, axis=1) - 2*u + np.roll(u, 1, axis=1)) / dy**2
    )

# -----------------------------
# Método de Euler explícito
# -----------------------------
u_euler = u0.copy()

for _ in range(nt):
    u_euler += dt * alpha * laplacian(u_euler)

# -----------------------------
# Método de Runge–Kutta de orden 4
# -----------------------------
u_rk4 = u0.copy()

for _ in range(nt):
    k1 = alpha * laplacian(u_rk4)
    k2 = alpha * laplacian(u_rk4 + 0.5 * dt * k1)
    k3 = alpha * laplacian(u_rk4 + 0.5 * dt * k2)
    k4 = alpha * laplacian(u_rk4 + dt * k3)

    u_rk4 += (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

# -----------------------------
# Gráficas
# -----------------------------
plt.figure()
plt.contourf(X, Y, u0, levels=50)
plt.title("Condición inicial")
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar()
plt.show()

plt.figure()
plt.contourf(X, Y, u_euler, levels=50)
plt.title("Ecuación del calor 2D – Euler explícito")
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar()
plt.show()

plt.figure()
plt.contourf(X, Y, u_rk4, levels=50)
plt.title("Ecuación del calor 2D – Runge–Kutta 4")
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar()
plt.show()

