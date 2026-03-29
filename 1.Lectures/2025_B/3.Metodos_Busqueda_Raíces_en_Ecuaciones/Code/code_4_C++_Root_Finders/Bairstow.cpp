#include <iomanip>
#include <vector>
#include <cmath>
using namespace std;

void bairstow(vector<double> &polynomial, double p, double q, double err);

int main() {
  double  coefficients[] = {1, -4, 5.25, -2.5},
          r = -0.5,
          s = 0.5,
          tolerance = 0.00001;
  vector<double> polynomial(coefficients, coefficients + sizeof(coefficients) / sizeof(double));

  printf ("\nRoot finding by Bairstow Method\n");
  printf("\nOriginal polynomial: ");
  for (unsigned i = 0; i < polynomial.size() - 1; i++) {
    printf("%gx^%lu + ",coefficients[i],polynomial.size()-i-1);  // %lu stands for unsigned long int
  }
  printf("%g\n\n",coefficients[polynomial.size() - 1]);

  bairstow(polynomial, r, s, tolerance);

  return 0;
}

void synthetic_division(vector<double> &polynomial, vector<double> &res, vector<double> &aux, double r, double s) {
  int i, j, degree;
  degree = polynomial.size() - 1;

  for (i = degree, j = 0; i >= 0; i--, j++) {
    if (i == degree) {
      res[j] = polynomial[j];
    } else if (i == degree - 1) {
      res[j] = polynomial[j] + res[j - 1] * r;
    } else {
      res[j] = polynomial[j] + res[j - 1] * r + res[j - 2] * s;
    }
  }

  for (i = degree, j = 0; i >= 0; i--, j++) {
    if (i == degree) {
      aux[j] = res[j];
    } else if (i == degree - 1) {
      aux[j] = res[j] + aux[j - 1] * r;
    } else {
      aux[j] = res[j] + aux[j - 1] * r + aux[j - 2] * s;
    }
  }
}

struct complex_number {
  double r, i;
};

void bairstow(vector<double> &polynomial, double p, double q, double err) {
  vector<complex_number *> roots;
  while (polynomial.size() > 3) {
    vector<double> res(polynomial.size(), 0.0);
    vector<double> aux(polynomial.size(), 0.0);

    double dp = 0.0;
    double dq = 0.0;
    double error_p = 1.0;
    double error_q = 1.0;
    int iteration = 1;
    printf ("i   polynomial\n");
    do {
      for (unsigned i = 0; i < res.size(); i++) {
        res[i] = 0;
        aux[i] = 0;
      }

      synthetic_division(polynomial, res, aux, p, q);

      printf("%d   {",iteration);
      for (unsigned i = 0; i < res.size(); i++) {
        printf("%g",res[i]);
        if (i < res.size()-1){
          printf(", ");
        }
      }
      printf("}\n");

      int deg = polynomial.size() - 1;
      double d = aux[deg - 2] * aux[deg - 2] - aux[deg - 1] * aux[deg - 3];
      dp = (-res[deg - 1] * aux[deg - 2] + res[deg] * aux[deg - 3]) / d;
      dq = (-aux[deg - 2] * res[deg] + aux[deg - 1] * res[deg - 1]) / d;

      error_p = dp / p;
      error_q = dq / q;
      p += dp;
      q += dq;

      iteration++;
    } while (fabs(error_p) > err && fabs(error_q) > err);

    double det = pow(p, 2) + 4 * q;

    complex_number *root1 = new complex_number;
    complex_number *root2 = new complex_number;
    if (det < 0) {
      root1->r = p / 2;
      root1->i = sqrt(-det) / 2;
      root2->r = p / 2;
      root2->i = -sqrt(-det) / 2;
    }
    else {
      root1->r = (p + sqrt(det)) / 2;
      root1->i = 0;
      root2->r = (p - sqrt(det)) / 2;
      root2->i = 0;
    }
    roots.push_back(root1);
    roots.push_back(root2);

    res = vector<double>(polynomial.size(), 0.0);
    aux = vector<double>(polynomial.size(), 0.0);

    synthetic_division(polynomial, res, aux, p, q);

    for (unsigned i = 0; i < polynomial.size() - 2; i++) {
      polynomial[i] = res[i];
    }
    polynomial.pop_back();
    polynomial.pop_back();

    printf("\nPolynomial Update\n{");
    for (unsigned i = 0; i < polynomial.size(); i++) {
      printf("%g",polynomial[i]);
      if (i < polynomial.size()-1){
        printf(", ");
      }
    }
    printf("}\n");
  }

  if (polynomial.size() == 3) {
    int p = -polynomial[1];
    int q = -polynomial[2];
    double det = pow(p, 2) + 4 * q;

    complex_number *root1 = new complex_number;
    complex_number *root2 = new complex_number;
    if (det < 0) {
      root1->r = p / 2;
      root1->i = sqrt(-det) / 2;
      root2->r = p / 2;
      root2->i = -sqrt(-det) / 2;
    }
    else {
      root1->r = (p + sqrt(det)) / 2;
      root1->i = 0;
      root2->r = (p - sqrt(det)) / 2;
      root2->i = 0;
    }
    roots.push_back(root1);
    roots.push_back(root2);
  }
  else if (polynomial.size() == 2) {
    complex_number *r = new complex_number;
    r->r = -polynomial[1] / polynomial[0];
    r->i = 0;
    roots.push_back(r);
  }

  printf("\nRoots:\n");
  for (unsigned i = 0; i < roots.size(); i++) {
    if (roots[i]->i != 0) {
      printf("%g + %gi\n",roots[i]->r,roots[i]->i);
    }
    else {
      printf("%g\n\n",roots[i]->r);
    }
  }
}
