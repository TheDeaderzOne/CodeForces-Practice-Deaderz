import sys

input = sys.stdin.readline
output = sys.stdout.write
TestCaseInt = int(input().replace("\n", ""))
BruhArr = []

for _ in range(TestCaseInt):
    BruhArr.append(int(input().replace("\n", "")))


def ArrMaker(Length):
    if Length & 1 == 0:
        FirstLen = int(Length // 2)
        SecondLen = int(Length // 2)
    else:
        FirstLen = int(Length // 2) + 1
        SecondLen = int(Length // 2)

    if Length == 3:
        return [1, 3, 2]

    FirstLenList = []
    SecondLenList = []

    for k in range(FirstLen):
        FirstLenList.append(k + 1)
    if FirstLen > SecondLen:
        FirstLenList[-1] = 2**18

    rangeshorter = 0

    if SecondLen & 1 == 1:
        rangeshorter = 2

    for j in range(SecondLen):
        if j < SecondLen - rangeshorter:
            SecondLenList.append((2**21) + (2**20) + FirstLenList[j])
        elif j == SecondLen - rangeshorter:
            SecondLenList.append((2**21) + FirstLenList[j])
        elif j == SecondLen - rangeshorter + 1:
            SecondLenList.append((2**20) + FirstLenList[j])

    if FirstLen > SecondLen:
        SecondLenList[-1] += FirstLenList[-1]

    FinalList = []
    teek1 = 0
    teek2 = 0

    for x in range(Length):
        if x & 1 == 0:
            FinalList.append(FirstLenList[teek1])
            teek1 += 1
        else:
            FinalList.append(SecondLenList[teek2])
            teek2 += 1

    return FinalList


for x in BruhArr:
    for u in ArrMaker(x):
        output(str(u) + " ")
    output("\n")
