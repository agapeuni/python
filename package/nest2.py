from mod.mod1 import add, sub
import mod.mod1 as m1
import mod.mod2 as m2

print(add(3, 1))
print(sub(3, 1))

print(m1.add(2, 1))
print(m1.sub(2, 1))

print(m2.PI)
print(m2.Math().solv(2))

