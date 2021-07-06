import sys
sys.path.append("D:\Z_Package\mod")

import mod1
print(mod1.add(2, 1))
print(mod1.sub(2, 1))

from mod1 import add, sub
print(add(3, 1))
print(sub(3, 1))

import mod2 as m2
print(m2.PI)

print(m2.Math().solv(2))