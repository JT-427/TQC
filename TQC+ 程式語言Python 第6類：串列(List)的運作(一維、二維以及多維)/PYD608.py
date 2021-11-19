# TODO

matrix = []

for r in range(3):
    matrix.append([])
    for c in range(3):
        value = eval(input())
        matrix[r].append(value)

largest = matrix[0][0]
smallest = matrix[0][0]

index_largest = (0, 0)
index_smallest = (0, 0)

for r in range(3):
    for c in range(3):
        if matrix[r][c] > largest:
            largest = matrix[r][c]
            index_largest = (r, c)
        if matrix[r][c] < smallest:
            smallest = matrix[r][c]
            index_smallest = (r, c)

print("Index of the largest number", largest, "is:", index_largest)
print("Index of the smallest number", smallest, "is:", index_smallest)


"""
Index of the largest number _ is: (_, _)
Index of the smallest number _ is: (_, _)
"""