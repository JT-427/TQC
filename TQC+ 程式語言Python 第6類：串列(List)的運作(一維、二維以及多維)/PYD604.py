# TODO

ls = []

for i in range(10):
    value = eval(input())
    ls.append(value)

count = 0
for i in ls:
    now_count = 0
    for j in ls:
        if j==i:
            now_count += 1
    if count < now_count:
        count = now_count
        mn = i

print(mn)
print(count)