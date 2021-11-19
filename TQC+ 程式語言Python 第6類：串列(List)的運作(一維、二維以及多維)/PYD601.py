# TODO

numbers = []
sum = 0
for i in range(12):
    value = eval(input())
    numbers.append(value)
    if i%2 == 0:
        sum += numbers[i]

for j in range(12):
    if j==0 or j%3 != 0:
        print(format(numbers[j], ">3d"), end="")
    else:
        print()
        print(format(numbers[j], ">3d"), end="")
print()
print(sum)