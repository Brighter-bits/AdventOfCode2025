import regex as re
from itertools import product
def findmax1(string:str):
    for i in range(9, 0, -1):
        for j in range(9, 0, -1):
            if re.match(f".*{str(i)}.*{str(j)}", string) != None:
                return str(i) + str(j)

def findmax2(line:str):
    maximumIndex = len(line)
    indexes = []
    for i in range(9, 0, -1):
        if line.find(str(i)) != -1 and line.find(str(i)) < maximumIndex-11:
            for char in range(len(line)-11):
                if line[char] == str(i):
                    indexes.append(char)
            break
    possibilities = []
    for index in indexes:
        LastChars = list(line[index+1:])
        candidate = line[index]
        while True:
            if len(candidate) == 12:
                break
            if 12-len(candidate) == len(LastChars):
                candidate += "".join(LastChars)
                break
            x = LastChars[:len(LastChars)-(11-len(candidate))]
            nextNum = max(LastChars[:len(LastChars)-(11-len(candidate))])
            candidate += (nextNum)
            LastChars = LastChars[LastChars.index(nextNum)+1:]
        possibilities.append(candidate)
    return max(list(map(int, possibilities)))
    


def Solve(part):
    with open("input3.txt") as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        total = 0
        if part == 1:
            for line in inp:
                total += int(findmax1(line))
        else:
            for line in inp:
                total += int(findmax2(line))
        print(total)

import os
os.system("cls")
Solve(1)
Solve(2)