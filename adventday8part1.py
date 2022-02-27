#input data
rawdata = open("C:\codingstuff\day8input.txt")
datastring = rawdata.read()
rawdata.close()

testdataraw = open("C:\codingstuff\day8testinput.txt")
testdatastring = testdataraw.read()
testdataraw.close()

def uniquesdisplaydatagetter (data):
    ones = 0
    fours= 0
    sevens = 0
    eights = 0
    lines = data.split("\n")
    signal_and_output = [x.split(" | ") for x in lines]
    outputs= [x[1] for x in signal_and_output]
    #print ("outputs:", outputs)
    splitoutputs = [x.split(" ") for x in outputs]
    #print ("splitoutputs", splitoutputs)
    for d in splitoutputs:
        for x in d:
            if len(x) == 2:
                ones+= 1
            if len(x) == 4:
                fours += 1
            if len(x) == 3:
                sevens += 1
            if len(x) == 7:
                eights += 1
    print ("ones: ", ones, "fours: ", fours, "sevens: ", sevens, "eights: ", eights, "and the total: ", ones+fours+sevens+eights)


#uniquesdisplaydatagetter(testdatastring)

uniquesdisplaydatagetter(datastring)




