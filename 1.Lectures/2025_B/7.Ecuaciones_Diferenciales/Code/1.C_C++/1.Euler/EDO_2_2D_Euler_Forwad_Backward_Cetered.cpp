/*==============================
Sistema 2D
dx/dt = -y
dy/dt = x
==============================
Compilar
g++ EDO_2_2D_Euler_Forwad_Backward_Cetered -o euler_2d

Executar
./euler_2d

Se generan:
euler_forward.dat
euler_backward.dat
euler_center.dat

Graficar con python
python plot_euler_2d.py
*/

#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

// Sistema 2D
double f(double x, double y) { return y; }
double g(double x, double y) { return -x; }

int main() {
    double h = 0.01;
    int N = 2000;

    // Condición inicial
    double x0 = 1.0, y0 = 0.0;

    ofstream fe("euler_forward.dat");
    ofstream fb("euler_backward.dat");
    ofstream fc("euler_center.dat");

    // ==============================
    // Euler Forward
    // ==============================
    double x = x0, y = y0;
    for (int i = 0; i < N; i++) {
        fe << x << " " << y << "\n";
        double xn = x + h * f(x, y);
        double yn = y + h * g(x, y);
        x = xn;
        y = yn;
    }

    // ==============================
    // Euler Backward (implícito simple)
    // Resolvido analíticamente para el sistema
    // ==============================
    x = x0; y = y0;
    for (int i = 0; i < N; i++) {
        fb << x << " " << y << "\n";
        double denom = 1 + h*h;
        double xn = (x + h*y) / denom;
        double yn = (y - h*x) / denom;
        x = xn;
        y = yn;
    }

    // ==============================
    // Euler Centered (Leapfrog)
    // ==============================
    double x_prev = x0;
    double y_prev = y0;

    // Primer paso con Euler forward
    x = x0 + h * f(x0, y0);
    y = y0 + h * g(x0, y0);

    fc << x0 << " " << y0 << "\n";
    for (int i = 1; i < N; i++) {
        fc << x << " " << y << "\n";
        double x_next = x_prev + 2*h*f(x, y);
        double y_next = y_prev + 2*h*g(x, y);
        x_prev = x;
        y_prev = y;
        x = x_next;
        y = y_next;
    }

    fe.close();
    fb.close();
    fc.close();

    cout << "Datos generados correctamente.\n";
    return 0;
}

