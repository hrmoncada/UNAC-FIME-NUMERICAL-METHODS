#include <iomanip>
using namespace std;

const int n = 3;

void cramer(double [n][n], double[]);
void printMatrix(double [n][n], double []);
void correctDiagonal(double [n][n], double [n][n]);
void makeDiagonalOne(double A[n][n], double B[n][n]);

int main() {
	double  A[n][n] = {{3,-0.1,-0.2},
										{0.1,7,-0.3},
										{0.3,-0.2,10}},
					b[n] = {7.85,-19.3,71.4};

	printf("\nMatrix Algebra by Cramer method\n");

	cramer(A, b);

	return 0;
}
void cramer(double A[n][n], double res1[n]){
	int x, y, i, j, h;
	double w, r;
	r = 1;

	double B[n][n];
	double auxA[n][n];
	double auxB[n][n];
	double res2[n];

	printMatrix(A, res1);

	for (x = 0; x < n; x++) { // init auxiliar matrices
		res2[x] = 1;
		for (y = 0; y < n; y++) {
			B[x][y] = 0;
			auxB[x][y] = 0;
			auxA[x][y] = A[x][y];
		}
		B[x][x]=1;
		auxB[x][x]=1;
	}

	correctDiagonal(A, B);
	makeDiagonalOne(A, B);

	for (x = 0; x < n ; x++) { //Determinant
		r = r * B[x][x];
	}

	for (x = 0; x < n ; x++) {
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				A[i][j] = auxA[i][j];
				B[i][j] = auxB[i][j];
			}
			A[i][x] = res1[i];
		}

		correctDiagonal(A, B);
		makeDiagonalOne(A, B);
		w = res2[x];
		for (h = 0; h < n ; h++) {
			w = w * B[h][h];
		}
		res2[x] = w;
	}

	printf("\nThe DETERMINANT of the input matrix is = %g\n\n",r);

	for (x = 0; x < n; x++) {
		printf("X%d = %g/%g = %g\n",x,res2[x],r,(res2[x]/r));
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
}

void correctDiagonal(double A[n][n], double B[n][n]) {
	double auxa[n];
	for (int i = 0; i < n; i++) {
		auxa[i] = 0;
	}
	for (int x = 0; x < n; x++) {
		if (A[x][x] == 0) {
			for (int y = x; y < n ; y++) {
				if (A[y][x] == 0){
					for (int h = 0; h < n; h++) {
						auxa[h] = A[y][h];
						A[y][h] = A[x][h];
						A[x][h] = auxa[h];
					}
					B[x][x] = B[x][x] * (-1);
				}
			}
		}
	}
}

void makeDiagonalOne(double A[n][n], double B[n][n]) {
	double z, w;
	for (int x = 0; x < n; x++) {
		z = A[x][x];
		for (int y = 0; y < n; y++) {
			A[x][y] = A[x][y] / z;
		}
		B[x][x] = B[x][x]*z;
		for (int i = x; i < n; i++) {
			if (i != x) {
				w = A[i][x];
				B[i][x] = w;
				for (int j = 0 ; j < n ; j++) {
					A[i][j] = (A[i][j])-(w * A[x][j]);
				}
			}
		}
	}
}
