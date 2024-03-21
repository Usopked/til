'''array = []
num = int(input())
while num:
    a, b = input().split()
    b = int(b)
    if a == 'add' and b not in array:
        array.append(b)
    elif a == 'remove' and b in array:
        array.remove(b)
    elif a == 'check':
        if b in array: print("1")
        else: print("0")
    elif a == 'toggle':
        if b in array: array.remove(b)
        else: array.append(b)
    elif a == 'all':
        array = []
        for i in range(20):
            array.append(i)
    elif a == 'empty':
        array = []
    num -= 1
'''

import sys

M = int(sys.stdin.readline())
S = 0

for _ in range(M):
    op = sys.stdin.readline().strip().split()

    if len(op) == 1:
        if op[0] == "all":
            S = (1<<21) - 1
        else:
            S = 0
    else:
        op, x = op[0], int(op[1])
        if op == "add":
            S |= (1 << x)
        elif op == "remove":
            S &= ~(1 << x)
        elif op == "check":
            res = (S & (1 << x)) >> x
            print(res)
        elif op == "toggle":
            S ^= (1 << x)
