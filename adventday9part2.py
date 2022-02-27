#input data- read files
rawdata = open("C:\codingstuff\day9input.txt")
datastring = rawdata.read()
rawdata.close()

testdataraw = open("C:\codingstuff\day9testinput.txt")
testdatastring = testdataraw.read()
testdataraw.close()

#input data- lists/strings
datalines = datastring.split("\n")
testlines = testdatastring.split("\n")

#---------what data am i testing----------
dataimtesting= datalines


# ---part 1---------find the low points ---------------

def lowpointfinder (data):
    lowpoints= []
    for y in range(len(data)):
        for x in range(len(data[y])):
            #edges
            #first column
            if x == 0 :
                #top corner
                if y == 0:
                    if int(data[y][x]) < int(data[y][x + 1]) and int(data[y][x]) < int(data[y + 1][x]):
                        lowpoints.append([[y,x],int(data[y][x])])
                #bottom corner
                elif y == len(data)-1:
                    if int(data[y][x]) < int(data[y][x + 1]) and int(data[y][x]) < int(data[y - 1][x]):
                        lowpoints.append([[y,x],int(data[y][x])])
                #the rest
                else:
                    if int(data[y][x]) < int(data[y][x + 1]) and int(data[y][x]) < int(data[y - 1][x]) and int(data[y][x]) < int(data[y + 1][x]):
                        lowpoints.append([[y,x],int(data[y][x])])
            # last column
            elif x == len(data[y])-1:
                # top corner
                if y == 0:
                    if int(data[y][x]) < int(data[y][x - 1]) and int(data[y][x]) < int(data[y + 1][x]):
                        lowpoints.append([[y,x],int(data[y][x])])
                # bottom corner
                elif y == len(data)-1:
                    if int(data[y][x]) < int(data[y][x - 1]) and int(data[y][x]) < int(data[y - 1][x]):
                        lowpoints.append([[y,x],int(data[y][x])])
                # the rest
                else:
                    if int(data[y][x]) < int(data[y][x - 1]) and int(data[y][x]) < int(data[y - 1][x]) and int(data[y][x]) < int(data[y + 1][x]):
                        lowpoints.append([[y,x],int(data[y][x])])
            #top row not including corners because they've already been dealt with
            elif y == 0 :
                if int(data[y][x]) < int(data[y][x + 1]) and int(data[y][x]) < int(data[y][x - 1]) and int(data[y][x]) < int(data[y + 1][x]):
                    lowpoints.append([[y,x],int(data[y][x])])
           # last row not including corners
            elif y == len(data)-1:
                if int(data[y][x]) < int(data[y][x + 1]) and int(data[y][x]) < int(data[y][x - 1]) and int(data[y][x]) < int(data[y - 1][x]):
                    lowpoints.append([[y,x],int(data[y][x])])
            #all the rest of the middle values
            else:
                if int(data[y][x]) < int(data[y][x - 1]) and int(data[y][x]) < int(data[y][x + 1]) and  int(data[y][x]) < int(data[y - 1][x]) and int(data[y][x]) < int(data[y + 1][x]):
                    lowpoints.append([[y,x],int(data[y][x])])

    return lowpoints

lowpoints = lowpointfinder((dataimtesting))

print("lowpoints [[y,x], value] : " , lowpoints)

#risk calculator
def riskcalc (lowpoints):
    riskvalues = [int(n)+1 for n in lowpoints]
    return sum(riskvalues)

#print(riskcalc(lowpointfinder(dataimtesting)))

#-------------part 2- finding the basins, based off of our knowledge of the lowpoints----------



def basinfinder (lowpoints, data):
    allbasins = []
    basinsizelist= []
    for point in lowpoints:
        basin = []
        basin.append(point)
        basingrowing= True
        while basingrowing:
            basingrowing = False
            for location in basin:
                neighbors= []

                if location[0][1] != 0:  # if x not zero:
                    # [y, x-1], value
                    neighbors.append([[location[0][0],location[0][1] - 1],int(data[location[0][0]][location[0][1] - 1])])
                if location[0][1] != len(data[0])-1: # if x is not the end of the data string
                    # [y, x+1], value
                    neighbors.append([[location[0][0],location[0][1] + 1],int(data[location[0][0]][location[0][1] + 1])])
                if location[0][0] != 0:  # y not zero
                    # [y-1, x], value
                    neighbors.append([[location[0][0]-1,location[0][1]],int(data[location[0][0]-1][location[0][1]])])
                if location[0][0] != len(data)-1: # if y is not the last row of the data strings
                    # [y, x+1], value
                    neighbors.append([[location[0][0]+1,location[0][1]],int(data[location[0][0]+1][location[0][1]])])
                for spot in neighbors:
                    if spot[1] >= location[1] and spot[1] != 9:
                        if spot not in basin:
                            basin.append(spot)


        print(basin)
        allbasins.append(([basin]))
        basinsizelist.append(len(basin))
    print ("basin size list:", basinsizelist)
    print("basin size list sorted:", sorted(basinsizelist, reverse = True))
    biggestbasins= sorted(basinsizelist, reverse=True)
    print("biggest three basins multiplied together: ", biggestbasins[0] * biggestbasins[1] * biggestbasins[2])

basinfinder (lowpoints, dataimtesting)
