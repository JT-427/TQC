# TODO

def compute(a, b, c):
    d = b**2 -4*a*c
    if d < 0:
        print("Your equation has no root.")
    else:
        x1 = (-b + d**(1/2))/(2*a)
        x2 = (-b - d**(1/2))/(2*a)

        print(f"{x1}, {x2}")
a = eval(input())
b = eval(input())
c = eval(input())
compute(a, b, c)


"""
Your equation has no root.
"""
