def FindLetter(Letter, grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == Letter:
                return (x, y)

def LTS(list):
    string = ""
    for part in list:
        for piece in part:
            string += piece + "|"
        string = string[:-1]
        string += ","
    return string[:-1]

def STL(string):
    list2 = string.split(",")
    list2 = list(map(lambda x: x.split("|"), list2))
    return list2

SplitDict = dict()
Bottoms = set()
from functools import cache

@cache
def Fall(grid, start):
    grid = STL(grid)
    x = start[0]
    y = start[1]
    timelines = 0
    while True:
        if grid[y][x] == "^":
            SplitDict[(x, y)] = True
            timelines += Fall(LTS(grid), (x-1, y))
            timelines += Fall(LTS(grid), (x+1, y))
            return timelines
        if y == len(grid)-1:
            Bottoms.add((x, y))
            return 1
        y += 1



def Solve():
    with open("input7.txt") as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        Start = FindLetter("S", inp)
        P2 = Fall(LTS(inp), Start)
        print(len(SplitDict))
        print(P2)

Solve()

