# TODO
import math
x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())

d = pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5)

print(f"( {x1} , {y1} )")
print(f"( {x2} , {y2} )")
print("Distance =", format(d, ".4f"))
