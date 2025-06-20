from scipy.optimize import minimize_scalar


def f(x):

    return x**2 + 2*x + 1


result = minimize_scalar(f)
print(result)
