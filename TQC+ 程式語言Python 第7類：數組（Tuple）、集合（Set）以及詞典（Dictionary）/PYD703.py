# TODO
a = input()
ls = []
while a != "end":
    ls.append(a)
    a = input()

tp = tuple(ls)

print(tp)
print(tp[:3])
print(tp[-3:])