#input data
rawdata = open("C:\codingstuff\day7input.txt")
datastring = rawdata.read()
rawdata.close()

from statistics import median

crabsubdata= [int(x) for x in datastring.strip().split(",")]
testdata = [16,1,2,0,4,2,7,1,2,14]

def crabfuelcalc (data):
    probableposition = median(data)
    fuelusage = [abs(probableposition- x) for x in data]
    totalfuel = sum(fuelusage)
    return(totalfuel)


print(crabfuelcalc(crabsubdata))