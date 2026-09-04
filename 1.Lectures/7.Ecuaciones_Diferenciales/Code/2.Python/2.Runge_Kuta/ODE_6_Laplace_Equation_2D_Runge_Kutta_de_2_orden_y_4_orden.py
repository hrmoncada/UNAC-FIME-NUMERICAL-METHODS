'''
A continuación te presento un programa completo y documentado en Python para resolver la ecuación de Laplace en 2D

\nabla^2 \phi(x,y) = 0

usando una formulación pseudo–temporal y los métodos de Runge–Kutta de segundo orden (RK2) y cuarto orden (RK4), de modo que la solución converge al estado estacionario:

\phi(x,y)  = \sin(x)\sinh(y)

Esta técnica es estándar en métodos numéricos cuando se quiere aplicar esquemas RK a ecuaciones elípticas.

1. Idea del método: Introducimos un tiempo ficticio t:

\frac{\partial \phi}{\partial t} = \nabla^2 \phi(x,y) 

Cuando t -> \infty, la solución converge a la solución estacionaria de Laplace.

2. Condiciones del problema

Dominio: x \in [0,\pi], y \in [0,1]

Solución analítica (para validación): \phi(x,y) = \sin(x) \sinh(y)

Condiciones de frontera (Dirichlet):
\phi(x,0) = 0
\phi(x,1) = \sin(x) \sinh(1)
\phi(0,y) = 0
\phi(\pi,y) = 0

'''
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# Parámetros del dominio
# --------------------------------------------------
Lx = np.pi
Ly = 1.0

Nx, Ny = 50, 50
dx = Lx / (Nx - 1)
dy = Ly / (Ny - 1)

x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y, indexing="ij")

# Paso de tiempo pseudo-temporal
dt = 0.25 * min(dx, dy)**2
nsteps = 5000

# --------------------------------------------------
# Solución exacta
# --------------------------------------------------
phi_exact = np.sin(X) * np.sinh(Y)

# --------------------------------------------------
# Laplaciano por diferencias finitas
# --------------------------------------------------
def laplacian(phi):
    lap = np.zeros_like(phi)
    lap[1:-1, 1:-1] = (
        (phi[2:,1:-1] - 2*phi[1:-1,1:-1] + phi[:-2,1:-1]) / dx**2 +
        (phi[1:-1,2:] - 2*phi[1:-1,1:-1] + phi[1:-1,:-2]) / dy**2
    )
    return lap

# --------------------------------------------------
# Aplicar condiciones de frontera
# --------------------------------------------------
def apply_bc(phi):
    phi[:, 0]  = 0.0
    phi[:, -1] = np.sin(x) * np.sinh(1)
    phi[0, :]  = 0.0
    phi[-1, :] = 0.0
    return phi

# --------------------------------------------------
# Runge–Kutta de segundo orden (Heun)
# --------------------------------------------------
def solve_RK2():
    phi = np.zeros((Nx, Ny))
    phi = apply_bc(phi)

    for _ in range(nsteps):
        k1 = laplacian(phi)
        k2 = laplacian(phi + dt * k1)
        phi += 0.5 * dt * (k1 + k2)
        phi = apply_bc(phi)

    return phi

# --------------------------------------------------
# Runge–Kutta de cuarto orden
# --------------------------------------------------
def solve_RK4():
    phi = np.zeros((Nx, Ny))
    phi = apply_bc(phi)

    for _ in range(nsteps):
        k1 = laplacian(phi)
        k2 = laplacian(phi + 0.5 * dt * k1)
        k3 = laplacian(phi + 0.5 * dt * k2)
        k4 = laplacian(phi + dt * k3)
        phi += dt / 6.0 * (k1 + 2*k2 + 2*k3 + k4)
        phi = apply_bc(phi)

    return phi

# --------------------------------------------------
# Resolver
# --------------------------------------------------
phi_RK2 = solve_RK2()
phi_RK4 = solve_RK4()

# --------------------------------------------------
# Errores
# --------------------------------------------------
err_RK2 = np.linalg.norm(phi_RK2 - phi_exact)
err_RK4 = np.linalg.norm(phi_RK4 - phi_exact)

print("Error RK2 =", err_RK2)
print("Error RK4 =", err_RK4)

# --------------------------------------------------
# Gráficas
# --------------------------------------------------
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.title("Solución exacta")
plt.contourf(X, Y, phi_exact, 50)
plt.colorbar()

plt.subplot(1,3,2)
plt.title("RK2")
plt.contourf(X, Y, phi_RK2, 50)
plt.colorbar()

plt.subplot(1,3,3)
plt.title("RK4")
plt.contourf(X, Y, phi_RK4, 50)
plt.colorbar()

plt.tight_layout()
plt.show()

