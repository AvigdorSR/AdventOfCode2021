import numpy as np

#input data- read files
rawdata = open("C:\codingstuff\day22input.txt")
datastring = rawdata.read()
rawdata.close()

testdataraw = open("C:\codingstuff\day22testinput.txt")
testdatastring = testdataraw.read()
testdataraw.close()

testline_1= '''on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10'''



#---------what data am i testing----------
data= testdatastring

#input data- list of strings
datalines = data.split("\n")
instructions = []
max_x = 0
min_x = 0
max_y = 0
min_y = 0
max_z = 0
min_z = 0

for line in datalines:
    instruction_dictionary= {}
    l = line.split(" ")
    if l[0] == "on":
        instruction_dictionary["state"] = True
    if l[0] == "off":
        instruction_dictionary["state"] = False
    coordinates_line= l[1].split(",")
    instruction_dictionary["x_start"], instruction_dictionary["x_stop"] = coordinates_line[0].split("..")
    instruction_dictionary["x_start"]= max(int(instruction_dictionary["x_start"][2:])+50, 0)
    min_x= min(min_x, instruction_dictionary["x_start"]+50)
    instruction_dictionary["x_stop"] = min(int(instruction_dictionary["x_stop"])+50,101)
    max_x = max(max_x, instruction_dictionary["x_stop"]+50)
    instruction_dictionary["y_start"], instruction_dictionary["y_stop"] = coordinates_line[1].split("..")
    instruction_dictionary["y_start"]= max(int(instruction_dictionary["y_start"][2:])+50, 0)
    min_y= min(min_y, instruction_dictionary["y_start"]+50)
    instruction_dictionary["y_stop"] = min(int(instruction_dictionary["y_stop"])+50, 101)
    max_y= max(max_y, instruction_dictionary["y_stop"] )+50
    instruction_dictionary["z_start"], instruction_dictionary["z_stop"] = coordinates_line[2].split("..")
    instruction_dictionary["z_start"]= max(int(instruction_dictionary["z_start"][2:])+50, 0)
    min_z= min(min_z, instruction_dictionary["z_start"] +50)
    instruction_dictionary["z_stop"] = min(int(instruction_dictionary["z_stop"])+50, 101)
    max_z= max(max_z, instruction_dictionary["z_stop"]+50)
    instructions.append(instruction_dictionary)

print(instructions)

print("max and min:", max_x, min_x, max_y, min_y,  max_z, min_z)




# ---part 1 ----------



# make a grid of the values

cuboid_reactor_grid = np.full((102, 102, 102), False, dtype= bool)
print(cuboid_reactor_grid.shape)
print("total cubes on at the start:", np.sum(cuboid_reactor_grid))

def reactor_restart (instructions_list, reactor_grid):
    for instruction_dictionary in instructions_list:
        reactor_grid[instruction_dictionary["y_start"]:instruction_dictionary["y_stop"] +1, instruction_dictionary["x_start"]:instruction_dictionary["x_stop"] +1, instruction_dictionary["z_start"] : instruction_dictionary["z_stop"] +1] = instruction_dictionary["state"]


reactor_restart(instructions, cuboid_reactor_grid)

print("total cubes on at the end:", np.sum(cuboid_reactor_grid))

