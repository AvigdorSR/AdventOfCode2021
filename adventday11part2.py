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

# ---part 1 and 2---------count total flashes, and break when the whole array is zero (simultaneous flash)-----------
import numpy as np

# make a grid of the values
grid = np.zeros((len(data), len(data[0])), dtype=int)

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
                    #make sure that they don't flash again, and that we don't get confused between one's that have flashed and been counted, and those we haven't by making those we've counted become negative
                    grid[y,x] = -10000
                    #repeat the loop after we're done to take into account the effect on the neighbors triggered by this one
                    checkformoreflashes = 1
                    #make neighbors go up by one, avoiding index errors, and bugs caused by negative indexing (gotta find a better way to do this)
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
        # reset all the octopi that have flashed to zero
        for (y, x), value in np.ndenumerate(grid):
            if grid[y,x] < 0:
                grid[y,x]= 0
        #check if everyone is zero
        if not np.any(grid):
            print("simultaneous flashing at step: " , stepcounter)

    print("flashcounter= ", flashcounter, "\n", "stepcounter = ", stepcounter, "\n", "final state of the grid: \n", grid)

flashcounter(grid, 500)
