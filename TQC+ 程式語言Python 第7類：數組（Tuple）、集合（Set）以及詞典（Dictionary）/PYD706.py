# TODO
s1 = set()

l = eval(input())
for i in range(l):
    p = input()
    p = p.lower()
    sp = set(p)
    if len(sp) == 27:
        print(True)
    else:
        print(False)