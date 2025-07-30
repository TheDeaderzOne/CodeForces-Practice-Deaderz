import sys

input = sys.stdin.readline
output = sys.stdout.write

StringLength = int(input().replace("\n", ""))

FirstWordList = [ord(char) - 96 for char in list(input().replace("\n", ""))]

SecondWordList = [ord(char) - 96 for char in list(input().replace("\n", ""))]

Taker = []


def BackWardsWorker(takerlist, firstwordarr, secondwordarr, stringlen):
    commonpointer = stringlen - 1
    if int((firstwordarr[commonpointer] + secondwordarr[commonpointer]) / 2) >= 14:
        takerlist.append(1)
    else:
        takerlist.append(0)
    commonpointer -= 1
    while commonpointer > -1:
        if (firstwordarr[commonpointer] + secondwordarr[commonpointer]) & 1 == 1:
            if takerlist[-1] == 0:
                if int((firstwordarr[commonpointer] + secondwordarr[commonpointer]) // 2) >= 14:
                    takerlist.append(1)
                else:
                    takerlist.append(0)
            else:
                if int(((firstwordarr[commonpointer] + secondwordarr[commonpointer]) // 2) + 1) >= 14:
                    takerlist.append(1)
                else:
                    takerlist.append(0)
        else:
            if int((firstwordarr[commonpointer] + secondwordarr[commonpointer]) / 2) >= 14:
                takerlist.append(1)
            else:
                takerlist.append(0)
        commonpointer -= 1
    takerlist.reverse()
    return takerlist


BackWardsWorker(Taker, FirstWordList, SecondWordList, StringLength)

FinalWord = []


def MedianTaker(stringlen, firstwordlist, secondwordlist, takerlist):
    commonpointer = 0
    initadder = 0
    while commonpointer != stringlen:
        if (firstwordlist[commonpointer] + secondwordlist[commonpointer]) & 1 == 0:
            FinalWord.append(int(((firstwordlist[commonpointer] + secondwordlist[commonpointer]) / 2) + initadder))
            initadder = 0
        elif (firstwordlist[commonpointer] + secondwordlist[commonpointer]) & 1 == 1:
            if takerlist[commonpointer + 1] == 1:
                FinalWord.append(
                    int(((firstwordlist[commonpointer] + secondwordlist[commonpointer]) // 2) + initadder + 1)
                )
                initadder = -13
            else:
                FinalWord.append(int(((firstwordlist[commonpointer] + secondwordlist[commonpointer]) // 2) + initadder))
                initadder = 13
        commonpointer += 1

    return [chr(x + 96) for x in FinalWord]


tempstr = "".join(MedianTaker(StringLength, FirstWordList, SecondWordList, Taker))

output(str(tempstr) + "\n")
