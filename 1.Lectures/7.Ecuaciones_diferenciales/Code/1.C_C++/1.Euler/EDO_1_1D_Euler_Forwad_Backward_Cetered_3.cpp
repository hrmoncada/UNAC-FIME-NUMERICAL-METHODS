/*==============================
 Sistema 1D
 du/dt = -lambda u
 u(0) = u0
==============================
Compilar
g++ EDO_1_1D_Euler_Forwad_Backward_Cetered_2.cpp -o euler
Executar
./euler
plot
python plot_1_ODE_1D_Euler_Forward_Backward_Centered_3.py

*/
#include <iostream>
#include <fstream>
#include <cmath>

int main() {

    // Parameters
    double lambda = 1.0;
    double u0 = 1.0;
    double dt = 0.1;
    double T = 5.0;
    int N = T / dt;

    // Arrays
    double u_forward[N+1];
    double u_backward[N+1];
    double u_center[N+1];
    double time[N+1];

    // Initial conditions
    u_forward[0]  = u0;
    u_backward[0] = u0;
    u_center[0]   = u0;
    time[0] = 0.0;

    // =====================
    // Euler Forward & Backward
    // =====================
    for (int n = 0; n < N; n++) {
        time[n+1] = time[n] + dt;

        // Euler Forward
        u_forward[n+1] = u_forward[n] - dt * lambda * u_forward[n];

        // Euler Backward
        u_backward[n+1] = u_backward[n] / (1.0 + dt * lambda);
    }

    // =====================
    // Euler Centered
    // =====================
    // First step with Forward Euler
    u_center[1] = u_center[0] - dt * lambda * u_center[0];

    for (int n = 1; n < N; n++) {
        u_center[n+1] = u_center[n-1] - 2.0 * dt * lambda * u_center[n];
    }

    // =====================
    // Save data
    // =====================
    std::ofstream file("euler_data.dat");
    file << "# t forward backward centered exact\n";

    for (int n = 0; n <= N; n++) {
        double exact = u0 * std::exp(-lambda * time[n]);
        file << time[n] << " "
             << u_forward[n] << " "
             << u_backward[n] << " "
             << u_center[n] << " "
             << exact << "\n";
    }

    file.close();

    std::cout << "Data saved to euler_data.dat\n";
    return 0;
}

