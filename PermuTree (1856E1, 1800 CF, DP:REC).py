import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline; input()
treelist = [int(x) for x in input().replace("\n","").split()]
alist = []; nodeheights = [0]*(len(treelist)+1)
for j in range(len(treelist)+1):
    alist.append([])
for x in range(len(treelist)):
    alist[treelist[x]-1].append(x+1)
    
def knapsackbiggest(arr):
    tot = sum(arr)
    possible = [False]*((tot//2) + 1)
    possible[0] = True
    for k in range(len(arr)):
        for x in range(len(possible)-1,-1,-1):
            if possible[x] and x+arr[k] <= len(possible)-1:
                possible[x+arr[k]] = True
    for f in range(len(possible)-1,-1,-1):
        if possible[f]:
            return f*(tot-f)
        
def height(adjlist,startnode):
    sum = 0
    for node in adjlist[startnode]:
        sum+=height(adjlist,node)
    nodeheights[startnode] = sum+1
    return sum+1

totalnum = 0
height(alist,0)

for i in range(len(alist)):
    for j in range(len(alist[i])):
        alist[i][j] = nodeheights[alist[i][j]]
        
for x in range(len(alist)):
    if len(alist[x])>0:
        totalnum += knapsackbiggest(alist[x])

print(totalnum)