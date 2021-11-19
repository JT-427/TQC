# TODO

grade = eval(input())

while grade != -9999:
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("E")
    grade = eval(input())
