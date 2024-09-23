import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
output = sys.stdout.write
testnum = int(input().replace("\n",""))

def divisibilityrule(base,modulo):
    for x in range(modulo):
        char = pow(base,x+1,modulo)
        if char == 0:
            return (1,x+1)
        elif char == 1:
            return (2,x+1)
        elif char == modulo - 1:
            return (3,x+1)
    return (0,0)
        
for x in range(testnum):
    x,y = [int(x) for x in input().replace("\n","").split()]
    num = divisibilityrule(x,y)
    if num[0]!=0:
        output(str(num[0])+ " " + str(num[1])+"\n")
    else:
        output(str(0)+"\n")