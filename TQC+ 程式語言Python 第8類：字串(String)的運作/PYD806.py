# TODO

text = input()
s = input()

def compute(text, s):
    c = 0
    for t in text:
        if t == s:
            c+=1
    return c
count = compute(text, s)
print(f"{s} occurs {count} time(s)")



"""
_ occurs _ time(s)
"""
