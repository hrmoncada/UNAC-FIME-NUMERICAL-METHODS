'''
En la ecuación de Poisson no hay derivadas temporales. Por lo tanto, Euler forward/backward/centrado no son métodos temporales aquí, sino que la discretización correcta es por diferencias finitas centradas en el espacio.
Lo que sí cambia es el método iterativo para resolver el sistema lineal resultante:

✅ “Euler forward” → Jacobi
✅ “Euler backward” → Gauss–Seidel
✅ “Euler centrado” → SOR (relajación centrada)

A continuación te doy un programa bien documentado, didáctico y estándar académico.

2D Poisson Equation

\nabla^2 u(x,y) = f(x,y)

Discretización (mallado uniforme):

\frac{u_{i+1,j} - 2u_{i,j} + u_{i-1,j}}{\Delta x^2} + \frac{u_{i,j+1} - 2u_{i,j} + u_{i,j-1}}{\Delta y^2}  = f_{i,j}
	​
'''

import numpy as np
import matplotlib.pyplot as plt

# ==============================
# Problem setup
# ==============================
Nx, Ny = 51, 51            # Número de nodos
Lx, Ly = 1.0, 1.0          # Dimensiones físicas

dx = Lx / (Nx - 1)
dy = Ly / (Ny - 1)

x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)

# ==============================
# Source term f(x,y)
# ==============================
def source(x, y):
    return np.sin(np.pi * x) * np.sin(np.pi * y)

f = np.zeros((Nx, Ny))
for i in range(Nx):
    for j in range(Ny):
        f[i, j] = source(x[i], y[j])

# Solution array
u = np.zeros((Nx, Ny))

# ========================================
# Boundary conditions (Dirichlet)
# u = 0 on all boundaries (can be changed)
# ========================================

# Iteration parameters
max_iter = 5000
tol = 1e-6

# ========================================
# Jacobi method (Euler forward analogue)
# ========================================
def poisson_jacobi(u, f):
    u_new = u.copy()
    for it in range(max_iter):
        u_old = u_new.copy()
        for i in range(1, Nx - 1):
            for j in range(1, Ny - 1):
                u_new[i, j] = (
                    (u_old[i+1, j] + u_old[i-1, j]) / dx**2 +
                    (u_old[i, j+1] + u_old[i, j-1]) / dy**2 -
                    f[i, j]
                ) / (2/dx**2 + 2/dy**2)

        if np.linalg.norm(u_new - u_old) < tol:
            print(f"Jacobi converged in {it} iterations")
            break

    return u_new

# ==============================
# Gauss–Seidel method (Euler backward)
# ==============================
def poisson_gauss_seidel(u, f):
    for it in range(max_iter):
        u_old = u.copy()
        for i in range(1, Nx - 1):
            for j in range(1, Ny - 1):
                u[i, j] = (
                    (u[i+1, j] + u[i-1, j]) / dx**2 +
                    (u[i, j+1] + u[i, j-1]) / dy**2 -
                    f[i, j]
                ) / (2/dx**2 + 2/dy**2)

        if np.linalg.norm(u - u_old) < tol:
            print(f"Gauss–Seidel converged in {it} iterations")
            break

    return u

# ==============================
# SOR method (Centered / accelerated)
# ==============================
def poisson_sor(u, f, omega=1.8):
    for it in range(max_iter):
        u_old = u.copy()
        for i in range(1, Nx - 1):
            for j in range(1, Ny - 1):
                u_new = (
                    (u[i+1, j] + u[i-1, j]) / dx**2 +
                    (u[i, j+1] + u[i, j-1]) / dy**2 -
                    f[i, j]
                ) / (2/dx**2 + 2/dy**2)

                u[i, j] = (1 - omega)*u[i, j] + omega*u_new

        if np.linalg.norm(u - u_old) < tol:
            print(f"SOR converged in {it} iterations")
            break

    return u

# ==============================
# Solve
# ==============================
u_jacobi = poisson_jacobi(np.zeros_like(u), f)
u_gs = poisson_gauss_seidel(np.zeros_like(u), f)
u_sor = poisson_sor(np.zeros_like(u), f)

# ==============================
# Visualization
# ==============================
fig, ax = plt.subplots(1, 3, figsize=(15, 4))

im0 = ax[0].imshow(u_jacobi.T, origin='lower', cmap='viridis')
ax[0].set_title("Jacobi")
plt.colorbar(im0, ax=ax[0])

im1 = ax[1].imshow(u_gs.T, origin='lower', cmap='viridis')
ax[1].set_title("Gauss–Seidel")
plt.colorbar(im1, ax=ax[1])

im2 = ax[2].imshow(u_sor.T, origin='lower', cmap='viridis')
ax[2].set_title("SOR")
plt.colorbar(im2, ax=ax[2])

plt.tight_layout()
plt.show()

