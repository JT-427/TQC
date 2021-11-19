# TODO

print("Enter group X's subjects:")
# TODO
X = set()
a = input()
while a != "end":
    X.add(a)
    a = input()

print("Enter group Y's subjects:")
# TODO
Y = set()
a = input()
while a != "end":
    Y.add(a)
    a = input()

ls1 = list(X | Y)
ls2 = list(X & Y)
ls3 = list(Y - X)
ls4 = list(X ^ Y)

ls1.sort()
ls2.sort()
ls3.sort()
ls4.sort()

print(ls1)
print(ls2)
print(ls3)
print(ls4)