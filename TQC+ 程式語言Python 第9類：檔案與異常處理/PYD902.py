f = open("read.txt")
# TODO
s = f.read()

numbers = [int(x) for x in s.split(" ")]

print(sum(numbers))