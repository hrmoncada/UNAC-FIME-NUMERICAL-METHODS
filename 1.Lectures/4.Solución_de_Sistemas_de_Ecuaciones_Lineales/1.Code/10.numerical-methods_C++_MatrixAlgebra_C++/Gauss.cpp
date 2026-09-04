#include <iomanip>
using namespace std;

const int n = 3;

void gauss(double [n][n+1]);
void printMatrix(double A[n][n+1]);

int main() {
  double  A[n][n+1] = {{3,-0.1,-0.2, 7.85},
										{0.1,7,-0.3, -19.3},
										{0.3,-0.2,10, 71.4}};

	printf("\nMatrix Algebra by Gauss method\n");

  gauss(A);

  return 0;
}

void gauss(double A[n][n+1]) {
  int x, i, j;
  double auxA[n], z, w;

  printf("\n\tInput Matrix\n");
  printMatrix(A);

  for (x = 0; x < n; x++) {
    z = A[x][x];
    for (j = 0; j < n+1; j++) {
      A[x][j] = A[x][j]/z;
    }
    for (i = 0; i < n; i++) {
      if (i != x) {
        w = A[i][x];
        for (j = 0; j < n+1; j++) {
          auxA[j] = A[x][j]*(w*-1);
        }
        for (j = 0; j < n+1; j++) {
          A[i][j]= A[i][j] + auxA[j];
        }
      }
    }
  }

  for (i=0;i<n;i++) {
    printf("X%d = %g\n",i,A[i][n]);
  }
  printf("\n");

}

void printMatrix(double A[n][n+1]) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			printf("%g\t",A[i][j]);
		}
    printf("| %g\n",A[i][n]);
	}
  printf("\n");
}
