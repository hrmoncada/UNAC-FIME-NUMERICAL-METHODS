'''
A continuación te dejo un programa completo en Python, claramente documentado en español, que resuelve la ecuación de onda 2D:

u_{tt} = c^2 (u_{xx} + u_{yy})

usando método de Runge–Kutta de 2.º orden (RK2) y Runge–Kutta de 4.º orden (RK4)
bajo condiciones de frontera fijas (Dirichlet) y malla uniforme.

Incluye:

✔ Definición de la malla
✔ Discretización de derivadas espaciales (método de diferencias finitas)
✔ Implementación de RK2 y RK4
✔ Animación 2D con matplotlib
✔ Comentarios detallados línea por línea
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ============================================
#  ECUACIÓN DE ONDA 2D: u_tt = c^2 (u_xx + u_yy)
#  Implementación con RK2 y RK4 explícitos
# ============================================

# Parámetros físicos y espaciales
Lx = 1.0
Ly = 1.0
Nx = 101
Ny = 101
dx = Lx / (Nx-1)
dy = Ly / (Ny-1)

c = 1.0   # velocidad de onda
dt = 0.4 * min(dx,dy) / c   # Condición CFL para estabilidad

T_final = 1.5

# ================================
#  Inicializando la malla
# ================================
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)

# Campo principal
u = np.zeros((Ny, Nx))
u_t = np.zeros((Ny, Nx))    # velocidad

# ================================
#  Condición inicial
#  Un pulso gaussiano en el centro
# ================================
u0 = np.exp(-200 * ((X - 0.5)**2 + (Y - 0.5)**2))
u[:] = u0.copy()


# =========================================================
# Operador Laplaciano con diferencias finitas 2º orden
# =========================================================
def laplacian(U):
    L = np.zeros_like(U)
    L[1:-1, 1:-1] = (
        (U[2:,1:-1] - 2*U[1:-1,1:-1] + U[:-2,1:-1]) / dx**2 +
        (U[1:-1,2:] - 2*U[1:-1,1:-1] + U[1:-1,:-2]) / dy**2
    )
    return L


# =========================================================
#  RHS del sistema de primer orden
#  u_t = v
#  v_t = c^2 ∇²u
# =========================================================
def rhs(u, v):
    return v, c**2 * laplacian(u)


# =========================================================
# MÉTODO RUNGE–KUTTA DE 2º ORDEN (RK2 / midpoint)
# =========================================================
def rk2(u, v):
    du1, dv1 = rhs(u, v)
    u_mid = u + 0.5 * dt * du1
    v_mid = v + 0.5 * dt * dv1

    du2, dv2 = rhs(u_mid, v_mid)

    u_new = u + dt * du2
    v_new = v + dt * dv2

    return u_new, v_new


# =========================================================
# MÉTODO RUNGE–KUTTA DE 4º ORDEN (RK4)
# =========================================================
def rk4(u, v):
    du1, dv1 = rhs(u, v)

    du2, dv2 = rhs(u + 0.5*dt*du1, v + 0.5*dt*dv1)
    du3, dv3 = rhs(u + 0.5*dt*du2, v + 0.5*dt*dv2)

    du4, dv4 = rhs(u + dt*du3, v + dt*dv3)

    u_new = u + dt*(du1 + 2*du2 + 2*du3 + du4)/6
    v_new = v + dt*(dv1 + 2*dv2 + 2*dv3 + dv4)/6

    return u_new, v_new


# =========================================================
# Seleccionar método: rk2 o rk4
# =========================================================
use_method = "rk4"   # cambiar a "rk2" si deseas

if use_method == "rk2":
    step = rk2
    print("Usando Runge-Kutta de 2do orden (RK2)")
else:
    step = rk4
    print("Usando Runge-Kutta de 4to orden (RK4)")


# =========================================================
# ANIMACIÓN
# =========================================================
fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(u, cmap="turbo", origin="lower", extent=[0,Lx,0,Ly])
ax.set_title("Ecuación de Onda 2D")
fig.colorbar(im)

def update(frame):
    global u, u_t
    u, u_t = step(u, u_t)

    # Condiciones de frontera fijas
    u[0,:] = u[-1,:] = u[:,0] = u[:,-1] = 0

    im.set_data(u)
    ax.set_title(f"t = {frame*dt:.3f} s")
    return [im]

ani = FuncAnimation(fig, update, frames=int(T_final/dt), interval=30)
plt.show()

