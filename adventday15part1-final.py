#input data- read files
import heapq

rawdata = open("C:\codingstuff\day15input.txt")
datastring = rawdata.read()
rawdata.close()
testdataraw = open("C:\codingstuff\day15testinput.txt")
testdatastring = testdataraw.read()
testdataraw.close()

testdatarawexpanded = open("C:\codingstuff\day15testinputexpanded.txt")
testdatastringexpanded = testdatarawexpanded.read()
testdatarawexpanded.close()

squigle_path_testinput= '''19111
19191
11191
99991
99991'''

# -- import timing, numpy
import datetime
start_time = datetime.datetime.now()

import numpy as np

#---------what data am i testing----------
data= testdatastringexpanded

#---------create an array of all the values, the total risk from start, and whether i've visited it----
gridstrings = data.split("\n")
risk_level_grid = np.zeros((len(gridstrings), len(gridstrings[0])), dtype=int) # make a grid of the values
max_y= len(gridstrings)-1 # -1 because the array is zero indexed
max_x= len(gridstrings[0])-1  # -1 because the array is zero indexed
total_risk_from_start_grid = np.full_like(risk_level_grid, 999)
total_risk_from_start_grid[0, 0] = 0  # make the start spot = 0
visited_status_grid = np.full_like(risk_level_grid, False, bool)

def gridpopulator (grid, strings_in):
    for y, string in enumerate(strings_in):
        for x, value in enumerate(string):
            grid[y, x] = int(value)
    grid[0, 0] = 0  # make the start spot = 0, because Eric said so
gridpopulator(risk_level_grid, gridstrings)

grid_making_time= datetime.datetime.now()
print("time to make grids", grid_making_time- start_time)
#print(risk_level_grid)
#print("\n risk from start", total_risk_from_start_grid, "\n visited status grid", visited_status_grid, "\nplaces to see", places_to_see)

#---part 1 - find the lowest risk path through the caves-----

def djistra (risk_level_grid):
    places_to_see = [(0, (0, 0))] # tuples of current risk value, and (y, x) so the heap or sort puts the lowest risk on top
    heapq.heapify(places_to_see)

    while len(places_to_see) != 0:
        checkspot = heapq.heappop(places_to_see)
        #places_to_see.sort()   #reverse=True) #sorted list method, making the least at the end
        #checkspot = places_to_see.pop(0)
        if checkspot[1] ==  (max_y, max_x) :
            print("exit risk: ", total_risk_from_start_grid[max_y, max_x])
            break
        else:
            visited_status_grid[checkspot[1]]= True
            y = checkspot[1][0]
            x= checkspot[1][1]
            #neighbors= [] #creat a list of all neighbors
            if y != 0:
                if visited_status_grid[y - 1, x] == False:
                    neighbor_risk = total_risk_from_start_grid[checkspot[1]]+ risk_level_grid[y - 1, x]
                    if neighbor_risk < total_risk_from_start_grid[y - 1, x]:
                        total_risk_from_start_grid[y - 1, x] = neighbor_risk
                    #total_risk_from_start_grid[y - 1, x]= min(total_risk_from_start_grid[y - 1, x], total_risk_from_start_grid[checkspot[1]]+ risk_level_grid[y - 1, x])
                    if (total_risk_from_start_grid[y - 1, x], (y - 1, x)) not in places_to_see:
                        heapq.heappush(places_to_see, (total_risk_from_start_grid[y - 1, x], (y - 1, x))) # heap method
                    #places_to_see.append((total_risk_from_start_grid[y - 1, x], (y - 1, x))) # sorted list method
            if y != max_y :
                if visited_status_grid[(y + 1, x)] == False:
                    neighbor_risk= total_risk_from_start_grid[checkspot[1]] + risk_level_grid[(y + 1, x)]
                    if neighbor_risk < total_risk_from_start_grid[(y + 1, x)]:
                        total_risk_from_start_grid[(y + 1, x)] =  total_risk_from_start_grid[checkspot[1]] + risk_level_grid[(y + 1, x)]
                    # total_risk_from_start_grid[(y + 1, x)] = min(total_risk_from_start_grid[(y + 1, x)], total_risk_from_start_grid[checkspot[1]] + risk_level_grid[(y + 1, x)])
                    if (total_risk_from_start_grid[(y + 1, x)], (y + 1, x)) not in places_to_see:
                        heapq.heappush(places_to_see, (total_risk_from_start_grid[(y + 1, x)], (y + 1, x))) # heap method
                    #places_to_see.append((total_risk_from_start_grid[(y + 1, x)], (y + 1, x)))  # sorted list method
            if x != max_x :
                if visited_status_grid[(y, x + 1)] == False:
                    neighbor_risk = total_risk_from_start_grid[checkspot[1]] + risk_level_grid[(y, x + 1)]
                    if neighbor_risk < total_risk_from_start_grid[(y, x + 1)]:
                        total_risk_from_start_grid[(y, x + 1)] = total_risk_from_start_grid[checkspot[1]] + risk_level_grid[(y, x + 1)]
                #total_risk_from_start_grid[(y, x + 1)] = min(total_risk_from_start_grid[(y, x + 1)], total_risk_from_start_grid[checkspot[1]] + risk_level_grid[(y, x + 1)])
                    if (total_risk_from_start_grid[(y, x + 1)], (y, x + 1)) not in places_to_see:
                        heapq.heappush(places_to_see, (total_risk_from_start_grid[(y, x + 1)], (y, x + 1))) # heap method
                    #places_to_see.append((total_risk_from_start_grid[(y, x + 1)], (y, x + 1)))  # sorted list method
            if x != 0:
                if visited_status_grid[(y, x - 1)] == False:
                    neighbor_risk = total_risk_from_start_grid[checkspot[1]] + risk_level_grid[(y, x - 1)]
                    if neighbor_risk < total_risk_from_start_grid[(y, x - 1)]:
                        total_risk_from_start_grid[(y, x - 1)] = total_risk_from_start_grid[checkspot[1]] + risk_level_grid[(y, x - 1)]
                #total_risk_from_start_grid[(y, x - 1)] = min(total_risk_from_start_grid[(y, x - 1)], total_risk_from_start_grid[checkspot[1]] + risk_level_grid[(y, x - 1)])
                    if (total_risk_from_start_grid[(y, x - 1)], (y, x - 1)) not in places_to_see:
                        heapq.heappush(places_to_see, (total_risk_from_start_grid[(y, x - 1)], (y, x - 1))) # heap method
                    #places_to_see.append((total_risk_from_start_grid[(y, x - 1)], (y, x - 1)))  # sorted list method
    print("total risk from start grid: \n" , total_risk_from_start_grid)
    print("places i've visited\n", visited_status_grid)
    print("lowest risk to exit: ", total_risk_from_start_grid[max_y, max_x])


djistra(risk_level_grid)

# timing
end_time = datetime.datetime.now()
print("djikstra time", end_time-grid_making_time , "\n total time: ", end_time - start_time)