#include <iomanip>
using namespace std;

void Lagrange(int n, double x[], double y[], double test);

int main() {
	int n = 3;
	double x[3] = {1,4,6},
				y[3] = {0,1.386294,1.791759};
	double test = 2.0;

	printf("\nInterpolation by Newton Polynomial Interpolation method\n");

	Lagrange(n, x, y, test);

	return 0;
}

void Lagrange(int n, double x[], double y[], double test){
	int i, j;
	double z,w,sum,u,d;
	sum = 0;
	u = d = 1;

	for (i = 0; i < n ; i++) {
		for (j = 0; j < n ; j++) {
			if (j != i){
				u = u*(test - x[j]);
				d = d*(x[i] - x[j]);
			}
		}
		sum += (y[i]*(u/d));
		u = d = 1;
	}
	printf("\nThe result is: %g\n\n",sum);
}
