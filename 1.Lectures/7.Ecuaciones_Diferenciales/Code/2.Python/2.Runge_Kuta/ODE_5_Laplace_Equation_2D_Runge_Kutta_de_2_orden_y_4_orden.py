'''
A continuación te presento un programa completo y documentado en Python para resolver la ecuación de Laplace en 2D en una malla rectangular usando un enfoque de evolución ficticia en el tiempo:

\frac{\partial u}{\partial t} = \nabla^2 u_{i,j}

Cuando el sistema converge al estado estacionario (∂\frac{\partial u}{\partial t} = 0), se obtiene la ecuación de Laplace:

 \nabla^2 u_{i,j} = 0

Este enfoque permite usar Runge–Kutta de 2.º y 4.º orden en el “tiempo numérico”, algo común en métodos de relajación avanzados.

📌 Planteamiento del problema

Dominio 2D:  [0,L] x [0,L]

Discretización espacial: diferencias finitas de segundo orden

Condiciones de frontera (ejemplo):
u(x,0)=0
u(x,L)=100
u(0,y)=0
u(L,y)=0

🔢 Operador Laplaciano (diferencias finitas)

Discretización (mallado uniforme):

\nabla^2 u_{i,j} = \frac{u_{i+1,j} - 2u_{i,j} + u_{i-1,j}}{\Delta x^2} + \frac{u_{i,j+1} - 2u_{i,j} + u_{i,j-1}}{\Delta y^2}  = 0

\Delta x = \Delta y

u_{i,j}  = \frac{1}{4} * [ u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1} ]
'''

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Parámetros del dominio
# ============================================================
Lx, Ly = 1.0, 1.0          # Tamaño del dominio
Nx, Ny = 50, 50            # Número de nodos
dx = Lx / (Nx - 1)
dy = Ly / (Ny - 1)

# Paso de tiempo ficticio
dt = 0.25 * min(dx, dy)**2

# Número de iteraciones
nt = 3000

# ============================================================
# Inicialización del campo
# ============================================================
u = np.zeros((Nx, Ny))

# Condiciones de frontera
u[:, -1] = 100.0    # frontera superior
u[:,  0] = 0.0
u[ 0, :] = 0.0
u[-1, :] = 0.0

# ============================================================
# Laplaciano 2D por diferencias finitas
# ============================================================
def laplacian(u):
    lap = np.zeros_like(u)
    lap[1:-1,1:-1] = (
        (u[2:,1:-1] - 2*u[1:-1,1:-1] + u[:-2,1:-1]) / dx**2 +
        (u[1:-1,2:] - 2*u[1:-1,1:-1] + u[1:-1,:-2]) / dy**2
    )
    return lap

# ============================================================
# RK2 (Heun)
# ============================================================
def solve_RK2(u):
    for n in range(nt):
        k1 = laplacian(u)
        u_tmp = u + dt * k1
        k2 = laplacian(u_tmp)
        u += dt * 0.5 * (k1 + k2)
    return u

# ============================================================
# RK4
# ============================================================
def solve_RK4(u):
    for n in range(nt):
        k1 = laplacian(u)
        k2 = laplacian(u + 0.5 * dt * k1)
        k3 = laplacian(u + 0.5 * dt * k2)
        k4 = laplacian(u + dt * k3)
        u += dt * (k1 + 2*k2 + 2*k3 + k4) / 6.0
    return u


# ============================================================
# Resolver con RK4 (cambiar a solve_RK2 si se desea)
# ============================================================
u_final2 = solve_RK2(u.copy())
u_final4 = solve_RK4(u.copy())

Error = np.abs(u_final4 - u_final2)

# ============================================================
# Gráfica de la solución
# ============================================================
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y, indexing='ij')

# ============================================================
# plot con RK4
# ============================================================
plt.figure(1, figsize=(6,5))
cp = plt.contourf(X, Y, u_final2, 50, cmap='inferno')
plt.colorbar(cp, label='Potencial u(x,y)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ecuación de Laplace 2D – RK2')
plt.tight_layout()

# ============================================================
# plot con RK4
# ============================================================
plt.figure(2, figsize=(6,5))
cp = plt.contourf(X, Y, u_final4, 50, cmap='inferno')
plt.colorbar(cp, label='Potencial u(x,y)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ecuación de Laplace 2D – RK4')
plt.tight_layout()

# ============================================================
# plot Error
# ============================================================
plt.figure(3, figsize=(6,5))
cp = plt.contourf(X, Y, Error, 50, cmap='inferno')
plt.colorbar(cp, label='Error')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Error')
plt.tight_layout()

plt.show()

