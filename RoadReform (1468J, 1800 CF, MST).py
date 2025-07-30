import sys
import math

input = sys.stdin.readline
output = sys.stdout.write

testcasenum = int(input().replace("\n", ""))

for x in range(testcasenum):

    kruskallist = []

    size, roads, speedlimit = [int(x) for x in input().replace("\n", "").split()]

    parentnodes = [int(x) for x in range(size)]
    sizelist = [1] * size

    for _ in range(roads):
        x, y, z = [int(x) for x in input().replace("\n", "").split()]
        kruskallist.append([x - 1, y - 1, z])

    kruskallist.sort(key=lambda x: x[2])
    changes = 0
    change2 = 0
    roadnum = 0
    tempcurling = math.inf
    switchturn = True

    def UFFind(node):
        if node == parentnodes[node]:
            return node
        parentnodes[node] = UFFind(parentnodes[node])
        return parentnodes[node]

    def UFUnion(x, y):
        parentx = UFFind(x)
        parenty = UFFind(y)
        if parentx != parenty:
            if sizelist[parentx] > sizelist[parenty]:
                sizelist[parentx] += sizelist[parenty]
                parentnodes[parenty] = parentx
            else:
                sizelist[parenty] += sizelist[parentx]
                parentnodes[parentx] = parenty

    def UFEquals(edge1, edge2):
        return UFFind(edge1) != UFFind(edge2)

    for x in range(roads):
        if UFEquals(kruskallist[x][0], kruskallist[x][1]):
            UFUnion(kruskallist[x][0], kruskallist[x][1])
            roadnum += 1
            tempcurling = min(abs(speedlimit - kruskallist[x][2]), tempcurling)
            if kruskallist[x][2] >= speedlimit:
                changes += kruskallist[x][2] - speedlimit
                switchturn = False
                tempcurling = 0

        if roadnum == size - 1:
            if switchturn:
                tempcurling = min(abs(speedlimit - kruskallist[x][2]), tempcurling)

    changes += tempcurling

    output(str(changes) + "\n")
