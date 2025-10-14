#include <iomanip>
#include <cmath>
using namespace std;

double f(double x);
void secant(double x0, double x1, double tolerance, int maxIterations);

int main() {
  double  x0 = 4.0,
          x1 = 5.0,
          tolerance = 0.001;
  int maxIterations = 100;

  printf ("\nRoot finding by Secant Method\n");

  secant(x0, x1, tolerance, maxIterations);

  return 0;
}

double f(double x) {
  return sin(x) - (0.25*x) + 2;
}

void secant(double x0, double x1, double tolerance, int maxIterations) {
  double x2, error;
  int iteration;
  error = tolerance+1;
  iteration = 0;

  printf ("\ni   xi\t\tf(xi-1)\t\tf(xi)\t\tError\n");

  while (error > tolerance) {
    x2 = x1 - ( (f(x1)*(x0-x1)) / (f(x0) - f(x1)) );
    error = (fabs (x1-x2));
    printf ("%d   %g\t%0.6f\t%0.6f\t%g\n",iteration+2,x2,f(x0),f(x1),error);

    x0 = x1;
    x1 = x2;
    iteration++;
    if (iteration > maxIterations) {
      printf ("\n\nThe maximum amount of allowed iterations was exceeded\n\n");
      return;
    }
  }
  printf ("\n\nFor a tolerance of %g the root of is: %g\n\n",tolerance,x2);

}
