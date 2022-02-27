import numpy as np

#input data- read files
rawdata = open("C:\codingstuff\day25input.txt")
datastring = rawdata.read()
rawdata.close()

testdataraw = open("C:\codingstuff\day25testinput.txt")
testdatastring = testdataraw.read()
testdataraw.close()


#---------what data am i testing----------
data= datastring

#input data- cucumber array
gridstrings = data.split("\n")

max_y = len(gridstrings)
max_y_index = max_y -1
max_x= len(gridstrings[0])
max_x_index = max_x -1

 # make a grid of the cucumbers, 0 = empty, 1= east moving, 2= south moving

cucumber_grid = np.zeros((max_y, max_x), dtype=int)

def gridpopulator (grid, strings_in):
    for y, string in enumerate(strings_in):
        for x, value in enumerate(string):
            if value == '>':
                grid[y, x] = 1
            if value == 'v':
                grid[y, x] = 2
            if value == '.':
                grid[y, x] = 0
gridpopulator(cucumber_grid, gridstrings)

#print(cucumber_grid)


def cucumber_tracker (cucumber_start_locations):
    cucumber_locations= cucumber_start_locations
    did_anyone_move= True
    steps= 0
    while did_anyone_move:
        steps += 1
        new_cucumber_location= np.zeros_like(cucumber_locations)
        for index, value in np.ndenumerate(cucumber_locations):
            y= index[0]
            x= index[1]
            if value == 1:
                if x == max_x_index:
                    if cucumber_locations[y, 0] == 0:
                        new_cucumber_location[y, 0] = 1
                    else:
                        new_cucumber_location[y, x] = 1
                else:
                    if cucumber_locations[y, x+1] == 0:
                        new_cucumber_location[y, x + 1] = 1
                    else:
                        new_cucumber_location[y,x] = 1
        #south movers, check if it's empty after the east movers moved on the new cucumber locations, and if there's already a south mover there from before
        for index, value in np.ndenumerate(cucumber_locations):
            y= index[0]
            x= index[1]
            if value == 2:
                if y == max_y_index:
                    if new_cucumber_location[0, x] == 0 and cucumber_locations[0, x]!=2:
                        new_cucumber_location[0, x] = 2
                    else:
                        new_cucumber_location[y,x]= 2
                else:
                    if new_cucumber_location[y+1, x] == 0 and cucumber_locations[y+1, x] !=2:
                        new_cucumber_location[y+1, x] = 2
                    else:
                        new_cucumber_location[y,x]= 2
            #print("steps:", steps)
        if np.array_equal(new_cucumber_location, cucumber_locations):
            did_anyone_move = False
            print("total steps to immobilization:", steps)
            break
        cucumber_locations = new_cucumber_location

cucumber_tracker(cucumber_grid)