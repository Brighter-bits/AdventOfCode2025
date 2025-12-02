from math import ceil, floor
def Solve(part):
    with open("input2.txt") as f:
        inp = f.readline().replace("\n", "").split(",")
        totals = []
        for bounds in inp:
            bounds = bounds.split("-")
            if part == 1:
                if len(bounds[0]) % 2 == 1:
                    if len(bounds[0]) == len(bounds[1]):
                        continue
                    bounds[0] = "".join(["1"] + ["0" for i in range(len(bounds[0]))])
                if len(bounds[1]) % 2 == 1:
                    bounds[1] = "".join(["9" for i in range(len(bounds[1])-1)])
            bounds = list(map(int, bounds))
            if bounds[1] < bounds[0]:
                continue
            for i in range(bounds[0], bounds[1]+1):
                i = str(i)
                mid = len(i)//2
                if part == 1:
                    if i[mid:] == i[:mid]:
                        totals.append(int(i))
                else:
                    for j in range(1, mid+1):
                        if len(i)%j == 0:
                            part = i[:j]
                            if i.count(part) == len(i)//j:
                                totals.append(int(i))
                                break
                    
        print(sum(totals))

         

Solve(1)
Solve(2)