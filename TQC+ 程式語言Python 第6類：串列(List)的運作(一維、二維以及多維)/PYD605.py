# TODO

ls = []
for _ in range(10):
    value = eval(input())
    ls.append(value)

total = sum(ls) - max(ls) - min(ls)
avg = total/8

print(total)
print(round(avg, 2))