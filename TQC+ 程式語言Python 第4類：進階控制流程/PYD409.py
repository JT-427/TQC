# TODO
no_1 = 0
no_2 = 0
no = 0
for _ in range(5):
    sel = input()
    if sel == '1':
        no_1 += 1
    elif sel == '2':
        no_2 += 1
    else:
        no += 1
    print("Total votes of No.1: Nami = ", no_1)
    print("Total votes of No.2: Chopper = ", no_2)
    print("Total null votes = ", no)

if no_2 > no_1:
    print("=> No.2 Chopper won the election.")
elif no_1 > no_2:
    print("=> No.1 Nami won the election.")
else:
    print("=> No one won the election.")

"""
Total votes of No.1: Nami = _
Total votes of No.2: Chopper = _
Total null votes = _

=> No.1 Nami won the election.
=> No.2 Chopper won the election.
=> No one won the election.
"""
