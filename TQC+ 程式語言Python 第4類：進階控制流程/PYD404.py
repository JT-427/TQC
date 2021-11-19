# TODO
val = input()

reverse_val = ""
for i in range(-1, -len(val)-1, -1):
    reverse_val += val[i]
print(reverse_val)