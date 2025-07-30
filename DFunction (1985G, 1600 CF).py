import sys
import math

input = sys.stdin.readline

numcases = int(input().replace("\n", ""))

for x in range(numcases):
    l, r, k = [int(x) for x in input().replace("\n", "").split()]
    if k >= 10:
        print(0)
    else:
        tempvar = 0
        if 10 % k == 0:
            tempvar = 10 // k
        else:
            tempvar = (10 // k) + 1
        print((pow(tempvar, r, 10**9 + 7) - pow(tempvar, l, 10**9 + 7) + 10**9 + 7) % (10**9 + 7))
