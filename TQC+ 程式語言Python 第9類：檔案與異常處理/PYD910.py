f_name = "read.dat"
# TODO
file = open(f_name, "r", encoding="utf-8")

f = 0
m = 0
for line in file:
    print(line)
    x = line.split()
    if x[2] == '0':
        f += 1
    elif x[2] == "1":
        m += 1

print("Number of males:", m)
print("Number of females:", f)

"""
Number of males: _
Number of females: _
"""