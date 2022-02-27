rawdata = open("C:\codingstuff\day5testinput.txt")
datastring = rawdata.read()
rawdata.close()

# create tuples of x1, y1, x2, y2
datalist = datastring.split("\n")
coordinates= []
for d in datalist:
    x1, y1, x2, y2 = list(map(int, d.replace(" -> ", " , ").split(',')))
    coordinates.append((x1, y1, x2, y2))

# create grid of all locations, based on maximum coordinates given
max_x = 0
max_y = 0
for c in coordinates:
    max_x = max(max_x, c[0], c[2])
    max_y = max(max_y, c[1], c[3])

import numpy as np
grid = np.zeros((max_y+1, max_x+1), dtype=int)

#add vent locations to grid
def vententry(grid, coordinates):
    for c in coordinates:
        if c[0] == c[2]:
            for y in range(min(c[1], c[3]), max(c[1],c[3])+1):
                grid[y, c[0]] += 1
        elif c[1] == c[3]:
            for x in range(min(c[0], c[2]), max(c[0], c[2]) + 1):
                grid[c[1], x] += 1
        else:
            x = [range(c[0], c[2]+1) if c[2]- c[0] >=1 else range(c[0], c[2]-1, -1)]
            y = [range(c[1], c[3]+1) if c[3] - c[1] >= 1 else range(c[1], c[3]-1, -1)]
            diaganals= zip(y,x)
            for d in diaganals:
                grid[d[0], d[1]] += 1


vententry(grid, coordinates)

print('score', (grid >= 2).sum())


