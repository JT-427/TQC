# TODO
y = eval(input())

while y != -9999:
    if y % 400 == 0:
        print(f"{y} is a leap year.")
    else:
        if y % 100 != 0 and y % 4 == 0:
            print(f"{y} is a leap year.")
        else:
            print(f"{y} is not a leap year.")
    y = eval(input())



"""
_ is a leap year.
_ is not a leap year.
"""
