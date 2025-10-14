'''
https://pythonnumericalmethods.studentorg.berkeley.edu/notebooks/chapter19.03-Bisection-Method.html

Again, the  \sqrt(2) is the root of the function f(x)=x^2−2. 
Using x0=1.4 as a starting point, use the previous equation to estimate  \sqrt(2).
Compare this approximation with the value computed by Python’s sqrt function.
'''

import numpy as np

def my_newton(f, df, x0, tol):
    # output is an estimation of the root of f 
    # using the Newton Raphson method
    # recursive implementation
    if abs(f(x0)) < tol:
        return x0
    else:
        return my_newton(f, df, x0 - f(x0)/df(x0), tol)

f = lambda x: x**2 - 2
f_prime = lambda x: 2*x
newton_raphson = 1.4 - (f(1.4))/(f_prime(1.4))

print("newton_raphson =", newton_raphson)
print("sqrt(2) =", np.sqrt(2))

estimate = my_newton(f, f_prime, 1.5, 1e-6)

print("estimate =", estimate)
print("sqrt(2) =", np.sqrt(2))

# Compute a single Newton step to get an improved approximation of the root of the function f(x)=x^3+3x^2−2x−5 and an initial guess, x0=0.29.
#x0 = 0.29
#x1 = x0-(x0**3+3*x0**2-2*x0-5)/(3*x0**2+6*x0-2)
#print("x1 =", x1)
