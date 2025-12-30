from collections import defaultdict
from functools import cache
GraphDict: defaultdict = defaultdict(list)

@cache
def Recursion(node, Goal):
    global GraphDict
    if node == Goal:
        return 1
    newNodes = GraphDict[node]
    total = 0
    for newNode in newNodes:
        total += Recursion(newNode, Goal)
    return total

@cache
def Recursion2(node, Goal, DCheck, FCheck):
    global GraphDict
    if node == Goal:
        return 1 if DCheck and FCheck else 0
    
    if node == "dac":
        DCheck = True
    if node == "fft":
        FCheck = True
    newNodes = GraphDict[node]
    total = 0
    for newNode in newNodes:
        total += Recursion2(newNode, Goal, DCheck, FCheck)
    return total

def Solve(part):
    with open("input11.txt") as f:
        inp = list(map(lambda x: x.replace("\n", "").split(":"), f.readlines()))
        for i in range(len(inp)):
            inp[i][1] = inp[i][1][1:].split(" ")
        for item in inp:
            for value in item[1]:
                GraphDict[item[0]].append(value)
        if part == 1:
            print(Recursion("you", "out"))
        else:
            print(Recursion2("svr", "out", False, False))

Solve(2)      