DistanceDict = dict() # Look familiar?
def Rect(n1, n2):
    return (abs(n1[0] - n2[0]) + 1) * (abs(n1[1] - n2[1])+1) # This is just the formula for the area of a rectangle.

# def Distance(Start:tuple[int, int], Destination:tuple[int, int]):
#     xdiff = abs(Start[0] - Destination[0])
#     ydiff = abs(Start[1] - Destination[1])
#     return (xdiff ** 2 + ydiff ** 2)**0.5

def CheckLine(n1, n2, walls):
    x1, y1 = n1
    x2, y2 = n2
    if x1 == x2:
        for wall in walls: # Wall : ((minx, maxx), (miny, maxy))
            wx1, wx2 = wall[0]
            wy1, wy2 = wall[1]
            if wy1 == wy2 and wx1 <= x1 <= wx2 and y1 <= wy1 <= y2:
                return False
    elif y1 == y2:
        for wall in walls: # Wall : ((minx, maxx), (miny, maxy))
            wx1, wx2 = wall[0]
            wy1, wy2 = wall[1]
            if wx1 == wx2 and wy1 <= y1 <= wy2 and x1 <= wx1 <= x2:
                return False
    else:
        raise 
    
    return True
    
        

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
            walls = []
            for i in range(len(coords)):
                walls.append(((min(coords[i%len(coords)][0], coords[(i+1)%len(coords)][0]), max(coords[i%len(coords)][0], coords[(i+1)%len(coords)][0])), (min(coords[i%len(coords)][1], coords[(i+1)%len(coords)][1]), max(coords[i%len(coords)][1], coords[(i+1)%len(coords)][1]))))

            while True:
                area, Start, End = heapq.heappop_max(AreaList)
                borders = []
                borders.append((Start[0], Start[1])) # I could probably do a little maths formula with a loop but I can't be bothered.
                borders.append((Start[0], End[1]))
                borders.append((End[0], End[1]))
                borders.append((End[0], Start[1]))
                valid = True
                # # if area == 24:
                # #     breakpoint()
                # Rays = list(map(lambda x: CheckPoint(x, walls, borders), borders))
                # for i in range(len(Rays)):
                #     if not CheckLine(Rays[i%len(Rays)], Rays[(i+1)%len(Rays)], i%2 == 0):
                #         valid = False
                #         break
                for i in range(len(borders)):
                    if not CheckLine(borders[i%len(borders)], borders[(i+1)%len(borders)], walls):
                        valid = False
                        break
                        
                if valid:
                    CheckLine()

                if valid:
                    print(area)
                    break

                # print(MakeGrid(walls, 100000))




Solve(2)