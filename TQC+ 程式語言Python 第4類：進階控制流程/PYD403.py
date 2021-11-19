# TODO
a = eval(input())
b = eval(input())

c = 0
ls = []
for i in range(a, b+1):
    if i % 4 == 0 or i % 9 == 0:
        ls.append(i)
        
        
for i in range(len(ls)):
    print(format(ls[i], "<4d"), end="")
    if i % 10 == 9:
        print()
print()
print(len(ls))
print(sum(ls))