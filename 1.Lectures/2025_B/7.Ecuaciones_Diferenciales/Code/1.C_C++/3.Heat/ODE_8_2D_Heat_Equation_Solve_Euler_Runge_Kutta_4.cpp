/*==============================
 Sistema 2D
 du/dt = alpha * (d^2u/dx^2 + d^2u/dy^2 )
 (x, y) \in [0,L] x [0,L] 
Condiciones de frontera: Dirichlet u = 0
Condición inicial: u(x,y,0) = sin(\pi x)sin( \pi y)

==============================
Compilar
python ODE_5_2D_Heat_Equation_Solve_Euler_Runge_Kutta_4.py
*/

#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>

using namespace std;

const int Nx = 30;
const int Ny = 30;
const double L = 1.0;
const double alpha = 1.0;

const double dx = L / (Nx - 1);
const double dy = L / (Ny - 1);
const double dt = 0.0005;
const int Nt = 500;

typedef vector<vector<double>> Matrix;

// Laplacian operator
double laplacian(const Matrix& u, int i, int j) {
    return (u[i+1][j] - 2*u[i][j] + u[i-1][j]) / (dx*dx)
         + (u[i][j+1] - 2*u[i][j] + u[i][j-1]) / (dy*dy);
}

// Initialize field
Matrix initialize() {
    Matrix u(Nx, vector<double>(Ny,0.0));
    for(int i=1;i<Nx-1;i++)
        for(int j=1;j<Ny-1;j++){
            double x = i*dx;
            double y = j*dy;
            u[i][j] = sin(M_PI*x)*sin(M_PI*y);
        }
    return u;
}

// Euler method
void Euler(Matrix& u) {
    Matrix unew = u;
    for(int i=1;i<Nx-1;i++)
        for(int j=1;j<Ny-1;j++)
            unew[i][j] = u[i][j] + dt*alpha*laplacian(u,i,j);
    u = unew;
}

// RK4 method
void RK4(Matrix& u) {
    Matrix k1=u, k2=u, k3=u, k4=u, temp=u;

    for(int i=1;i<Nx-1;i++)
        for(int j=1;j<Ny-1;j++)
            k1[i][j] = alpha*laplacian(u,i,j);

    for(int i=1;i<Nx-1;i++)
        for(int j=1;j<Ny-1;j++)
            temp[i][j] = u[i][j] + 0.5*dt*k1[i][j];
    for(int i=1;i<Nx-1;i++)
        for(int j=1;j<Ny-1;j++)
            k2[i][j] = alpha*laplacian(temp,i,j);

    for(int i=1;i<Nx-1;i++)
        for(int j=1;j<Ny-1;j++)
            temp[i][j] = u[i][j] + 0.5*dt*k2[i][j];
    for(int i=1;i<Nx-1;i++)
        for(int j=1;j<Ny-1;j++)
            k3[i][j] = alpha*laplacian(temp,i,j);

    for(int i=1;i<Nx-1;i++)
        for(int j=1;j<Ny-1;j++)
            temp[i][j] = u[i][j] + dt*k3[i][j];
    for(int i=1;i<Nx-1;i++)
        for(int j=1;j<Ny-1;j++)
            k4[i][j] = alpha*laplacian(temp,i,j);

    for(int i=1;i<Nx-1;i++)
        for(int j=1;j<Ny-1;j++)
            u[i][j] += dt*(k1[i][j]+2*k2[i][j]+2*k3[i][j]+k4[i][j])/6.0;
}

// Save field
void save(const Matrix& u, string filename) {
    ofstream file(filename);
    for(int i=0;i<Nx;i++){
        for(int j=0;j<Ny;j++)
            file << u[i][j] << " ";
        file << "\n";
    }
}

int main(){
    Matrix uEuler = initialize();
    Matrix uRK4   = initialize();

    for(int n=0;n<Nt;n++){
        Euler(uEuler);
        RK4(uRK4);
    }

    save(uEuler,"euler.dat");
    save(uRK4,"rk4.dat");

    cout << "Simulation finished.\n";
    return 0;
}

