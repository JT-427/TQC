# TODO
n = eval(input())
if n < 10:
    for i in range(1, n+1, 1):
        for g in range(1, n+1, 1):
            print(g, '*', i, '=', format(i*g, '<2d'), end='  ')
        print('')