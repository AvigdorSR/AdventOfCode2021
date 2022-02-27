import numpy as np
import copy

#input data- read files
rawdata = open("C:\codingstuff\day22input.txt")
datastring = rawdata.read()
rawdata.close()

testdataraw = open("C:\codingstuff\day22testinput2.txt")
testdatastring = testdataraw.read()
testdataraw.close()

testline_1= '''on x=10..12,y=10..12,z=10..12'''

testline_2 = '''on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13'''


testline_3 = '''on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11'''

testline_4= '''on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10'''

#---------what data am i testing----------
data= datastring

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
    instruction_dictionary["x_start"]= int(instruction_dictionary["x_start"][2:])
    min_x= min(min_x, instruction_dictionary["x_start"])
    instruction_dictionary["x_stop"] = int(instruction_dictionary["x_stop"])
    max_x = max(max_x, instruction_dictionary["x_stop"])
    instruction_dictionary["y_start"], instruction_dictionary["y_stop"] = coordinates_line[1].split("..")
    instruction_dictionary["y_start"]= int(instruction_dictionary["y_start"][2:])
    min_y= min(min_y, instruction_dictionary["y_start"])
    instruction_dictionary["y_stop"] = int(instruction_dictionary["y_stop"])
    max_y= max(max_y, instruction_dictionary["y_stop"] )
    instruction_dictionary["z_start"], instruction_dictionary["z_stop"] = coordinates_line[2].split("..")
    instruction_dictionary["z_start"]= int(instruction_dictionary["z_start"][2:])
    min_z= min(min_z, instruction_dictionary["z_start"] )
    instruction_dictionary["z_stop"] = int(instruction_dictionary["z_stop"])
    max_z= max(max_z, instruction_dictionary["z_stop"])
    instructions.append(instruction_dictionary)

print(instructions)





# ---part 1 & 2  splitting the cubes into pieces. so we're only keeping track of ranges of on states, instead of individual nodes----------

def reactor_restart (instructions_list):
    on_cubes = []
    # find out which cubes should be on at the end, not allowing for doubles.
    for instruction_dictionary in instructions_list:
        new_on_cubes_list = []
        for cube in on_cubes:
            if instruction_dictionary["y_start"] <= cube["y_stop"]  and instruction_dictionary["y_stop"] >= cube["y_start"] and  instruction_dictionary["x_start"] <= cube["x_stop"]  and instruction_dictionary["x_stop"] >= cube["x_start"] and instruction_dictionary["z_start"] <= cube["z_stop"]  and instruction_dictionary["z_stop"] >= cube["z_start"]:
                #y range that isn't touched by the off instructions (take into account that the off cube may extend beyond the top/bottom etc)
                if cube["y_start"] < instruction_dictionary["y_start"] :
                    new_on_cube_y_below = copy.deepcopy(cube)
                    new_on_cube_y_below["y_stop"] = instruction_dictionary["y_start"] -1 #because the cube index to turn off is inclusive
                    new_on_cubes_list.append(new_on_cube_y_below)
                if cube["y_stop"] > instruction_dictionary["y_stop"] :
                    new_on_cube_y_above= copy.deepcopy(cube)
                    new_on_cube_y_above["y_start"]= instruction_dictionary["y_stop"] +1 #because the cube index to turn off is inclusive
                    new_on_cubes_list.append(new_on_cube_y_above)

                # now the x parts that are on, but only dealing with y range that is being cut into by the off cube
                if cube["x_start"] < instruction_dictionary["x_start"]:
                    new_on_cube_x_before = copy.deepcopy(cube)
                    new_on_cube_x_before["y_start"] = max(instruction_dictionary["y_start"], new_on_cube_x_before["y_start"])
                    new_on_cube_x_before["y_stop"] =  min(instruction_dictionary["y_stop"], new_on_cube_x_before["y_stop"])
                    new_on_cube_x_before["x_stop"] = instruction_dictionary["x_start"] - 1  # because the cube index to turn off is inclusive
                    new_on_cubes_list.append(new_on_cube_x_before)

                if cube["x_stop"] > instruction_dictionary["x_stop"]:
                    new_on_cube_x_after = copy.deepcopy(cube)
                    new_on_cube_x_after["y_start"] = max(instruction_dictionary["y_start"], new_on_cube_x_after["y_start"])
                    new_on_cube_x_after["y_stop"] = min(instruction_dictionary["y_stop"], new_on_cube_x_after["y_stop"])
                    new_on_cube_x_after["x_start"] = instruction_dictionary["x_stop"] + 1  # because the cube index to turn off is inclusive
                    new_on_cubes_list.append(new_on_cube_x_after)


                #now z axis, taking into account the limited x and y range
                if cube["z_start"] < instruction_dictionary["z_start"]:
                    new_on_cube_z_before = copy.deepcopy(cube)
                    new_on_cube_z_before["y_start"] = max(instruction_dictionary["y_start"], new_on_cube_z_before["y_start"])
                    new_on_cube_z_before["y_stop"] = min(instruction_dictionary["y_stop"], new_on_cube_z_before["y_stop"])
                    new_on_cube_z_before["x_start"] = max(instruction_dictionary["x_start"], new_on_cube_z_before["x_start"])
                    new_on_cube_z_before["x_stop"] = min (instruction_dictionary["x_stop"], new_on_cube_z_before["x_stop"])

                    new_on_cube_z_before["z_stop"] = instruction_dictionary["z_start"] - 1  # because the cube index to turn off is inclusive
                    new_on_cubes_list.append(new_on_cube_z_before)

                if cube["z_stop"] > instruction_dictionary["z_stop"]:
                    new_on_cube_z_after = copy.deepcopy(cube)
                    new_on_cube_z_after["y_start"] = max(instruction_dictionary["y_start"], new_on_cube_z_after["y_start"])
                    new_on_cube_z_after["y_stop"] = min(instruction_dictionary["y_stop"],new_on_cube_z_after["y_stop"])
                    new_on_cube_z_after["x_start"] = max(instruction_dictionary["x_start"],new_on_cube_z_after["x_start"])
                    new_on_cube_z_after["x_stop"] = min(instruction_dictionary["x_stop"],new_on_cube_z_after["x_stop"])

                    new_on_cube_z_after["z_start"] = instruction_dictionary["z_stop"] + 1  # because the cube index to turn off is inclusive
                    new_on_cubes_list.append(new_on_cube_z_after)
            else:
                new_on_cubes_list.append(cube)
        if instruction_dictionary["state"] == True:
            new_on_cubes_list.append(instruction_dictionary)
        on_cubes = new_on_cubes_list

    #evaluate how many cubes are on
    total_cubes_on= 0
    for cube in on_cubes:
        total_cubes_on +=  (cube['x_stop'] +1 - cube['x_start'])* (cube["y_stop"] +1 - cube['y_start']) * (cube["z_stop"] +1 - cube['z_start'])

    #print("on cubes list: \n", on_cubes)
    print("total cubes on \n", total_cubes_on)


reactor_restart(instructions)

