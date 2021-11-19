#TODO

matrix1 = []
print("Enter matrix 1:")
#TODO
for i in range(2):
    matrix1.append([])
    for j in range(2):
        #置於迴圈內，依給定之格式輸出
        print("[%d, %d]: " % (i+1, j+1), end = '')
        value = eval(input())
        matrix1[i].append(value)


matrix2 = []
print("Enter matrix 2:")
#TODO
for i in range(2):
    matrix2.append([])
    for j in range(2):
        #置於迴圈內，依給定之格式輸出
        print("[%d, %d]: " % (i+1, j+1), end = '')
        value = eval(input())
        matrix2[i].append(value)




print("Matrix 1:")
#TODO
for i in matrix1:
    for g in i:
        print(g, end=" ")
    print()
print("Matrix 2:")
#TODO
for i in matrix2:
    for g in i:
        print(g, end=" ")
    print()
print("Sum of 2 matrices:")
#TODO
for i, g in zip(matrix1, matrix2):
    for x, y in zip(i, g):
        print(x+y, end=" ")
    print()
