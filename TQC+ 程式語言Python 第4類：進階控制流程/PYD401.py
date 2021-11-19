# TODO
for n in range(10):
    value = eval(input())
    if n == 0:
        smallest = value
    if value < smallest:
        smallest = value

print(smallest)
