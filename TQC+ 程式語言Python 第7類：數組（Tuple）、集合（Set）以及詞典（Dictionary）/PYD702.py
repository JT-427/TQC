# TODO

print("Create tuple1:")
# TODO
a = eval(input())
ls_1 = []
while a != -9999:
    ls_1.append(a)
    a = eval(input())

print("Create tuple2:")
# TODO
b = eval(input())
ls_2 = []
while b != -9999:
    ls_2.append(b)
    b = eval(input())
ls_3 = ls_1+ls_2
print("Combined tuple before sorting:", tuple(ls_3))
ls_3.sort()
print("Combined list after sorting:", ls_3)


"""
Combined tuple before sorting: _
Combined list after sorting: _
"""
