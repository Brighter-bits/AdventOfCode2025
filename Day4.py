Dirs = ([-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]) # 0, 0 is the roll itself and so is not included in the list
def Add(grid, x, y):
    for dir in Dirs:
        try: 
            newY = y + dir[0] if y + dir[0] >= 0 else None
            newX = x + dir[1] if x + dir[1] >= 0 else None
            grid[newY][newX] += 1
        except: 
            continue
    return grid

def Pass(inp):
    numgrid = [[0 for i in range(len(inp[0]))] for b in range(len(inp))]
    rollCoords = []
    for x in range(len(inp[0])):
        for y in range(len(inp)):
            if inp[y][x] == "@":
                rollCoords.append((x, y))
                numgrid = Add(numgrid, x, y)
    return numgrid, rollCoords
    
def Delete(numgrid, rollCoords):
    answer = 0
    deadCoords = []
    for roll in rollCoords:
        if numgrid[roll[1]][roll[0]] < 4:
            answer += 1
            deadCoords.append((roll[0], roll[1]))
    return answer, deadCoords

def Solve(part):
    with open("input4.txt") as f:
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        # for i in range(len(numgrid)):
        #     numgrid[i] = list(map(str, numgrid[i]))
        # for i in numgrid:
        #     print("".join(i)) 
        total = 0
        if part == 1:
            numgrid, rollCoords = Pass(inp)
            total, _ = Delete(numgrid, rollCoords)
        else:
            while True:
                numgrid, rollCoords = Pass(inp)
                answer, deadCoords = Delete(numgrid, rollCoords)
                if answer == 0:
                    break
                total += answer
                for roll in deadCoords:
                    inp[roll[1]][roll[0]] = "."
        print(total)

from os import system
system("cls")
Solve(1)
Solve(2)