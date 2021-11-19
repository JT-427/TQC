# TODO


num = eval(input())

if num %3 == 0 and num %5 == 0:
    print(num, "is a multiple of 3 and 5.")
elif num %3 == 0 :
    print(num, "is a multiple of 3.")
elif num %5 == 0 :
    print(num, "is a multiple of 5.")
else:
    print(num, "is not a multiple of 3 or 5.")

"""
_ is a multiple of 3 and 5.
_ is a multiple of 3.
_ is a multiple of 5.
_ is not a multiple of 3 or 5.
"""