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

class Line2():
    def __init__(self, lights, joltage, buttons, length):
        self.lights = lights
        self.joltage = joltage
        self.length = length
        self.buttons = buttons


        matrix = [[0 for a in range(len(buttons))] for b in range(len(joltage))]
        for button in range(len(buttons)):
            for a in buttons[button]:
                matrix[a][button] = 1
        for i in range(len(joltage)):
            matrix[i].insert(0, joltage[i])

        
        self.matrix = numpy.array(matrix)
        print(self.matrix)

def Add(arr1, arr2):
    for i in range(len(arr2)):
        arr1[i] += arr2[i]
    return arr1


from itertools import combinations, combinations_with_replacement
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

import numpy


def Pass2(Goal, Buttons, passes):
    if passes == 1:
        for i in Buttons:
            result = [0 for a in range(len(Goal))]
            for a in i:
                result[a] += 1
            if result == Goal:
                return True
    else:
        for attempt in combinations_with_replacement(Buttons, passes):
            result = [0 for a in range(len(Goal))]
            for i in attempt:
                for a in i: # Yes this is bad practice, but I'm really far behind
                    result[a] += 1
            if result == Goal:
                return True
    return False

def Solve(part):
    with open("input10.txt") as f:
        inp = list(map(lambda x: x.replace("\n", "").split(" "), f.readlines()))
        Lines = []
        for i in range(len(inp)):
            if part == 1:
                lights = "0b"
                for j in list(inp[i][0].strip("[]")):
                    lights += "1" if j == "#" else "0"
                length = len(lights)-2

            joltage = list(map(int, inp[i][-1].strip("{}").split(",")))
            buttons = list(map(lambda x: list(map(int, x.strip("()").split(","))), inp[i][1:-1]))

            if part == 1:
                Lines.append(Line(int(lights, 2), joltage, buttons, length))
            else:
                Lines.append(Line2(0, joltage, buttons, 0))
        total = 0
        for machine in Lines:
            count = 1
            running = True
            while running:
                if part == 1:
                    if Pass(machine.lights, machine.buttons, count):
                        total += count
                        break
                else:
                    if count == 1:
                        for a in range(len(machine.matrix)):
                            if (machine.matrix[a][1:] == [1 for c in range(len(machine.matrix[a])-1)]).all():
                                total += combo[0]
                                running = False
                                break
                        for a in range(len(machine.matrix)):
                            for b in range(a+1, len(machine.matrix)):
                                combo = Add(machine.matrix[a], machine.matrix[b])
                                if (combo[1:] == [1 for c in range(len(combo)-1)]).all():
                                    total += combo[0]
                                    running = False
                                    break
                    if running == True and Pass2(machine.joltage, machine.buttons, count):
                        total += count
                        break
                count += 1
            print(total)

Solve(2)