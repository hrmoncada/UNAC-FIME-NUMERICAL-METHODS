#include <iomanip>
#include <cmath>
using namespace std;

double f(double x);
void bisection(double a, double b, double tolerance);

int main() {
  double  a = 4,
          b = 5,
          tolerance = 0.001;

  printf ("\nRoot finding by Bisection Method\n");

  bisection(a, b, tolerance);

  return 0;
}

double f(double x) {
  return sin(x) - (0.25*x) + 2;
}

void bisection(double a, double b, double tolerance) {
  double xr, error;
  error = tolerance + 1;

  if (f(a) * f(b) > 0) {
    printf ("f(%g) and f(%g) do not enclose a root\n\n",a,b);
    return;
  }

  printf ("\na\tb\tx\tf(a) \t\tf(b) \t\tf(x)\t\terror\n");
  while (error > tolerance) {
    xr = (a + b) / 2.0;
    error = fabs(f(xr));

    printf ("%g\t%g\t%g\t%.6g \t%.6g \t %.6g\t%0.4f\n",a,b,xr,f(a),f(b),f(xr),error);
    if (f(xr) * f(a) > 0) {
      a = xr;
    } else if (f(xr) * f(b) > 0) {
      b = xr;
    }
  }
  printf ("\n\nFor a tolerance of %g the root of is: %g\n",tolerance,xr);

}
