from collections import defaultdict
def Distance(Start:tuple[int, int, int], Destination:tuple[int, int, int]):
    xdiff = abs(Start[0] - Destination[0])
    ydiff = abs(Start[1] - Destination[1])
    zdiff = abs(Start[2] - Destination[2])
    return (xdiff ** 2 + ydiff ** 2 + zdiff**2)**0.5

DistanceDict = dict()
NetworkDict = defaultdict(list)
DistanceList = []

def merge(data):
    data = [set(x) for x in data]
    Finished = False
    while not Finished:
        Finished = True
        out = []
        for a in data:
            for b in out:
                if a & b:
                    b |= a
                    Finished = False
                    break
            else:
                out.append(a)
        data = out
    return [list(x) for x in data]

def DictToList(dict:dict):
    newlist = list(dict.items())
    newlist = list(map(lambda x: [x[0]] + x[1], newlist))
    return newlist


def Solve(part):
    with open("input8.txt") as f:
        global DistanceList
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        for coord in inp:
            coord = tuple(map(int, coord.split(",")))
            DistanceDict[coord] = []
        coords = list(DistanceDict.keys())
        for i in range(len(coords)):
            for j in range(i+1, len(coords)):
                dist = Distance(coords[i], coords[j])
                # DistanceDict[coords[i]].append((dist, coords[j]))
                # DistanceDict[coords[j]].append((dist, coords[i]))
                DistanceList.append((dist, coords[i], coords[j]))
        import heapq
        heapq.heapify(DistanceList)
        if part == 1:
            for i in range(1000):
                _, Start, End = heapq.heappop(DistanceList)
                NetworkDict[Start].append(End)
                NetworkDict[End].append(Start)
            NetworkList = DictToList(NetworkDict)
            Network = merge(NetworkList)
            lengths = list(map(lambda x: len(x), Network))
            lengths.sort(reverse=True)
            print(lengths[0] * lengths[1] * lengths[2])
        else:
            Final = False
            while True:
                _, Start, End = heapq.heappop(DistanceList)
                NetworkDict[Start].append(End)
                NetworkDict[End].append(Start)
                NetworkList = DictToList(NetworkDict)
                Network = merge(NetworkList)
                if len(Network[0]) == len(inp):
                    if not Final:
                        Final = True
                    else:
                        print(Start[0] * End[0])
                        break

Solve(1)
Solve(2)