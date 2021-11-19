# TODO

text = input()

if len(text) > 7:
    if text.isalnum():
        check = 0
        for i in text:
            if i.isupper():
                check += 1
        if check > 0:
            print("Valid password")
        else:
            print("Invalid password")
    else:
        print("Invalid password")
else:
    print("Invalid password")



"""
Valid password
Invalid password
"""