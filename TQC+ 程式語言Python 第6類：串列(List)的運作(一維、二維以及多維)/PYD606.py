# TODO

row = eval(input())
col = eval(input())

def compute(row, col):
    ls = []
    for r in range(row):
        ls.append([])
        for c in range(col):
            ls[r].append(c-r)
    return ls

ls = compute(row, col)

for i in ls:
    for j in i:
        print(format(j, ">4d"), end="")
    print("")