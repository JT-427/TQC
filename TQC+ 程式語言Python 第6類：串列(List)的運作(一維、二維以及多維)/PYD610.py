#TODO

matrix = []
for i in range(4):
    print(f"Week {i+1}:")
    matrix.append([])
    for g in range(3):
        print(f"Day {g+1}:", end="")
        value = eval(input())
        matrix[i].append(value)

sum_of_temp = 0
max_of_temp = None
min_of_temp = None
for a in matrix:
    for b in a:
        if max_of_temp is None or b > max_of_temp:
            max_of_temp = b
        if min_of_temp is None or b < min_of_temp:
            min_of_temp = b
        sum_of_temp += b

print("Average:", round(sum_of_temp/12, 2))
print("Highest:", max_of_temp)
print("Lowest:", min_of_temp)






"""
Week _:
Day _: 
Average: _
Highest: _
Lowest: _
"""