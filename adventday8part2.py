#input data- read files
rawdata = open("C:\codingstuff\day8input.txt")
datastring = rawdata.read()
rawdata.close()

testdataraw = open("C:\codingstuff\day8testinput.txt")
testdatastring = testdataraw.read()
testdataraw.close()

#input data- lists/strings
lines = datastring.split("\n")
testlines = testdatastring.split("\n")
firstexample = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

# number interpreter
def numberinterpreter (data):
    interpretedoutput = []
    stringvalue= ""
    #figure out the meaning of each signal, and make a dictionary of the values
    displaydatadictionary = {"1": "null", "2": "null", "3": "null", "4": "null", "5": "null", "6": "null", "7": "null", "8": "null", "9": "null", "0": "null"}
    signal_and_output = data.split(" | ")
    signal = [sorted(x) for x in signal_and_output[0].split(" ")]
    #print("initial signal reading" , signal)
    output= [sorted(x) for x in signal_and_output[1].split(" ")]
    while len(signal)> 6 :
        for x in signal:
            if len(x) == 7:
                displaydatadictionary["8"] = x
                signal.remove(x)
            elif len(x) == 2:
                displaydatadictionary["1"] = x
                signal.remove(x)
            elif len(x) == 4:
                displaydatadictionary["4"] = x
                signal.remove(x)
            elif len(x) == 3:
                displaydatadictionary["7"]= x
                signal.remove(x)
    for x in signal:
        if len(x) == 6:
            if all(letter in x for letter in displaydatadictionary["4"]):
                displaydatadictionary["9"]= x
                signal.remove(x)
    for x in signal:
        if len(x) == 6:
            if all(letter in x for letter in displaydatadictionary["7"]):
                displaydatadictionary["0"] = x
                signal.remove(x)
    for x in signal:
        if len(x) == 6:
            if not all(letter in x for letter in displaydatadictionary["7"]):
                displaydatadictionary["6"] = x
                signal.remove(x)
    for x in signal:
        if len(x) == 5:
            if all(letter in displaydatadictionary["6"] for letter in x):
                displaydatadictionary["5"] = x
                signal.remove(x)
    for x in signal:
        if len(x) == 5:
            if all(letter in displaydatadictionary["9"] for letter in x ):
                displaydatadictionary["3"] = x
                signal.remove(x)
    for x in signal:
        if len(x) == 5:
                displaydatadictionary["2"] = x
                signal.remove(x)
    #print ("unsolved signals:", signal)
    #print("display dictionary" , displaydatadictionary)
    # interpret the output and make it into a number
    for y in output:
        for key in displaydatadictionary.keys():
            if displaydatadictionary[key] == y:
                interpretedoutput.append(key)
    for v in interpretedoutput:
        stringvalue += v[0]
    #print ("interpreted output", interpretedoutput)
    return int(stringvalue)


#print(numberinterpreter(firstexample))
#print(sum(list(map(numberinterpreter, testlines))))
print(sum(list(map(numberinterpreter, lines))))

