#include <iomanip>
using namespace std;

void NewtonInterpolation(int n, double x[], double y[], double test);

int main() {
  const int n = 3;
	double x[n] = {1,4,6},
         y[n] = {0,1.386294,1.791759};
	double test = 2;

  printf("\nInterpolation by Newton Polynomial Interpolation method\n");

  NewtonInterpolation(n, x, y, test);

  return 0;
}

void NewtonInterpolation(int n, double x[], double y[], double test){
  int i,j;
  double sum,mult;
  sum = 0;

  for(j = 0; j < n-1; j++) {
    for(i = n-1; i > j; i--) {
      y[i] = (y[i]-y[i-1]) / (x[i]-x[i-j-1]);
    }
  }
  for(i = n-1; i >= 0; i--) {
    mult = 1;
    for(j=0; j < i; j++) {
      mult *= (test-x[j]);
    }
    mult *= y[j];
    sum += mult;
  }
  printf("\nThe result is: %g\n\n",sum);
}
