/* Heat2D_backward_euler.cpp — 2D Backward Euler (implícito) con Gauss–Seidel
Compila con g++:
g++ -O2 ODE_3_Heat2D_backward_euler.cpp -o heat2D && ./heat2D
Abre los CSV generados con Python/matplotlib o Excel.

Backward Euler implícito para la ecuación de difusión 2D:
    u_t = alpha * (u_xx + u_yy)
Discretización: (I - dt * alpha * L) u^{n+1} = u^n
Se resuelve mediante Gauss-Seidel iterativo (con SOR opcional).

Produce archivo "u2d_tfinal.csv" con la solución final en formato CSV.
Usa un script simple de Python  para leer el CSV y graficar:
plot_2_ODE_2D_Backward_Euler.py
*/
#include <bits/stdc++.h>
using namespace std;

int main(){
    // Parámetros físicos y numéricos
    const double alpha = 1.0;      // difusividad
    const double Lx = 1.0, Ly = 1.0;
    const int Nx = 50, Ny = 50;    // malla (interior + boundaries will be handled)
    const double dx = Lx/(Nx-1);
    const double dy = Ly/(Ny-1);
    const double dt = 0.001;       // paso de tiempo
    const double t_final = 0.1;
    const int maxSteps = int(t_final/dt);

    // Parámetros SOR/Gauss-Seidel
    const int maxIter = 5000;
    const double tol = 1e-6;
    const double omega = 1.0; // omega=1 -> Gauss-Seidel, omega in (1,2) -> SOR

    // coeficientes
    const double rx = alpha*dt/(dx*dx);
    const double ry = alpha*dt/(dy*dy);

    // arrays: u_old = u^n, u = u^{n+1}
    vector<vector<double>> u(Ny, vector<double>(Nx, 0.0));
    vector<vector<double>> u_old = u;

    // Condiciones de frontera (Dirichlet) ejemplo: u=0 en frontera
    for(int j=0;j<Ny;j++){
        for(int i=0;i<Nx;i++){
            // ejemplo: condición inicial con un pico en el centro
            double x = i*dx, y = j*dy;
            double xc = 0.5*Lx, yc = 0.5*Ly;
            double r2 = (x-xc)*(x-xc)+(y-yc)*(y-yc);
            u[j][i] = exp(-200.0*r2); // condición inicial
        }
    }
    u_old = u;

    // Implicit matrix solve per paso: (1 + 2rx + 2ry) u_ij^{n+1} - rx(u_{i+1}+u_{i-1}) - ry(u_{j+1}+u_{j-1}) = u_old_ij
    // Iterative Gauss-Seidel
    for(int step=0; step<maxSteps; ++step){
        // copiar RHS
        // - aplicar condiciones de frontera en u_old (si son constantes, ya están)
        // equivalente a bordes fijos: u at boundaries remain fixed
        // iniciar iteración GS
        int iter = 0;
        double err = 0.0;
        do{
            err = 0.0;
            for(int j=1;j<Ny-1;++j){
                for(int i=1;i<Nx-1;++i){
                    double rhs = u_old[j][i];
                    double diag = 1.0 + 2.0*(rx+ry);
                    double sum = rx*(u[j][i+1] + u[j][i-1]) + ry*(u[j+1][i] + u[j-1][i]);
                    // Gauss-Seidel update (with relaxation)
                    double u_new = (rhs + sum) / diag;
                    // SOR
                    double u_upd = (1.0 - omega)*u[j][i] + omega*u_new;
                    err = max(err, fabs(u_upd - u[j][i]));
                    u[j][i] = u_upd;
                }
            }
            iter++;
            if(iter>maxIter) break;
        } while(err>tol);

        // actualizar antiguo
        u_old = u;
    }

    // Guardar en CSV
    ofstream fout("u2d_tfinal.csv");
    for(int j=0;j<Ny;j++){
        for(int i=0;i<Nx;i++){
            fout << u[j][i];
            if(i < Nx-1) fout << ",";
        }
        fout << "\n";
    }
    fout.close();
    cout << "2D backward-euler finished. Output: u2d_tfinal.csv\n";
    return 0;
}

