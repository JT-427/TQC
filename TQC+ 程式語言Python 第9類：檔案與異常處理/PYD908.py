f_name = input()
n = int(input())

# TODO
f = open(f_name, "r")

index = set()
data = []

for line in f:
    for w in line.split():
        index.add(w)
        data.append(w)

for i in sorted(index):
    if data.count(i) == n:
        print(i)

