import sys

input = sys.stdin.readline

rocknum, scissornum, papernum = [int(x) for x in input().replace("\n", "").split()]
statenum = []

for i in range(101):
    tex = []
    for j in range(101):
        tex.append([])
        for k in range(101):
            tex[j].append([])
    statenum.append(tex)


def returns(rock, scissor, paper, coord, rockpaperconst, rockscissorconst, scissorpaperconst, total):
    return (
        rockpaperconst * statenum[rock - 1][scissor][paper][coord]
        + rockscissorconst * statenum[rock][scissor - 1][paper][coord]
        + scissorpaperconst * statenum[rock][scissor][paper - 1][coord]
    ) / (total)


def statemaker():
    for rock in range(101):
        for scissor in range(101):
            for paper in range(101):
                if rock == 0:
                    statenum[0][scissor][paper] = [0, 1, 0]
                elif scissor == 0:
                    statenum[rock][0][paper] = [0, 0, 1]
                elif paper == 0:
                    statenum[rock][scissor][0] = [1, 0, 0]
                else:
                    total = rock * scissor + rock * paper + paper * scissor
                    rockpaper = rock * paper
                    rockscissor = rock * scissor
                    paperscissor = paper * scissor
                    statenum[rock][scissor][paper] = [
                        returns(rock, scissor, paper, 0, rockpaper, rockscissor, paperscissor, total),
                        returns(rock, scissor, paper, 1, rockpaper, rockscissor, paperscissor, total),
                        returns(rock, scissor, paper, 2, rockpaper, rockscissor, paperscissor, total),
                    ]
    return statenum


statemaker()

for x in range(3):
    statenum[rocknum][scissornum][papernum][x] = str(statenum[rocknum][scissornum][papernum][x])

huy = " ".join(statenum[rocknum][scissornum][papernum])

print(huy)
