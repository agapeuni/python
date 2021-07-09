from sympy import Symbol, solve, pprint

print()
a = Symbol('a')
b = Symbol('b')
e = (a + b)**5
pprint(e)

print()
x = Symbol('x')
eq = 2 * x - 6
print("2 * x - 6 =", solve(eq))

print()
y = Symbol('y')
eq = y - 6
print("y - 6 =", solve(eq))
