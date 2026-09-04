#include <iomanip>
using namespace std;

const int n = 3;

void gaussjordan(double [n][n], double[]);
void printMatrix(double [n][n], double []);
void makeDiagonalOne(double [n][n], double []);

int main() {
	double  A[n][n] = {{3,-0.1,-0.2},
										{0.1,7,-0.3},
										{0.3,-0.2,10}},
					b[n] = {7.85,-19.3,71.4};

	printf ("\nMatrix Algebra by Gauss-Jordan method\n");

	gaussjordan(A, b);

	return 0;
}

void gaussjordan(double A[n][n], double B[]) {
	int x, y, i, j, h;
	double auxB;
	double auxA[n];

	printf("\n\tInput Matrix\n");
	printMatrix(A, B);

	for (x = 0; x < n; x++) {
		auxA[x] = 0;
	}
	auxB = 0;
	for (x = 0; x < n; x++) {
		if (A[x][x] == 0){
			for (y = x; y < n ; y++) {
				if (A[y][x] != 0) {
					for (h = 0; h < n; h++) {
						auxA[h]=A[y][h];
						A[y][h]=A[x][h];
						A[x][h]=auxA[h];
					}
					auxB=B[y];
					B[y]=B[x];
					B[x]=auxB;
				}
			}
		}
	}

	makeDiagonalOne(A, B);

	printf("\n\tOutput Matrix\n");
	printMatrix(A, B);
	for (x = 0; x < n; x++) {
		printf("X%d = %g\n",x,B[x]);
	}
	printf("\n");

}

void printMatrix(double A[n][n], double b[]) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			printf("%g\t",A[i][j]);
		}
		printf("| %g\n",b[i]);
	}
	printf("\n");
}

void makeDiagonalOne(double A[n][n], double B[]) {
	double z, w;
	for (int x = 0; x < n; x++) {
		z = A[x][x];
		B[x] = B[x] / z;
		for (int y = 0; y < n; y++) {
			A[x][y] = A[x][y] / z;
		}
		for (int i = 0; i < n; i++) {
			if (i != x) {
				w = A[i][x];
				for (int j = 0 ; j < n ; j++){
					A[i][j] = (A[i][j])-(w * A[x][j]);
				}
				B[i] = (B[i])-(w * B[x]);
			}
		}
	}
}
