/*==============================
 Sistema 1D
 du/dt = -lambda u
 u(0) = u0
==============================
g++ EDO_1_1D_Euler_Forwad_Backward_Cetered_2.cpp -o euler1d
./euler1d

*/

#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

// Parámetros del problema
const double lambda = 1.0;   // coeficiente
const double u0 = 1.0;       // condición inicial
const double dt = 0.1;       // paso temporal
const int N = 20;            // número de pasos

// Euler Forward (Explícito)
vector<double> euler_forward() {
    vector<double> u(N+1);
    u[0] = u0;
    for (int n = 0; n < N; n++) {
        u[n+1] = u[n] - dt * lambda * u[n];
    }
    return u;
}

// Euler Backward (Implícito)
vector<double> euler_backward() {
    vector<double> u(N+1);
    u[0] = u0;
    for (int n = 0; n < N; n++) {
        u[n+1] = u[n] / (1.0 + dt * lambda);
    }
    return u;
}

// Euler Center (Crank–Nicolson)
vector<double> euler_center() {
    vector<double> u(N+1);
    u[0] = u0;
    double factor = (1.0 - 0.5 * dt * lambda) / (1.0 + 0.5 * dt * lambda);
    for (int n = 0; n < N; n++) {
        u[n+1] = factor * u[n];
    }
    return u;
}

// Solución exacta
double exact(double t) {
    return u0 * exp(-lambda * t);
}

int main() {

    auto uF = euler_forward();
    auto uB = euler_backward();
    auto uC = euler_center();

    cout << fixed << setprecision(6);
    cout << " n     t       Euler-F     Euler-B     Euler-C     Exact\n";
    cout << "-----------------------------------------------------------\n";

    for (int n = 0; n <= N; n++) {
        double t = n * dt;
        cout << setw(2) << n << "  "
             << setw(6) << t << "  "
             << setw(10) << uF[n] << "  "
             << setw(10) << uB[n] << "  "
             << setw(10) << uC[n] << "  "
             << setw(10) << exact(t) << "\n";
    }

    return 0;
}

