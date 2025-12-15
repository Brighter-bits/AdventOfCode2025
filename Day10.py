def Solve(part):
    with open("input10.txt") as f:
        inp = list(map(lambda x: x.replace("\n", "").split(" "), f.readlines()))
        for i in range(len(inp)):
            print(inp[i])

Solve(1)