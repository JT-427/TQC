# TODO

while True:
    h = eval(input())
    if h == -9999:
        break
    w = eval(input())
    if w == -9999:
        break
    bmi = w/(0.01*h)**2
    print("BMI:", format(bmi, ".2f"))
    
    if bmi >= 30:
        msg = "fat"
    elif bmi >=25:
        msg = "over weight"
    elif bmi >=18.5:
        msg = "normal"
    else:
        msg = "under weight"
    print("State:", msg)


"""
fat
over weight
normal
under weight
BMI: _
State: _
"""