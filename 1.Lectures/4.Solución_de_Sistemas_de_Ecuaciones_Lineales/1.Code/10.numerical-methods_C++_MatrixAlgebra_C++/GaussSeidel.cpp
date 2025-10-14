#include <iomanip>
#include <cmath>
using namespace std;

const int n = 3;

void gauss_seidel(double[][n], double[], double tolerance, int maxIterations);

int main() {
  double  a[n][n] = {{3,-0.1,-0.2},
                    {0.1,7,-0.3},
                    {0.3,-0.2,10}},
          b[n] = {7.85,-19.3,71.4},
          tolerance = 0.000001;
  int maxIterations = 100;


  printf("\nMatrix Algebra by Gauss–Seidel method\n");

  gauss_seidel(a, b, tolerance, maxIterations);

  return 0;
}

void gauss_seidel(double a[][n], double b[], double tolerance, int maxIterations) {
  double y[10];
  double e1, e2, e3;
  int iteration = 1, i = 0, j = 0;
  int auxiter = maxIterations;
  double x[n] = {0, 0, 0};

  do {
    for (i = 0; i < n; i++) {
      y[i] = (b[i] / a[i][i]);

      for (j = 0; j < n; j++) {
        if (j == i) {
          continue;
        }

        y[i] = y[i] - ((a[i][j] / a[i][i]) * x[j]);
        x[i] = y[i];
      }
    }

    e1 = b[0] - fabs((a[0][0]*y[0]) + (a[0][1]*y[1]) + (a[0][2]*y[2]));
    e2 = b[1] - fabs((a[1][0]*y[0]) + (a[1][1]*y[1]) + (a[1][2]*y[2]));
    e3 = b[2] - fabs((a[2][0]*y[0]) + (a[2][1]*y[1]) + (a[2][2]*y[2]));

    if (iteration > maxIterations) {
      printf("\n\nThe maximum amount of allowed iterations was exceeded\n\n");
      return;
    }

		iteration++;

  } while(e1 > tolerance || e2 > tolerance || e3 > tolerance);

  for(i = 0; i < n ; i++){
    printf("x%d = %g\n",i+1,y[i]);
  }
  printf("\nIterations: %d\n\n",iteration);

}
