# TODO

ls = []

for i in range(10):
    value = eval(input())
    ls.append(value)

for _ in range(len(ls)-1):
    for a in range(len(ls)-1):
        if ls[a] < ls[a+1]:
            ls[a], ls[a+1] = ls[a+1], ls[a]

print(" ".join(str(c) for c in ls[:3]))