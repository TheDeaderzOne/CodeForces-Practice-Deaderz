import sys

input = sys.stdin.readline
output = sys.stdout.write

testcases = int(input().replace("\n", ""))

arrgy = []

for x in range(testcases):
    arrgy.append(int(input().replace("\n", "")))

for x in range(len(arrgy)):
    if arrgy[x] & 1 == 1:
        output("Bob" + "\n")
    else:
        if (arrgy[x] & (-1 * arrgy[x])) == arrgy[x]:
            counts = 0
            tempholder = int(arrgy[x])
            while (tempholder >> 1) > 0:
                counts += 1
                tempholder >>= 1

            if counts & 1 == 0:
                output("Alice" + "\n")
            else:
                output("Bob" + "\n")

        else:
            output("Alice" + "\n")
