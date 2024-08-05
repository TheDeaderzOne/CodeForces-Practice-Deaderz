import sys

input = sys.stdin.readline
output = sys.stdout.write

vertexnumber = int(input().replace("\n",""))

pairsgeo = []

def aero():

    if vertexnumber & 1 == 1:
        return "NO"

    else:

        for _ in range(vertexnumber):
            pairsgeo.append([int(x) for x in input().replace("\n","").split()])

        for hu in range(vertexnumber>>1):
            norm = (abs(pairsgeo[hu][0]-pairsgeo[hu+1][0]),abs(pairsgeo[hu][1]-pairsgeo[hu+1][1]))
            buzarro = (abs(pairsgeo[hu-(vertexnumber>>1)][0]-pairsgeo[hu-(vertexnumber>>1)+1][0]),abs(pairsgeo[hu-(vertexnumber>>1)][1]-pairsgeo[hu-(vertexnumber>>1)+1][1]))
            if norm!=buzarro:
                return "NO"
        
        return "YES"

output(str(aero())+"\n")
