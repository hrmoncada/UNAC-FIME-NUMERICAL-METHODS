/*==============================
 Sistema 1D
 dy/dt = -y + sin(t)
 y(0) = 1
==============================
Compilar
g++ ODE_6_1D_Runge_Kutta_2_Runge_Kutta_4.cpp -o runge_kutta
Executar
./runge_kutta
plot
python plot_6_ODE_1D_Runge_Kutta_2_Runge_Kutta_4.py
*/

#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

// Definición de la EDO dy/dt = f(t,y)
double f(double t, double y) {
    return -y + sin(t);
}

// Runge-Kutta de orden 2 (Heun)
double rk2(double t, double y, double h) {
    double k1 = f(t, y);
    double k2 = f(t + h, y + h * k1);
    return y + (h / 2.0) * (k1 + k2);
}

// Runge-Kutta de orden 4
double rk4(double t, double y, double h) {
    double k1 = f(t, y);
    double k2 = f(t + h / 2.0, y + h * k1 / 2.0);
    double k3 = f(t + h / 2.0, y + h * k2 / 2.0);
    double k4 = f(t + h, y + h * k3);
    return y + (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4);
}

int main() {
    double t0 = 0.0;
    double tf = 10.0;
    double y0 = 1.0;
    double h = 0.05;

    ofstream out_rk2("rk2.dat");
    ofstream out_rk4("rk4.dat");

    double t = t0;
    double y2 = y0;
    double y4 = y0;

    while (t <= tf) {
        out_rk2 << t << " " << y2 << endl;
        out_rk4 << t << " " << y4 << endl;

        y2 = rk2(t, y2, h);
        y4 = rk4(t, y4, h);
        t += h;
    }

    out_rk2.close();
    out_rk4.close();

    cout << "Simulación completada. Archivos rk2.dat y rk4.dat generados.\n";
    return 0;
}

