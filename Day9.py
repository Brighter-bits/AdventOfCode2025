from copy import deepcopy
import sys
sys.setrecursionlimit(100000000)
DistanceDict = dict() # Look familiar?
def Rect(n1, n2):
    return (abs(n1[0] - n2[0]) + 1) * (abs(n1[1] - n2[1])+1) # This is just the formula for the area of a rectangle.

# def Distance(Start:tuple[int, int], Destination:tuple[int, int]):
#     xdiff = abs(Start[0] - Destination[0])
#     ydiff = abs(Start[1] - Destination[1])
#     return (xdiff ** 2 + ydiff ** 2)**0.5

grid = []
Visited = set()

def CheckLine(n1, n2, walls):
    x1, y1 = n1
    x2, y2 = n2
    if x1 == x2:
        for wall in walls: # Wall : ((minx, maxx), (miny, maxy))
            wx1, wx2 = wall[0]
            wy1, wy2 = wall[1]
            if wy1 == wy2 and wx1 <= x1 <= wx2 and y1 < wy1 < y2:
                return False
    elif y1 == y2:
        for wall in walls: # Wall : ((minx, maxx), (miny, maxy))
            wx1, wx2 = wall[0]
            wy1, wy2 = wall[1]
            if wx1 == wx2 and wy1 <= y1 <= wy2 and x1 < wx1 < x2:
                return False
    else:
        raise 
    
    return True

def FindCoord(xcoords, ycoords, coord):
    x = -1
    y = -1
    if coord[0] < xcoords[0]:
        x = 0
    elif coord[0] == xcoords[-1]:
        x = (len(xcoords)*2)-1
    else:
        for i in range(0, len(xcoords)-1):
            if xcoords[i] == coord[0]:
                x = 2*i
                break
            elif xcoords[i] < coord[0] < ycoords[i+1]:
                x = (2*i)-1
                break

    if coord[1] < ycoords[0]:
        y = 0
    elif coord[1] == ycoords[-1]:
        y = (len(ycoords)*2)-1
    else:
        for i in range(0, len(ycoords)-1):
            if ycoords[i] == coord[1]:
                y = 2*i
                break
            elif ycoords[i] < coord[1] < ycoords[i+1]:
                y = (2*i)-1
                break
    return (x, y)

def FloodFill(Node):
    global grid
    x = Node[0]
    y = Node[1]
    if Node in Visited:
        return
    Visited.add(Node)
    if grid[y][x-1] != "#":
        grid[y][x-1] = "#"
        FloodFill((x-1, y))

    if grid[y][x+1] != "#":
        grid[y][x+1] = "#"
        FloodFill((x+1, y))

    if grid[y-1][x] != "#":
        grid[y-1][x] = "#"
        FloodFill((x, y-1))

    if grid[y+1][x] != "#":
        grid[y+1][x] = "#"
        FloodFill((x, y+1))



def CoordinateCompress(coords:list[tuple[int, int]]):
    global grid
    ycoords = []
    xcoords = []
    oldcoords = deepcopy(coords)
    coords.sort(key=lambda x: x[0])
    for i in range(0, len(coords)-1, 2):
        xcoords.append(coords[i][0])
    coords.sort(key=lambda x: x[1])
    for i in range(0, len(coords)-1, 2):
        ycoords.append(coords[i][1])
    grid = [["." for i in range((2*len(xcoords)))] for j in range((2*len(ycoords)))] # Number of walls coords + the number of spaces between the walls = 2*numwalls
    oldcoords = list(map(lambda x: FindCoord(xcoords, ycoords, x), oldcoords))
    # print(oldcoords)
    for i in range(len(oldcoords)):
        x1, y1 = oldcoords[(i)%len(oldcoords)]
        x2, y2 = oldcoords[(i+1)%len(oldcoords)]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                grid[y][x1] = "#"
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                grid[y1][x] = "#"
    for y in range(len(grid)):
        for x in range(len(grid[0])-1):
            if grid[y][x] == "#" and grid[y][x-1] != "#" and grid[y][x+1] != "#":
                FloodFill((x+1, y))
                break
    # for i in grid:
    #     print("".join(i))
    return xcoords, ycoords


# def MakeGrid(walls, dim:int):
#     grid = [["." for a in range(dim)] for b in range(dim)]
#     for wall in walls:
#         wx1, wx2 = wall[0]
#         wy1, wy2 = wall[1]

#         if wx1 == wx2:
#             for i in range(wy1, wy2+1):
#                 grid[i][wx1] = "#"
#         if wy1 == wy2:
#             for i in range(wx1, wx2+1):
#                 grid[wy1][i] = "#"


    # return grid

# def CheckLine(n1, n2, Vertical):
#     if Vertical and n1[1] == n2[1]:
#         return True
#     elif not Vertical and n1[0] == n2[0]:
#         return True
#     else:
#         return False

def Solve(part):
    global grid
    AreaList = []
    with open("input9.txt") as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        for coord in inp:
            coord = tuple(map(int, coord.split(",")))
            DistanceDict[coord] = []
        coords = list(DistanceDict.keys())
        for i in range(len(coords)):
            for j in range(i+1, len(coords)):
                area = Rect(coords[i], coords[j])
                AreaList.append((area, coords[i], coords[j]))
        import heapq
        heapq.heapify_max(AreaList) # I updated to python 3.14 just for this feature.
        if part == 1:
            print(heapq.heappop_max(AreaList)[0])
        else:
            # walls = []
            # for i in range(len(coords)):
            #     walls.append(((min(coords[i%len(coords)][0], coords[(i+1)%len(coords)][0]), max(coords[i%len(coords)][0], coords[(i+1)%len(coords)][0])), (min(coords[i%len(coords)][1], coords[(i+1)%len(coords)][1]), max(coords[i%len(coords)][1], coords[(i+1)%len(coords)][1]))))
            xcoords, ycoords = CoordinateCompress(coords)
            while True:
                area, Start, End = heapq.heappop_max(AreaList)
                x1, y1 = FindCoord(xcoords, ycoords, Start)
                x2, y2 = FindCoord(xcoords, ycoords, End)
                # borders = []
                # borders.append((Start[0], Start[1])) # I could probably do a little maths formula with a loop but I can't be bothered.
                # borders.append((Start[0], End[1]))
                # borders.append((End[0], End[1]))
                # borders.append((End[0], Start[1]))
                valid = True
                # if area == 24:
                #     breakpoint()
                # Rays = list(map(lambda x: CheckPoint(x, walls, borders), borders))
                # for i in range(len(Rays)):
                #     if not CheckLine(Rays[i%len(Rays)], Rays[(i+1)%len(Rays)], i%2 == 0):
                #         valid = False
                # #         break
                # for i in range(len(borders)):
                #     if not CheckLine(borders[i%len(borders)], borders[(i+1)%len(borders)], walls):
                #         valid = False
                #         break
                        
                # if valid:
                #     if not CheckLine((abs(Start[0] + End[0])//2, Start[1]), (abs(Start[0] + End[0])//2, End[1]), walls):
                #         valid = False
                #     if not CheckLine((Start[0], abs(Start[1]+End[1])//2), (End[0], abs(Start[1]+End[1])//2), walls):
                #         valid = False


                for y in range(min(y1, y2), max(y1, y2)):
                    for x in range(min(x1, x2), max(x1, x2)+1):
                        if grid[y][x] != "#":
                            valid = False
                            break
                    if not valid:
                        break
                    
                if valid:
                    print(area)
                    break

                # print(MakeGrid(walls, 100000))




Solve(2)