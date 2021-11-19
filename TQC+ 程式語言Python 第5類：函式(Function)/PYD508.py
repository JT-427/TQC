# TODO

def compute(a, b):
    if a > b:
        a, b = b, a
    
    value = 1
    for i in range(a):
        i += 1
        if a % (i) == 0 and b % (i) == 0:
            value = i
    print(value)

a = input()
v = a.split(",")

compute(int(v[0]), int(v[1]))