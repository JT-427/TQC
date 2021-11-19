# TODO
text = input()
ls = text.split("-")

check = 0
for c, i in enumerate(ls):
    len = 3 if c == 0 else 2 if c == 1 else 4
    if i.isdigit():
        check += 1
    else:
        check = 0
        break

if check != 0:
    print("Valid SSN")
else:
    print("Invalid SSN")


"""
Valid SSN
Invalid SSN
"""