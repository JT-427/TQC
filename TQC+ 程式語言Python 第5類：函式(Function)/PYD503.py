# TODO

def compute(a, b):
    sum = 0
    for i in range(a, b+1):
        sum += i
    return sum

def main():
    n1 = eval(input())
    n2 = eval(input())
    print(compute(n1, n2))
main()    