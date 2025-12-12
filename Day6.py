import regex as re
import numpy as np
from math import prod
def CalcLine(nums, sym) -> int:
    nums = list(map(int, nums))
    if sym == "*": 
        return prod(nums)
    elif sym == "+": 
        return sum(nums)
    else: 
        raise ValueError("That doesn't look good at all.")


def Solve(part):
    with open("input6.txt") as f:
        total = 0
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        if part == 1:
            inp = list(map(lambda x: re.sub(r" +", ",", x, 9999).split(","), inp))
            inp = list(map(lambda x: [part for part in x if part != ""], inp))
            inp = np.array(inp).T
            for line in inp:
                total += CalcLine(line[:-1], line[-1])
        else:
            inp = np.array(list(map(lambda x: list(x), inp))).T
            inp = list(map(lambda x: "".join(x), inp))
            inp = list(map(lambda x: re.sub(r" +", "", x, 9999), inp))
            
            line = []
            symbol = ""
            for part in inp:
                if part == "":
                    total += CalcLine(line, symbol)
                    line = []
                    symbol = ""
                    continue
                if line == []:
                    line.append(part[:-1])
                    symbol = part[-1]
                else:
                    line.append(part)
            total += CalcLine(line, symbol)        
        print(total)

from os import system as sys
sys("cls")
Solve(1)
Solve(2)