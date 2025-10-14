'''
https://pythonnumericalmethods.studentorg.berkeley.edu/notebooks/chapter19.03-Bisection-Method.html

Compute the root of the function f(x)=x63 − 100 x^2 − x + 100 using f_solve.
'''

from scipy.optimize import fsolve
f = lambda x: x**3-100*x**2-x+100

fsolve(f, [2, 80])

