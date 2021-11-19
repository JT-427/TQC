f_name = input()
string = input()
# TODO
f = open(f_name, "r")

print("=== Before the deletion")
# TODO
data = f.read()
print(data)
f.close()

print("=== After the deletion")

# TODO
f = open(f_name, "w")
data = data.replace(string, "")
f.write(data)
print(data)
f.close