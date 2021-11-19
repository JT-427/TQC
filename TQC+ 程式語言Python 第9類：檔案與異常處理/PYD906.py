f_name = input()
str_old = input()
str_new = input()
#TODO

f = open(f_name, "r")

print("=== Before the replacement")
# TODO
data = f.read()
print(data)
f.close()

print("=== After the replacement")

# TODO
f = open(f_name, "w")
data = data.replace(str_old, str_new)
f.write(data)
print(data)
f.close