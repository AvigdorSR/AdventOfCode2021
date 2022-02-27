#input data- read files
rawdata = open("C:\codingstuff\day11input.txt")
datastring = rawdata.read()
rawdata.close()
testdataraw = open("C:\codingstuff\day11testinput.txt")
testdatastring = testdataraw.read()
testdataraw.close()

#input data- list of strings
datalines = datastring.split("\n")
testlines = testdatastring.split("\n")
firsttestline= [""]
#---------what data am i testing----------
data= datalines

# ---part 1---------count total flashes ---------------
import numpy as np

# make a grid of the values
grid = np.zeros((len(data), len(data[0])), dtype=int)
ymax= len(data)
xmax= len(data[0])

def gridpopulator (data):
    for y, string in enumerate(data):
        for x, value in enumerate(string):
            grid[y, x] = int(value)
gridpopulator(data)


def flashcounter (grid, totalsteps):
    flashcounter = 0
    stepcounter = 0
    while stepcounter < totalsteps:
        stepcounter +=1
        checkformoreflashes = 1
        grid = grid + 1
        while checkformoreflashes == 1:
            checkformoreflashes = 0
            for (y, x), value in np.ndenumerate(grid):
                if grid[y,x] >= 10 :
                    flashcounter += 1
                    grid[y,x] = -10000
                    checkformoreflashes = 1
                    #make neighbors go up by one
                    if y != 0:
                        grid[y - 1, x] += 1
                        try:
                            grid[y-1, x+1] += 1
                        except IndexError:
                            pass
                        if x != 0:
                            grid[y - 1, x-1] += 1
                    try:
                        grid [y+ 1, x] += 1
                    except IndexError:
                        pass
                    try:
                        grid [y+ 1, x+1] += 1
                    except IndexError:
                        pass
                    try:
                        if x != 0:
                            grid[y + 1, x - 1] += 1
                    except IndexError:
                        pass
                    try:
                        grid [y, x+1] += 1
                    except IndexError:
                        pass
                    if x != 0:
                        grid[y, x-1] +=1
        for (y, x), value in np.ndenumerate(grid):
            if grid[y,x] < 0:
                grid[y,x]= 0
    print("flashcounter= ", flashcounter, "\n", "stepcounter = ", stepcounter, "\n", "grid: \n", grid)

flashcounter(grid, 100)
