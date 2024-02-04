import sys
input = sys.stdin.readline
output = sys.stdout.write
TestCases = int(input().replace("\n","")); lengthsy = []; listoflists = []; prefixsumlist = []

for _ in range(TestCases):
    lengthsy.append(int(input().replace("\n",""))*2)
    z = [int(x) for x in input().replace("\n","").split()]
    z.sort()
    listoflists.append(z)

def checks(setty,lengthlist,psumlist,index):
    if lengthlist[index]!=len(setty[index]) or len(set(setty[index]))!=(lengthlist[index]/2):
        return False
    psumlist = []
    point = len(setty[index])-1
    psumpointer = 0
    lengthlistmore = int(lengthlist[index]/2)
    tracks = 0
    while lengthlistmore>0:
        if point != len(setty[index])-1 and setty[index][point]==setty[index][point+1]:
            tracks+=1
            if tracks>1:
                return False
            point-=1
        else:
            tracks = 0
            if setty[index][point] % 2 == 1:
                return False
            if len(psumlist)==0:
                if (setty[index][point])%(2*lengthlistmore) == 0:
                    psumlist.append(setty[index][point]/(2*lengthlistmore))
                else:
                    return False
                point-=1
                lengthlistmore-=1
            else:
                texy = setty[index][point]-(2*psumlist[psumpointer])
                if (texy)%(2*lengthlistmore) == 0:
                    tempu = int(texy/(2*lengthlistmore))
                else:
                    return False
                if tempu>0:
                    psumlist.append(psumlist[psumpointer]+tempu)
                else:
                    return False
                psumpointer+=1
                lengthlistmore-=1
                point-=1
    if point>0:
        return False
    return True

for h in range(TestCases):
    foo = checks(listoflists,lengthsy,prefixsumlist,h)
    if foo:
        output(str("YES")+"\n")
    else:
        output(str("NO")+"\n")