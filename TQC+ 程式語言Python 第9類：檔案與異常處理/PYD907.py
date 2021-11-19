# TODO
name = input()
f = open(name, "r")
lines = 0
words = 0
chars = 0

for line in f:
    lines += 1

    words += len(line.split())

    s = line.strip()
    s = s.replace(" ","")
    chars += len(s)

print(f"{lines} line(s)")
print(f"{words} word(s)")
print(f"{chars} character(s)")

"""
_ line(s)
_ word(s)
_ character(s)     
"""