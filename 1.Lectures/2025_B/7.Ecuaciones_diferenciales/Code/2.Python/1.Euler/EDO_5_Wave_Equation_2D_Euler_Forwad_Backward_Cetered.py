'''
A continuación te dejo un programa completo en Python, claramente documentado, que resuelve la ecuación de onda en 2D:

u_{tt} = c^2 (u_{xx} + u_{yy})
	​
utilizando tres esquemas temporales:

Euler Forward (Explícito)
Euler Backward (Implícito)
Esquema Centrado en Tiempo (Leap–Frog / Staggered)

El código usa diferencias finitas en espacio, condiciones de frontera de Dirichlet (u = 0) y produce gráficos animados.
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve

"""
===========================================================================
         2D WAVE EQUATION SOLVER (u_tt = c^2 * (u_xx + u_yy))
         Methods: Euler Forward, Euler Backward, Centered (Leapfrog)
         Author: ChatGPT
         Fully documented for teaching and research.
===========================================================================

Spatial PDE:
        u_tt = c^2 (u_xx + u_yy)

Boundary conditions:
        Dirichlet: u = 0 on all boundaries.

Initial conditions:
        u(x,y,0) = Gaussian pulse
        u_t(x,y,0) = 0

Available time-integration schemes:
        - euler_forward()
        - euler_backward()
        - centered_scheme()

===========================================================================
"""

# ================================================================
# PARAMETERS
# ================================================================
Lx, Ly = 1.0, 1.0          # domain size
Nx, Ny = 80, 80            # grid resolution
dx, dy = Lx/(Nx-1), Ly/(Ny-1)
c = 1.0                    # wave speed
T = 2.0                    # final time
dt = 0.4 * min(dx, dy)/c   # CFL safe step
Nt = int(T/dt)

x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y, indexing="ij")

# ================================================================
# INITIAL CONDITION: Gaussian pulse
# ================================================================
def initial_condition():
    u0 = np.exp(-200 * ((X-0.5)**2 + (Y-0.5)**2))
    ut0 = np.zeros_like(u0)
    return u0, ut0

# ================================================================
# LAPLACIAN OPERATOR
# ================================================================
def laplacian(u):
    """Compute 2D Laplacian with central differences."""
    lap = np.zeros_like(u)
    lap[1:-1, 1:-1] = (
        (u[2:, 1:-1] - 2*u[1:-1, 1:-1] + u[:-2, 1:-1]) / dx**2 +
        (u[1:-1, 2:] - 2*u[1:-1, 1:-1] + u[1:-1, :-2]) / dy**2
    )
    return lap

# ================================================================
# 1) EULER FORWARD (Explicit)
# ================================================================
def euler_forward():
    print("Running Euler Forward...")
    u, ut = initial_condition()
    frames = []

    for n in range(Nt):
        utt = c**2 * laplacian(u)
        ut = ut + dt * utt
        u = u + dt * ut

        # Dirichlet boundaries
        u[0,:] = u[-1,:] = u[:,0] = u[:,-1] = 0

        if n % 10 == 0:
            frames.append(u.copy())

    return frames

# ================================================================
# 2) CENTERED (Leapfrog in time)
# ================================================================
def centered_scheme():
    print("Running Centered Scheme...")
    u0, ut0 = initial_condition()

    # First step (using Euler forward just to start)
    u1 = u0 + dt * ut0 + 0.5 * (c**2) * dt**2 * laplacian(u0)

    u_prev = u0
    u = u1
    frames = [u0]

    for n in range(1, Nt):
        lap = laplacian(u)
        u_next = 2*u - u_prev + (c**2)*(dt**2)*lap

        u_next[0,:] = u_next[-1,:] = u_next[:,0] = u_next[:,-1] = 0

        u_prev, u = u, u_next

        if n % 10 == 0:
            frames.append(u.copy())

    return frames

# ================================================================
# 3) EULER BACKWARD (Implicit)
# ================================================================
def euler_backward():
    print("Running Euler Backward... (slow but unconditionally stable)")

    N = Nx * Ny

    # Coefficients for implicit matrix
    ax = c**2 * dt / dx**2
    ay = c**2 * dt / dy**2

    main = np.ones(N) * (1 + 2*ax + 2*ay)
    offx = np.ones(N-1) * (-ax)
    offy = np.ones(N-Nx) * (-ay)

    # Zero out row jumps (avoid wrap-around)
    for i in range(1, Ny):
        offx[i*Nx - 1] = 0

    A = diags([main, offx, offx, offy, offy], [0, -1, 1, -Nx, Nx])

    u, ut = initial_condition()
    frames = []

    for n in range(Nt):
        b = u.flatten() + dt * ut.flatten()
        u_new = spsolve(A, b)
        u = u_new.reshape((Nx, Ny))

        u[0,:] = u[-1,:] = u[:,0] = u[:,-1] = 0

        if n % 10 == 0:
            frames.append(u.copy())

    return frames

# ================================================================
# PLOT ANIMATION
# ================================================================
def animate(frames, title):
    fig = plt.figure(figsize=(6,5))
    ax = fig.add_subplot(111)

    img = ax.imshow(frames[0], cmap="viridis",
                    extent=[0, Lx, 0, Ly], origin="lower")
    ax.set_title(title)
    fig.colorbar(img)

    def update(i):
        img.set_data(frames[i])
        ax.set_title(f"{title} (frame {i})")
        return img,

    anim = FuncAnimation(fig, update, frames=len(frames), interval=50)
    plt.show()

# ================================================================
# RUN ALL METHODS
# ================================================================
frames1 = euler_forward()
frames2 = centered_scheme()
frames3 = euler_backward()

animate(frames1, "2D Wave — Euler Forward")
animate(frames2, "2D Wave — Centered (Leapfrog)")
animate(frames3, "2D Wave — Euler Backward (Implicit)")

