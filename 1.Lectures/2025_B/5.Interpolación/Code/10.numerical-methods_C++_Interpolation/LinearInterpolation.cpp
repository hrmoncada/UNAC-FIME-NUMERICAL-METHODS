#include <iomanip>
using namespace std;

double linear_interpolation(double x, double x0, double x1, double y0, double y1);

int main() {
	double x = 2.5, x0 = 2, x1 = 4, y0 = 3, y1 = 6, y;

	printf("\nInterpolation by Linear Interpolation method\n");
	y = linear_interpolation(x,x0,x1,y0,y1);
	
	printf("\nWhen x = %g\n     y = %g\n",x, y);
	printf("\n x\t y\n%g\t%g\n%g\t%g\n%g\t%g\n\n",x0,y0,x,y,x1,y1);

  return 0;
}

double linear_interpolation(double x, double x0, double x1, double y0, double y1) {
	return y0 + ((y1 - y0) / (x1 - x0))*(x - x0);
}
