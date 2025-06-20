from sympy import symbols, diff
x = symbols('x')
f = x**2 + 3*x + 1

df = diff(f, x)

print(df)
