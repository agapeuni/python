from sympy import pprint, Symbol

a = Symbol('a')
b = Symbol('b')
e = (a + b)**5

print("\nExpression:")
pprint(e)
print('\nExpansion of the above expression:')
pprint(e.expand())
print()