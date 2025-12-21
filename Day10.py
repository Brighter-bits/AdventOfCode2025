from copy import deepcopy
class Line():
    def __init__(self, lights, joltage, buttons, length):
        self.lights = lights
        self.joltage = joltage
        self.length = length
        tempbuttons = deepcopy(buttons)
        self.buttons = []
        for button in tempbuttons:
            Xorable = ["0b"] + ["0" for i in range(length)]
            for num in button:
                Xorable[num+1] = "1"
            self.buttons.append(int("".join(Xorable), 2))

from itertools import combinations
def Pass(Goal, Buttons, passes) -> bool:
    if passes == 1:
        for i in Buttons:
            if Goal == i:
                return True
    else:
        for attempt in combinations(Buttons, passes):
            combo = attempt[0]
            for part in attempt[1:]:
                combo ^= part
            if combo == Goal:
                return True
    return False

def Solve(part):
    with open("input10.txt") as f:
        inp = list(map(lambda x: x.replace("\n", "").split(" "), f.readlines()))
        Lines: list[Line] = []
        for i in range(len(inp)):
            lights = "0b"
            for j in list(inp[i][0].strip("[]")):
                lights += "1" if j == "#" else "0"
            length = len(lights)-2
            joltage = list(map(int, inp[i][-1].strip("{}").split(",")))
            buttons = list(map(lambda x: list(map(int, x.strip("()").split(","))), inp[i][1:-1]))
            Lines.append(Line(int(lights, 2), joltage, buttons, length))
        total = 0
        for machine in Lines:
            count = 1
            while True:
                if Pass(machine.lights, machine.buttons, count):
                    total += count
                    break
                count += 1
        print(total)
Solve(1)