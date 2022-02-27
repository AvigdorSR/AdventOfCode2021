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
                        lowpoints.append(data[y][x])
                #bottom corner
                elif y == len(data)-1:
                    if int(data[y][x]) < int(data[y][x + 1]) and int(data[y][x]) < int(data[y - 1][x]):
                        lowpoints.append(data[y][x])
                #the rest
                else:
                    if int(data[y][x]) < int(data[y][x + 1]) and int(data[y][x]) < int(data[y - 1][x]) and int(data[y][x]) < int(data[y + 1][x]):
                        lowpoints.append(data[y][x])
            # last column
            elif x == len(data[y])-1:
                # top corner
                if y == 0:
                    if int(data[y][x]) < int(data[y][x - 1]) and int(data[y][x]) < int(data[y + 1][x]):
                        lowpoints.append(data[y][x])
                # bottom corner
                elif y == len(data)-1:
                    if int(data[y][x]) < int(data[y][x - 1]) and int(data[y][x]) < int(data[y - 1][x]):
                        lowpoints.append(data[y][x])
                # the rest
                else:
                    if int(data[y][x]) < int(data[y][x - 1]) and int(data[y][x]) < int(data[y - 1][x]) and int(data[y][x]) < int(data[y + 1][x]):
                        lowpoints.append(data[y][x])
            #top row not including corners because they've already been dealt with
            elif y == 0 :
                if int(data[y][x]) < int(data[y][x + 1]) and int(data[y][x]) < int(data[y][x - 1]) and int(data[y][x]) < int(data[y + 1][x]):
                    lowpoints.append(data[y][x])
           # last row not including corners
            elif y == len(data)-1:
                if int(data[y][x]) < int(data[y][x + 1]) and int(data[y][x]) < int(data[y][x - 1]) and int(data[y][x]) < int(data[y - 1][x]):
                    lowpoints.append(data[y][x])
            #all the rest of the middle values
            else:
                if int(data[y][x]) < int(data[y][x - 1]) and int(data[y][x]) < int(data[y][x + 1]) and  int(data[y][x]) < int(data[y - 1][x]) and int(data[y][x]) < int(data[y + 1][x]):
                    lowpoints.append(data[y][x])

    return lowpoints

def riskcalc (lowpoints):
    riskvalues = [int(x)+1 for x in lowpoints]
    return sum(riskvalues)

print(riskcalc(lowpointfinder(datalines)))
