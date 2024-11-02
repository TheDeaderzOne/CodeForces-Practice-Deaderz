import sys

input = sys.stdin.readline
output = sys.stdout.write

TestCaseNum = int(input().replace("\n",""))
bist = []
core = 0
for x in range(TestCaseNum):
    tempbinrep = 0
    orlist = [0]*60
    u = int(input().replace("\n",""))
    testlist = [int(x) for x in input().replace("\n","").split()]
    const = sum(testlist)
    for x in testlist:
        tempbinrep |= x
        temp = x
        for x in range(60):
            if temp==0:
                break   
            elif temp&1 == 1:
                orlist[x]+=1
            temp>>=1
    counter = 0
    for ind in range(len(testlist)):
        tempchanges = testlist[ind]&tempbinrep
        factor = (const + testlist[ind]*len(testlist))%(((10**9)+7))
        tempory = (const)%(((10**9)+7))
        for u in range(60):
            if tempchanges == 0:
                break
            elif tempchanges&1 == 1:
                tempory += ((len(testlist)-orlist[u])*(2**u))%(((10**9)+7))
            tempchanges>>=1
        counter+=((factor-tempory)*tempory)
    output(str(counter%((10**9)+7))+"\n")