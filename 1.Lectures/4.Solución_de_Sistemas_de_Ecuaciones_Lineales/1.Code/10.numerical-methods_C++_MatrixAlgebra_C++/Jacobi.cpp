#include <iomanip>
#include <cmath>
using namespace std;

const int n = 3;

void jacobi(double[][n], double[], double tolerance, int maxIterations);
double f(double b, double a1, double x1, double a2, double x2, double a3);

int main() {
	double  a[n][n] = {{3,-0.1,-0.2},
										{0.1,7,-0.3},
										{0.3,-0.2,10}},
					b[n] = {7.85,-19.3,71.4},
					tolerance = 0.000001;
	int maxIterations = 100;

	printf("\nMatrix Algebra by Jacobi method\n");

	jacobi(a, b, tolerance, maxIterations);

	return 0;
}

void jacobi (double a[][n], double b[], double tolerance, int maxIterations) {
	double y[10];
	double x1, x2, x3, e1, e2, e3, t1, t2, t3;
	int iteration = 1;
	x1 = x2 = x3 = 0;

	do {
		t1 = x1;
		t2 = x2;
		t3 = x3;

		x1 = f(b[0], a[0][1], t2, a[0][2], t3, a[0][0]);
		x2 = f(b[1], a[1][0], t1, a[1][2], t3, a[1][1]);
		x3 = f(b[2], a[2][0], t1, a[2][1], t2, a[2][2]);

		e1 = fabs(a[0][0] * x1 + a[0][1] * x2 + a[0][2] * x3 - b[0]);
		e2 = fabs(a[1][0] * x1 + a[1][1] * x2 + a[1][2] * x3 - b[1]);
		e3 = fabs(a[2][0] * x1 + a[2][1] * x2 + a[2][2] * x3 - b[2]);

		if (iteration > maxIterations) {
      printf("\n\nThe maximum amount of allowed iterations was exceeded\n\n");
      return;
    }

		iteration++;

	} while (e1 > tolerance || e2 > tolerance || e3 > tolerance);

	printf("\nx1 = %g\nx2 = %g\nx3 = %g\nIterations: %d\n\n",x1,x2,x3,iteration);
}

double f(double b, double a1, double x1, double a2, double x2, double a3) {
	return (b - a1*x1 - a2*x2) / a3;
}
