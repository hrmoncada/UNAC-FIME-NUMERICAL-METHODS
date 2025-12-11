'''
A continuación tienes un programa completo y documentado en Python para resolver la ecuación de Laplace en 2D

\nabla^2 \phi =  0

sobre una malla bidimensional usando diferencias finitas y métodos iterativos tipo Euler:

✅ Forward Euler (explícito) – método de Jacobi
✅ Backward Euler (implícito) – formulado como Gauss–Seidel
✅ Esquema centrado – operador Laplaciano clásico de 5 puntos

Discretización (mallado uniforme):

\nabla^2 u_{i,j} = \frac{u_{i+1,j} - 2u_{i,j} + u_{i-1,j}}{\Delta x^2} + \frac{u_{i,j+1} - 2u_{i,j} + u_{i,j-1}}{\Delta y^2}  = 0

\Delta x = \Delta y

u_{i,j}  = \frac{1}{4} * [ u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1} ]

'''

import numpy as np
import matplotlib.pyplot as plt

# ==============================
# Parámetros del dominio
# ==============================
Nx, Ny = 50, 50          # Número de nodos
Lx, Ly = 1.0, 1.0        # Dimensiones físicas

dx = Lx / (Nx - 1)
dy = Ly / (Ny - 1)

max_iter = 5000
tolerance = 1e-6

# ==============================
# Inicialización del campo
# ==============================
phi = np.zeros((Nx, Ny))

# Condiciones de frontera (Dirichlet)
phi[:, -1] = 1.0   # Borde superior caliente
phi[:, 0]  = 0.0
phi[0, :]  = 0.0
phi[-1, :] = 0.0

# ==============================
# Método de Jacobi (Euler Forward)
# ==============================
def laplace_jacobi(phi):
    phi_new = phi.copy()
    for it in range(max_iter):
        phi_old = phi_new.copy()

        for i in range(1, Nx-1):
            for j in range(1, Ny-1):
                phi_new[i, j] = 0.25 * (
                    phi_old[i+1, j] +
                    phi_old[i-1, j] +
                    phi_old[i, j+1] +
                    phi_old[i, j-1]
                )

        error = np.max(np.abs(phi_new - phi_old))
        if error < tolerance:
            print(f"Jacobi converged in {it} iterations")
            break

    return phi_new


# ==============================
# Método Gauss–Seidel (Euler Backward)
# ==============================
def laplace_gauss_seidel(phi):
    phi_new = phi.copy()
    for it in range(max_iter):

        phi_old = phi_new.copy()

        for i in range(1, Nx-1):
            for j in range(1, Ny-1):
                phi_new[i, j] = 0.25 * (
                    phi_new[i+1, j] +
                    phi_new[i-1, j] +
                    phi_new[i, j+1] +
                    phi_new[i, j-1]
                )

        error = np.max(np.abs(phi_new - phi_old))
        if error < tolerance:
            print(f"Gauss-Seidel converged in {it} iterations")
            break

    return phi_new


# ==============================
# Resolver
# ==============================
phi_jacobi = laplace_jacobi(phi)
phi_gs = laplace_gauss_seidel(phi)

# ==============================
# Gráficos
# ==============================
def plot_solution(phi, title):
    plt.figure(figsize=(6, 5))
    plt.contourf(phi, 50, cmap="inferno")
    plt.colorbar(label="φ")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(title)
    plt.tight_layout()
    plt.show()

plot_solution(phi_jacobi, "Laplace 2D – Jacobi (Euler Forward)")
plot_solution(phi_gs, "Laplace 2D – Gauss–Seidel (Euler Backward)")

