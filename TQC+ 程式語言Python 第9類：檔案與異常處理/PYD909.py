f_name = "data.dat"
file = open(f_name, "w")

# TODO
for _ in range(5):
    a = input()
    file.write(a+"\n")
file.close()

print("The content of \"data.dat\":")
file = open(f_name, "r", encoding="utf-8")

for line in file:
    print(line)


"""
The content of "data.dat":
"""