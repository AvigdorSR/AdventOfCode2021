#input data- read files
rawdata = open("C:\codingstuff\day13input.txt")
datastring = rawdata.read()
rawdata.close()
testdataraw = open("C:\codingstuff\day13testinput.txt")
testdatastring = testdataraw.read()
testdataraw.close()

#---------what data am i testing----------
data= datastring

import numpy as np



#convert data into coordinates and instructions,
datasplit = data.split("\n\n")
coordinates_string = datasplit[0]
instructions_string = datasplit[1]
strings_of_the_coordinates = coordinates_string.split("\n")

#make tuples of all y,x pairs because numpy does y, x coordinates
coordinates= []
max_x = 0
max_y = 0
for d in strings_of_the_coordinates:
    x, y = list(map(int, d.split(',')))
    coordinates.append(( y , x ))
# create grid of all locations, based on maximum coordinates given
for c in coordinates:
    max_x = max(max_x, c[1])
    max_y = max(max_y, c[0],)
grid = np.zeros((max_y+1, max_x+1), dtype=int)
print("max y", max_y, "max x", max_x)
#populate the grid
for c in coordinates:
    grid[c[0], c[1]] = "1"

# make list of
#instructions= [["x", 655], ["y", 447], ["x", 327], ['y', 223],['x', 163], ['y' , 111],['x' ,81], ["y", 55], ['x' , 40], ["y", 27], ["y", 13], ['y' , 6]]
instructions= []
for instruction in instructions_string.split("\n"):
    instruct = [i for i in instruction if i.isdigit()  or i == "x" or i == "y"]
    instructions.append(instruct)
for id, instruction in enumerate(instructions):
        a= ""
        for i in instruction:
            if i.isdigit():
                a+= i
        instructions[id] = [instruction[0],int(a)]

print("instructions: ", instructions)

print("total dots:", np.sum(grid))

# ---part 1 ------------------
def folder (grid, instructions):
    for i in instructions:
        if i[0]== "y":
            for coordinate, value in np.ndenumerate(grid):
                if coordinate[0] > i[1] and value == 1:
                    grid[coordinate[0] - 2*(coordinate[0] - i[1]), coordinate[1]] = 1
                    grid[coordinate] = 0
        if i[0] == "x":
            for coordinate, value in np.ndenumerate(grid):
                if coordinate[1] > i[1]  and value == 1 :
                    grid[coordinate[0], coordinate[1]- 2*(coordinate[1] - i[1])] = 1
                    grid[coordinate] = 0
    #print(grid)
    print("visible dots:", np.sum(grid))

folder (grid, instructions)

# ---part 2 ------------------
min_y_instruction = 1000
min_x_instruction = 1000
for i in instructions:
    if i[0] == "y":
        min_y_instruction = min(min_y_instruction, i[1])
    if i[0] == "x":
        min_x_instruction= min(min_x_instruction, i[1])

for (y, x), element in np.ndenumerate(grid):
    if y > min_y_instruction:
        try:
            grid = np.delete(grid, y, axis=0)
        except IndexError:
            pass
    if x > min_x_instruction:
        try:
            grid = np.delete(grid, x, axis=1)
        except IndexError:
            pass

#np.savetxt("day13fixed.csv", grid, delimiter=",")

print(grid)
#grid2= np.nonzero(grid)

#print(grid2)