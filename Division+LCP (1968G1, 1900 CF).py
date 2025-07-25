import sys
import math 

input = sys.stdin.readline

modulo = (10**15)+37
base = 1009

polynomialpowers = []

for i in range(3*10**5): polynomialpowers.append(pow(base,i,modulo))

def hashdescend(string, powlist):
    powmount = len(string)-1; tot = 0
    for char in string:
        tot = (tot + ((ord(char) * powlist[powmount]) % modulo))%modulo
        powmount -= 1
    return tot

def ModifiedRabinKarp(teststring,pattern):
    LCPvar = 1
    lastpointer = len(pattern)-1
    if len(pattern)>len(teststring): return 0
    beginstr = teststring[:len(pattern)]
    patternnum = hashdescend(pattern,polynomialpowers); testnum = hashdescend(beginstr,polynomialpowers)
    for i in range(len(teststring)-len(pattern)):
        testnum = (modulo + testnum - ((ord(teststring[i])*polynomialpowers[len(pattern)-1]) % modulo)) % modulo
        testnum = (base*testnum)%modulo
        testnum = (testnum + ord(teststring[i+len(pattern)])) % modulo
        if testnum == patternnum and i >= lastpointer:
            lastpointer = i+len(pattern)
            LCPvar+=1
    return LCPvar

def LCPChecker(string,input, partitions):
    if ModifiedRabinKarp(string, string[:input]) >= partitions:
        return True
    return False

def binsearch(string,partitions):
    lo = 1
    hi = len(string)+1
    while lo != hi:
        
        mid = (lo+hi)//2
        if LCPChecker(string, mid, partitions):
            lo = mid+1
        else:
            hi = mid
    return lo-1


numcases= int(input().replace("\n",""))

for x in range(numcases):
    _,partitionlength,_ = [int(x) for x in input().replace("\n","").split()]
    print(binsearch(input().replace("\n",""), partitionlength))


