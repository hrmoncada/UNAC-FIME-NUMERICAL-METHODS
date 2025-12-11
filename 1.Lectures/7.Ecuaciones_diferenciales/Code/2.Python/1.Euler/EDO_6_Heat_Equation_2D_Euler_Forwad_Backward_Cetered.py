'''
Ecuación de Calor 2D

Resolviendo:

u_{t} = \alpha (u_{xx} + u_{yy})

en un dominio rectangular (x,y) \in [0,L] x [0,L].

Aquí tienes un programa completo en Python, documentado paso a paso, que resuelve la ecuación del calor 2D usando tres esquemas en el tiempo:

Euler Forward (explícito)
Euler Backward (implícito)
Esquema Centrado en el tiempo (Crank–Nicolson, semi-implícito)

Incluye:

Discretización en diferencias finitas
Condiciones de frontera de Dirichlet (temperatura fijada)
Documentación detallada
Gráficos 2D de la solución

'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags, kron, identity, csc_matrix
from scipy.sparse.linalg import spsolve

"""
===============================================================
      SOLVER FOR THE 2D HEAT EQUATION USING FINITE DIFFERENCES
===============================================================

PDE:
    u_t = α ( u_xx + u_yy )

Domain:
    (x,y) ∈ [0,Lx] × [0,Ly]

Methods implemented:
    1. Euler Forward (explicit)
    2. Euler Backward (implicit)
    3. Crank–Nicolson (semi-implicit)

Boundary conditions:
    Dirichlet (fixed temperature)

Author: ChatGPT (2025)
---------------------------------------------------------------
"""


# ==============================================================
#  GRID AND INITIAL DATA
# ==============================================================

Lx, Ly = 1.0, 1.0       # domain size
Nx, Ny = 40, 40         # grid size
dx, dy = Lx/(Nx-1), Ly/(Ny-1)

alpha = 0.01            # thermal diffusivity
dt = 0.0005             # time step
T_final = 0.1

Nt = int(T_final/dt)

# Create grid
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)

# Initial condition: Gaussian bump
u0 = np.exp(-40*((x[:,None]-0.5)**2 + (y[None,:]-0.5)**2))


# ==============================================================
#  STENCIL COEFFICIENTS FOR LAPLACIAN
# ==============================================================

rx = alpha * dt / dx**2
ry = alpha * dt / dy**2

# CFL for explicit forward Euler
if rx + ry > 0.5:
    print("Warning: Explicit scheme may be unstable.")


# ==============================================================
#  BUILD 2D LAPLACIAN MATRIX FOR IMPLICIT SOLVERS
# ==============================================================

def build_laplacian_2D(Nx, Ny, dx, dy):
    """Construct sparse Laplacian matrix for 2D grid with Dirichlet BC."""
    # 1D Laplacians
    main_x = -2*np.ones(Nx)
    off_x  = np.ones(Nx-1)
    Lx_1D = diags([off_x, main_x, off_x], [-1, 0, 1]) / dx**2

    main_y = -2*np.ones(Ny)
    off_y  = np.ones(Ny-1)
    Ly_1D = diags([off_y, main_y, off_y], [-1, 0, 1]) / dy**2

    # 2D Laplacian = kron(I, Lx) + kron(Ly, I)
    L2D = kron(identity(Ny), Lx_1D) + kron(Ly_1D, identity(Nx))
    return csc_matrix(L2D)

L = build_laplacian_2D(Nx, Ny, dx, dy)


# ==============================================================
#  FORWARD EULER (EXPLICIT)
# ==============================================================

def heat2D_forward(u):
    """Explicit Euler step for u_t = α ∇²u."""
    un = u.copy()
    for i in range(1, Nx-1):
        for j in range(1, Ny-1):
            un[i,j] = ( u[i,j] 
                       + rx*(u[i+1,j] - 2*u[i,j] + u[i-1,j])
                       + ry*(u[i,j+1] - 2*u[i,j] + u[i,j-1]) )
    return un


# ==============================================================
#  BACKWARD EULER (IMPLICIT)
# ==============================================================

A_backward = identity(Nx*Ny) - alpha*dt*L

def heat2D_backward(u):
    """Implicit Euler using sparse linear solver."""
    b = u.reshape(-1)
    sol = spsolve(A_backward, b)
    return sol.reshape((Nx,Ny))


# ==============================================================
#  CRANK–NICOLSON (CENTRAL IN TIME)
# ==============================================================

A_CN_left  = identity(Nx*Ny) - 0.5*alpha*dt*L
A_CN_right = identity(Nx*Ny) + 0.5*alpha*dt*L

def heat2D_crank_nicolson(u):
    """Crank–Nicolson step."""
    b = (A_CN_right @ u.reshape(-1))
    sol = spsolve(A_CN_left, b)
    return sol.reshape((Nx,Ny))


# ==============================================================
#  RUN SIMULATIONS
# ==============================================================

def run_simulation(u0, method="forward"):
    u = u0.copy()
    for n in range(Nt):
        if method == "forward":
            u = heat2D_forward(u)
        elif method == "backward":
            u = heat2D_backward(u)
        elif method == "cn":
            u = heat2D_crank_nicolson(u)
        else:
            raise ValueError("Unknown method.")
    return u


# ==============================================================
#  RUN & PLOT RESULTS
# ==============================================================

uf = run_simulation(u0, method="forward")
ub = run_simulation(u0, method="backward")
uc = run_simulation(u0, method="cn")

plt.figure(figsize=(15,4))

plt.subplot(1,3,1)
plt.imshow(uf.T, origin='lower', cmap='inferno')
plt.title("Forward Euler")
plt.colorbar()

plt.subplot(1,3,2)
plt.imshow(ub.T, origin='lower', cmap='inferno')
plt.title("Backward Euler")
plt.colorbar()

plt.subplot(1,3,3)
plt.imshow(uc.T, origin='lower', cmap='inferno')
plt.title("Crank–Nicolson")
plt.colorbar()

plt.show()

