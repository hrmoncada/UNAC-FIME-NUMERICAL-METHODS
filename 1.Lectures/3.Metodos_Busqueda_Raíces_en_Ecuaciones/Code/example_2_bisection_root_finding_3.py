def bisection_method(func, a, b, tolerance=1e-6, max_iterations=100):
    """
    Finds a root of a function using the bisection method.

    Args:
        func (function): The function for which to find the root.
                         It should take a single numerical argument.
        a (float): The lower bound of the initial interval.
        b (float): The upper bound of the initial interval.
        tolerance (float): The desired accuracy of the root.
        max_iterations (int): The maximum number of iterations to perform.

    Returns:
        float: The approximate root of the function.
        None: If a root is not found within the given interval or iterations.
    """

    if func(a) * func(b) >= 0:
        print("Error: The function does not change sign over the given interval.")
        return None

    for i in range(max_iterations):
        midpoint = (a + b) / 2
        f_mid = func(midpoint)

        if abs(f_mid) < tolerance:
            return midpoint  # Root found within tolerance

        if func(a) * f_mid < 0:
            b = midpoint
        else:
            a = midpoint

        if abs(b - a) < tolerance:
            return midpoint  # Interval sufficiently small

    print("Warning: Maximum iterations reached. The root may not be found with desired accuracy.")
    return (a + b) / 2  # Return the midpoint of the final interval

# Example usage:
def my_function(x):
    return x**3 - x - 2

# Find a root in the interval [1, 2]
root = bisection_method(my_function, 1, 2)

if root is not None:
    print(f"Approximate root: {root}")
    print(f"Function value at root: {my_function(root)}")

# Example with a different function and interval
def another_function(x):
    return x**2 - 4

root2 = bisection_method(another_function, 0, 3, tolerance=1e-5)

if root2 is not None:
    print(f"Approximate root for x^2 - 4: {root2}")
    print(f"Function value at root: {another_function(root2)}")
