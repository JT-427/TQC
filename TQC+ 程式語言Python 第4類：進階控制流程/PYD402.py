# TODO
value = 0
min_num = None
while value != 9999:
    value = eval(input())
    if min_num is None or min_num > value:
        min_num = value
print(min_num)
