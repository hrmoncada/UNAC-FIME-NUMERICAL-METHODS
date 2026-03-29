/* Heat1D_forward_euler.cpp — 1D Euler Forward (explícito) para difusión (FTCS)
Vompila con g++:

g++ -O2 ODE_4_Heat1D_forward_euler.cpp -o heat1D && ./heat1D

Abre los CSV generados con Python/matplotlib o Excel.
Forward Euler (explícito) para la ecuación del calor 1D:
    u_t = alpha * u_xx
Esquema FTCS: u_i^{n+1} = u_i^n + alpha*dt*(u_{i+1}-2u_i+u_{i-1})/dx^2
Produce archivo "u1d_euler_forward.csv" con la solución final.

Usa un script simple de Python  para leer el CSV y graficar:
plot_1_ODE_1D_Forward_Euler.py
*/
#include <bits/stdc++.h>
using namespace std;

int main(){
    const double alpha = 1.0;
    const double L = 1.0;
    const int N = 201; // puntos
    const double dx = L/(N-1);
    const double dx2 = dx*dx;

    // estabilidad: dt <= dx^2 / (2*alpha)
    double dt = 0.9 * dx2 / (2.0*alpha);
    const double t_final = 0.1;
    int nsteps = int(t_final/dt) + 1;

    vector<double> u(N,0.0), u_new(N,0.0);

    // condición inicial: gaussiana
    for(int i=0;i<N;i++){
        double x = i*dx - L/2.0 + 0.5*L; // centrada en 0.5
        u[i] = exp(-200.0*(x-0.5)*(x-0.5));
    }
    // condiciones de frontera Dirichlet (u=0)
    u[0] = u[N-1] = 0.0;

    for(int n=0;n<nsteps;n++){
        for(int i=1;i<N-1;i++){
            u_new[i] = u[i] + alpha*dt*(u[i+1]-2.0*u[i]+u[i-1])/dx2;
        }
        // fronteras fijas
        u_new[0] = 0.0; u_new[N-1]=0.0;
        u.swap(u_new);
    }

    ofstream fout("u1d_euler_forward.csv");
    for(int i=0;i<N;i++){
        fout << u[i];
        if(i<N-1) fout << ",";
    }
    fout << "\n";
    fout.close();
    cout << "1D forward-euler finished. Output: u1d_euler_forward.csv\n";
    return 0;
}

