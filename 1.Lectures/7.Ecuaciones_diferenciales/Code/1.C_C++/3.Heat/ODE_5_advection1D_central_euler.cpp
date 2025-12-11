/* advection1D_central_euler.cpp — 1D Forward Euler en tiempo + central en espacio (advección)
Compila con g++:

g++ -O2 ODE_5_advection1D_central_euler.cpp -o adv1D && ./adv1D

Abre los CSV generados con Python/matplotlib o Excel.

Esquema: forward Euler en tiempo, diferencia central en espacio para la ecuación de advección lineal: u_t + c u_x = 0
 u_i^{n+1} = u_i^n - c*dt/(2dx) * (u_{i+1} - u_{i-1})

Produce archivo "u1d_advection_central.csv" Usa un script simple de Python  para leer el CSV y graficar:
python plot_5_ODE_advection1D_central_euler.py

ADVERTENCIA: este esquema es generalmente inestable para advección pura (es neutrally unstable / dispersive). Se muestra aquí por instrucción didáctica.
*/
#include <bits/stdc++.h>
using namespace std;

int main(){
    const double c = 1.0;      // velocidad de advección
    const double L = 1.0;
    const int N = 201;
    const double dx = L/(N-1);
    // CFL (para estabilidad aproximada con central scheme): |c| * dt / dx <= 1 (pero central+FE puede ser instable)
    double dt = 0.4 * dx / fabs(c); // prudente
    const double t_final = 0.5;
    int nsteps = int(t_final/dt) + 1;

    vector<double> u(N,0.0), u_new(N,0.0);

    // condición inicial: pulso gaussiano centrado en x=0.25
    for(int i=0;i<N;i++){
        double x = i*dx;
        u[i] = exp(-200.0*(x-0.25)*(x-0.25));
    }
    // Usaremos condiciones de frontera periódicas para demo
    for(int n=0;n<nsteps;n++){
        for(int i=1;i<N-1;i++){
            u_new[i] = u[i] - c * dt/(2.0*dx) * (u[i+1] - u[i-1]);
        }
        // periodic BC
        u_new[0] = u[0] - c*dt/(2.0*dx)*(u[1]-u[N-2]);
        u_new[N-1] = u_new[0]; // si deseas guardar periodicidad en nodo final
        u.swap(u_new);
    }

    ofstream fout("u1d_advection_central.csv");
    for(int i=0;i<N;i++){
        fout << u[i];
        if(i<N-1) fout << ",";
    }
    fout << "\n";
    fout.close();
    cout << "1D advection (central+forward) finished. Output: u1d_advection_central.csv\n";
    return 0;
}

