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
    def __init__(self, Xjoltage, joltage, buttons, length):
        self.Xjoltage = Xjoltage
        self.joltage = joltage
        self.length = length
        self.buttons = buttons
        self.Xbuttons = []

        matrix = [[0 for a in range(len(buttons))] for b in range(len(joltage))]
        for button in range(len(buttons)):
            for a in buttons[button]:
                matrix[a][button] = 1
        for i in range(len(joltage)):
            matrix[i].insert(0, joltage[i])

        
        self.matrix = numpy.array(matrix, dtype=numpy.float64)

        for button in buttons:
            Xorable = ["0b"] + ["0" for i in range(length)]
            for num in button:
                Xorable[num+1] = "1"
            self.Xbuttons.append(int("".join(Xorable), 2))



def Add(arr1, arr2):
    for i in range(len(arr2)):
        arr1[i] += arr2[i]
    return arr1

def Subtract(arr1, arr2):
    for i in range(len(arr2)):
        arr1[i] -= arr2[i]
    return arr1

def SubtractJB(arr1, button):
    for a in button:
        arr1[a] -= 1
    return arr1

def Divide(arr1, linear):
    for a in range(len(arr1)):
        arr1[a] //= linear
    return arr1

def ItemsToIndexes(List:list, items:list):
    indexes = []
    for item in items:
        indexes.append(List.index(item))
    return indexes

from itertools import combinations, combinations_with_replacement, product
def Pass(Goal, Buttons, passes):
    if passes == 1:
        for i in Buttons:
            if Goal == i:
                return True, [i]
    else:
        for attempt in combinations(Buttons, passes):
            combo = attempt[0]
            for part in attempt[1:]:
                combo ^= part
            if combo == Goal:
                return True, attempt
    return False, 0

def PassWithReplacement(Goal, Buttons):
    correctattempts = []
    for attempt in product("01", repeat=len(Buttons)):
        combo = 0
        buttonattempt = []
        # if all(i == "0" for i in attempt):
        #     continue
        for i in range(len(attempt)):
            if attempt[i] == "1":
                buttonattempt.append(Buttons[i])
                combo ^= Buttons[i]
        if combo == Goal:
            correctattempts.append(buttonattempt)
    return correctattempts

def ListCheck(result, goal):
    for i in range(len(goal)):
        if result[i] > goal[i]:
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
                if ListCheck(result, Goal):
                    break
            if result == Goal:
                return True
    return False

def FindButtons(machine):
    count = 1
    if type(machine) == Line:
        while True:
            complete, buttons = Pass(machine.lights, machine.buttons, count)
            if complete:
                return count, ItemsToIndexes(machine.buttons, buttons)
            count += 1
    elif type(machine) == Line2:
        possibilities = []
        for i in range(len(machine.Xbuttons)):
            complete, buttons = Pass(machine.Xjoltage, machine.Xbuttons, count)
            if complete:
                possibilities.append((count, ItemsToIndexes(machine.Xbuttons, buttons)))
            count += 1
        return possibilities
    else:
        raise TypeError("AHHHHHHHHHHH")

def FindButtons2(Xjoltage, Xbuttons, buttons):
    possibilities = []
    foundbuttonsList = PassWithReplacement(Xjoltage, Xbuttons)
    for foundbuttons in foundbuttonsList:
        possibilities.append(ItemsToIndexes(Xbuttons, foundbuttons))
    return possibilities

# def DownDownDownDown(arr): # This is a function which continually divides by two.
#     modifier = 1
#     dividing = True
#     while dividing:
#         for a in arr:
#             if a % 2 == 1:
#                 dividing = False
#                 break
#         if dividing:
#             for a in range(len(arr)):
#                 arr[a] //= 2
#             modifier *= 2
#     return modifier, arr

def CheckEvenness(arr):
    for a in arr:
        if a % 2 == 1 or a < 0:
            return False
    return True

def LTS(arr):
    arr = list(map(str, arr))
    string = ""
    for part in arr:
        string += part + ","
    return string[:-1]

def LTS2(arr):
    arr = list(map(lambda x: list(map(str, x)), arr))
    string = ""
    for part in arr:
        for piece in part:
            string += piece + ","
        string = string[:-1]
        string += "|"
    return string[:-1]

def STL(string):
    list2 = string.split(",")
    list2 = list(map(int, list2))
    return list2

def STL2(string):
    list2 = string.split("|")
    list2 = list(map(lambda x: list(map(int, x.split(","))), list2))
    return list2

from functools import cache
@cache
def Recursion(joltage, Xbuttons, buttons):
    joltage = STL(joltage)
    Xbuttons = STL(Xbuttons)
    buttons = STL2(buttons)
    Xjoltage = int(CreateXJoltage(joltage), 2)
    if joltage == [0 for a in range(len(joltage))]:
        return 0

    possibilities = FindButtons2(Xjoltage, Xbuttons, buttons)
    resultnums = [1000000000000]
    for possibility in possibilities:
        newjoltage = list(joltage)
        for button in possibility:
            newjoltage = SubtractJB(newjoltage, buttons[button])
        if not CheckEvenness(newjoltage):
            continue
        newjoltage = Divide(newjoltage, 2)
        resultnums.append(2 * Recursion(LTS(newjoltage), LTS(Xbuttons), LTS2(buttons)) + len(possibility))
    return min(resultnums)
    


def CreateXJoltage(joltage):
    Xjoltage = "0b" # The X stands for Xorable which just means a binary number representing the lights
    for j in joltage:
        Xjoltage += "1" if j%2 == 1 else "0"
    return Xjoltage

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
            if part == 2:
                Xjoltage = "0b" # The X stands for Xorable which just means a binary number representing the lights
                for j in joltage:
                    Xjoltage += "1" if j%2 == 1 else "0"
                length = len(Xjoltage)-2

            buttons = list(map(lambda x: list(map(int, x.strip("()").split(","))), inp[i][1:-1]))

            if part == 1:
                Lines.append(Line(int(lights, 2), joltage, buttons, length))
            else:
                Lines.append(Line2(int(Xjoltage, 2), joltage, buttons, length))
        total = 0
        oldtotal = 0
        for machine in Lines:
            oldtotal = total
            if part == 1:
                total += FindButtons(machine)[0]
            else:
                # ##### Get rid of any buttons which will add up to 0.
                # for a in range(len(machine.matrix)):
                #     if machine.matrix[a][0] == 0:
                #         ToBeDeleted = []
                #         for b in range(1, len(machine.matrix[a])):
                #             if b == 1:
                #                 ToBeDeleted.append(b)
                #         deleted = 0
                #         for index in ToBeDeleted:
                #             machine.matrix = numpy.delete(machine.matrix, index-deleted, 1)
                #             deleted += 1
                #         machine.matrix = numpy.delete(machine.matrix, a, 0)
                running = True
                ##### Check if there's an obvious answer where you just get what the sum of all the button presses will be
                for a in range(len(machine.matrix)):
                    if (machine.matrix[a][1:] == [1 for c in range(len(machine.matrix[a])-1)]).all():
                        total += machine.matrix[a][0]
                        running = False
                        break
                if not running:
                    print(total-oldtotal)
                    continue

                ##### Check if we can combine two rows to get a full row.
                for a in range(len(machine.matrix)):
                    if not running:
                        break
                    for b in range(a+1, len(machine.matrix)):
                        combo = Add(machine.matrix[a], machine.matrix[b])
                        if (combo[1:] == [1 for c in range(len(combo)-1)]).all():
                            total += combo[0]
                            running = False
                            break
                
                # if numpy didn't work out:
                if not running:
                    print(total-oldtotal)
                    continue
                total += Recursion(LTS(machine.joltage), LTS(machine.Xbuttons), LTS2(machine.buttons))
            print(total-oldtotal)
        print(total)
Solve(2)