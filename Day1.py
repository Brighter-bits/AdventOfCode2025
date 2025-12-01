def Solve1():
    with open("input1.txt") as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        position = 50
        total = 0
        for instruct in inp:
            turns = int(instruct[1:])
            if instruct[0] == "L":
                position = (position - turns) % 100
            else:
                position = (position + turns) % 100
            if position == 0:
                total += 1
        print(total)

def Solve2():
    with open("input1.txt") as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        position = 50
        total = 0
        for instruct in inp:
            turns = int(instruct[1:])
            if instruct[0] == "L":
                for i in range(turns):
                    position = (position - 1) % 100
                    if position == 0:
                        total += 1
            else:
                for i in range(turns):
                    position = (position + 1) % 100
                    if position == 0:
                        total += 1 
        print(total)

Solve1()
Solve2()