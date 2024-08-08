import sys
import math

sys.setrecursionlimit(10**5); TestCaseNum = int(input().replace("\n",""))

monthsinayear = [0]*TestCaseNum; daysinamonth = [0]*TestCaseNum; daysinaweek = [0]*TestCaseNum

for x in range(TestCaseNum):
    monthsinayear[x],daysinamonth[x],daysinaweek[x] = [int(j) for j in input().replace("\n","").split()]

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def solver(yearmonths,monthdays,weekdays):

    summationofweird = 0

    realcoefficient = (monthdays-1)%weekdays

    totaltests = min(monthdays,yearmonths)

    increment = int(weekdays/gcd(realcoefficient,weekdays))
    
    counting = (totaltests)%increment

    n = (totaltests-1)//increment
    summationofweird += (n*counting)
    n = (totaltests-1-counting)//increment
    summationofweird += ((((n)*(n+1))*increment)>>1)

    return int(summationofweird)

for x in range(TestCaseNum):
    print(solver(monthsinayear[x],daysinamonth[x],daysinaweek[x]))
