# TODO

matrix = []
for s in range(3):
    matrix.append([])
    if s == 0:
        print("The 1st student:")
    elif s == 1:
        print("The 2nd student:")
    else:
        print("The 3rd student:")
    for g in range(5):
        value = eval(input())
        matrix[s].append(value)

for s in range(3):
    average = sum(matrix[s])/len(matrix[s])
    print("Student", s+1)
    print("#Sum", sum(matrix[s]))
    print("#Average", format(average, ".2f"))


"""
The _ student:
Student _
#Sum _
#Average _
"""
