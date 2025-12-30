from math import prod
def Solve(part):
    with open("input12.txt") as f:
        # IDK. uhhh. I'm not doing this programatically.
        inp = f.read().split("\n\n")
        Trees = inp[-1].split("\n")
        EvenPackingSpaces = [18, 13, 15, 14, 12, 17] # I'm just eyeballing it, this is for two mushed together
        OddPackingSpaces = [9, 7, 9, 7, 8, 9] # This is for one on it's own.
        GridTrees = []
        total = 0 # total = 1 (Why did I do that?????????????????)
        for i in range(len(Trees)):
            Area, Amounts = Trees[i].split(":")
            Area = prod(list(map(int, Area.split("x"))))
            Amounts = list(map(int, Amounts[1:].split(" ")))
            GridTrees.append((Area, Amounts))
        for i in range(len(GridTrees)):
            TreeSum = sum([(GridTrees[i][1][x]//2) * EvenPackingSpaces[x] for x in range(len(EvenPackingSpaces))] + [(GridTrees[i][1][x]%2) * OddPackingSpaces[x] for x in range(len(EvenPackingSpaces))])
            if TreeSum < GridTrees[i][0]:
                total += 1
        print(total)
Solve(1)