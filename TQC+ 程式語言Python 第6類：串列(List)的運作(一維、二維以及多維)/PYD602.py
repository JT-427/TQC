# TODO

numbers = []

for i in range(5):
    value = input()
    if value.upper() == "J":
        numbers.append(11)
    elif value.upper() == "Q":
        numbers.append(12)
    elif value.upper() == "K":
        numbers.append(13)
    elif value.upper() == "A":
        numbers.append(1)
    else:
        numbers.append(int(value))
print(sum(numbers))