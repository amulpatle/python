# import module1

# print(module1.sum(10,55))
# print(module1.mul(10,55))

# import module1 as m
# print(m.mul(10,55))
# print(m.sum(55,77))

from module1 import sum
from module1 import mul

print(sum(10,20))
print(mul(10,20))