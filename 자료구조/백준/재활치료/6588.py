import sys
import math
primelist = [1]*1000001
for i in range(2, 1001):
    if primelist[i] == 1:
        for j in range(i+i, 1000000, i):
            if primelist[j] == 1:
                primelist[j] = 0

while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break
    for i in range(3, num):
        if primelist[i] and primelist[num-i] == 1:
            print(num,'=',i,'+',(num-i))
            break