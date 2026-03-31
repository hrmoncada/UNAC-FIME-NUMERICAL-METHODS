'''
Aquí tienes dos programas completos en Python para resolver la ecuación de calor en 2D usando:

✅ Runge–Kutta de 2° orden (RK2 / Heun)
✅ Runge–Kutta de 4° orden (RK4)

Ambos usan diferencias finitas centrales en espacio y condiciones de frontera fijas (Dirichlet).
Incluyo documentación en cada parte del código y gráficas en 2D.

✅ Ecuación de Calor 2D

Resolviendo:

u_{t} = \alpha (u_{xx} + u_{yy})

en un dominio rectangular (x,y) \in [0,L] x [0,L].
'''
import numpy as np
import matplotlib.pyplot as plt

# ================================================================
# 2D Heat Equation using RK2 (Heun)
# u_t = α ( u_xx + u_yy )
# ================================================================

def laplacian(u, dx, dy):
    """Compute 2D Laplacian using central differences."""
    return (
        (u[2:, 1:-1] - 2 * u[1:-1, 1:-1] + u[:-2, 1:-1]) / dx**2 +
        (u[1:-1, 2:] - 2 * u[1:-1, 1:-1] + u[1:-1, :-2]) / dy**2
    )

def rk2_heat(u, alpha, dx, dy, dt):
    """Runge–Kutta 2 (Heun) time step."""
    Lu = laplacian(u, dx, dy)
    u_pred = u.copy()
    u_pred[1:-1, 1:-1] += dt * alpha * Lu

    Lu_pred = laplacian(u_pred, dx, dy)
    u[1:-1, 1:-1] += dt * 0.5 * alpha * (Lu + Lu_pred)
    return u

# ---------------------
# Grid parameters
# ---------------------
Lx, Ly = 1.0, 1.0
Nx, Ny = 101, 101
dx, dy = Lx/(Nx-1), Ly/(Ny-1)
alpha = 0.01
dt = 0.25 * min(dx, dy)**2 / alpha   # Stability condition
steps = 200

# ---------------------
# Initial Condition
# ---------------------
u = np.zeros((Nx, Ny))
# Gaussian hot spot in center
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y, indexing='ij')
u = np.exp(-50 * ((X-0.5)**2 + (Y-0.5)**2))

# ---------------------
# Time integration
# ---------------------
for n in range(steps):
    u = rk2_heat(u, alpha, dx, dy, dt)

# ---------------------
# Plot final result
# ---------------------
plt.figure(figsize=(6,5))
plt.imshow(u.T, origin='lower', extent=[0, Lx, 0, Ly])
plt.colorbar(label='Temperature')
plt.title("2D Heat Equation — RK2")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

