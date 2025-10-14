#include <iomanip>
#include <cmath>
using namespace std;

double f(double x);
double f_derivative(double x);
void newton_raphson(double x0, double tolerance, int maxIterations);

int main() {
  double  x0 = 3,
          tolerance = 0.001;
  int maxIterations = 100;

  printf ("\nRoot finding by Newton Raphson\n");

  newton_raphson(x0, tolerance, maxIterations);

  return 0;
}

double f(double x) {
  return sin(x) - (0.25*x) + 2;
}

double f_derivative(double x) {
  return cos(x) - 0.25;
}

void newton_raphson(double x0, double tolerance, int maxIterations) {
  double x1, error;
  int iteration;
  error = tolerance + 1;
  iteration = 1;

  printf ("\ni   xi\t\tf(xi)\t\tf'(xi)\t\tError\n");
  printf ("0   %g\t\t%0.6f\t%0.6f\t%g\n",x0,f(x0),f_derivative(x0),fabs(x1 - x0));

  while (error > tolerance) {
    x1 = x0 - f(x0) / f_derivative(x0);
    error = fabs(x1 - x0);
    x0 = x1;
    iteration++;
    printf ("%d   %g\t%0.6f\t%0.6f\t%g\n",iteration,x1,f(x1),f_derivative(x1),error);

    if (iteration > maxIterations) {
      printf ("\n\nThe maximum amount of allowed iterations was exceeded\n\n");
      return;
    }
  }
  printf ("\n\nFor a tolerance of %g the root of is: %g\n\n",tolerance,x1);

}
