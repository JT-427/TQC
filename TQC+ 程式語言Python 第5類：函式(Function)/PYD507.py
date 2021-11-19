def compute(x):
    count = 0
    for i in range(1, x):
        if x%i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False

def main():
    x = eval(input())
    if compute(x):
        print("Prime")
    else:
        print("Not Prime")
main()