def Solve(part):
    with open("input5.txt") as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        total = 0
        bounds = inp[:inp.index("")]
        values = inp[inp.index("")+1:]
        for bound in range(len(bounds)):
            bounds[bound] = list(map(int, bounds[bound].split("-")))
        if part == 1:
            for value in values:
                for bound in bounds:
                    if bound[0] <= int(value) <= bound[1]:
                        total += 1
                        break
        else:
            NonOverlappingBounds = []
            bounds.sort(key=lambda x: x[0])
            for bound in bounds:
                for NBound in range(len(NonOverlappingBounds)): # I really should have chosen a shorter name
                    if NonOverlappingBounds[NBound][0] <= bound[0] <= NonOverlappingBounds[NBound][1] and bound[1] > NonOverlappingBounds[NBound][1]:
                        NonOverlappingBounds[NBound][1] = bound[1]
                        break
                    elif NonOverlappingBounds[NBound][0] <= bound[1] <= NonOverlappingBounds[NBound][1] and bound[0] < NonOverlappingBounds[NBound][0]:
                        NonOverlappingBounds[NBound][0] = bound[0]
                        break
                    elif bound[0] <= NonOverlappingBounds[NBound][0] and bound[1] >= NonOverlappingBounds[NBound][1]:
                        NonOverlappingBounds[NBound] = [bound[0], bound[1]]
                        break
                    elif NonOverlappingBounds[NBound][0] <= bound[1] <= NonOverlappingBounds[NBound][1] and NonOverlappingBounds[NBound][0] <= bound[0] <= NonOverlappingBounds[NBound][1]:
                        break
                else:
                    NonOverlappingBounds.append(bound)
            for bound in NonOverlappingBounds:
                total += bound[1] - bound[0] + 1
        print(total)

from os import system
system("cls")
Solve(1)
Solve(2)