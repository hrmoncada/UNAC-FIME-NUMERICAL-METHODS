/*==============================
 Sistema 2D
 dx/dt = y 
 dy/dt = -x

==============================
Compilar
g++ ODE_4_2D_Runge_Kutta_2_Runge_Kutta_4.cpp -o runge_kutta
Executar
./runge_kutta
plot
python plot_7_ODE_2D_Runge_Kutta_2_Runge_Kutta_4.py
*/

#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

// System definition
double f(double x, double y) { return y; }
double g(double x, double y) { return -x; }

int main() {
    double t0 = 0.0, tf = 20.0;
    double h = 0.01;
    double x0 = 1.0, y0 = 0.0;

    int steps = (tf - t0) / h;

    double x_rk2 = x0, y_rk2 = y0;
    double x_rk4 = x0, y_rk4 = y0;
    double t = t0;

    ofstream rk2_file("rk2.csv");
    ofstream rk4_file("rk4.csv");

    rk2_file << "t,x,y\n";
    rk4_file << "t,x,y\n";

    for (int i = 0; i <= steps; i++) {

        // Save data
        rk2_file << t << "," << x_rk2 << "," << y_rk2 << "\n";
        rk4_file << t << "," << x_rk4 << "," << y_rk4 << "\n";

        // ---------- RK2 (Midpoint Method) ----------
        double k1x = h * f(x_rk2, y_rk2);
        double k1y = h * g(x_rk2, y_rk2);

        double k2x = h * f(x_rk2 + 0.5 * k1x, y_rk2 + 0.5 * k1y);
        double k2y = h * g(x_rk2 + 0.5 * k1x, y_rk2 + 0.5 * k1y);

        x_rk2 += k2x;
        y_rk2 += k2y;

        // ---------- RK4 ----------
        double k1x4 = h * f(x_rk4, y_rk4);
        double k1y4 = h * g(x_rk4, y_rk4);

        double k2x4 = h * f(x_rk4 + 0.5 * k1x4, y_rk4 + 0.5 * k1y4);
        double k2y4 = h * g(x_rk4 + 0.5 * k1x4, y_rk4 + 0.5 * k1y4);

        double k3x4 = h * f(x_rk4 + 0.5 * k2x4, y_rk4 + 0.5 * k2y4);
        double k3y4 = h * g(x_rk4 + 0.5 * k2x4, y_rk4 + 0.5 * k2y4);

        double k4x4 = h * f(x_rk4 + k3x4, y_rk4 + k3y4);
        double k4y4 = h * g(x_rk4 + k3x4, y_rk4 + k3y4);

        x_rk4 += (k1x4 + 2*k2x4 + 2*k3x4 + k4x4) / 6.0;
        y_rk4 += (k1y4 + 2*k2y4 + 2*k3y4 + k4y4) / 6.0;

        t += h;
    }

    rk2_file.close();
    rk4_file.close();

    cout << "Simulation complete. Files: rk2.csv, rk4.csv\n";
    return 0;
}

