#input data
rawdata = open("C:\codingstuff\day7input.txt")
datastring = rawdata.read()
rawdata.close()

# datalists
crabsubdata= [int(x) for x in datastring.strip().split(",")]
testdata = [16,1,2,0,4,2,7,1,2,14]

#function
def crabfuelcalc (data):
    fuelsums= []
    for c in range (max(data)):
        fuelusagepart1 = [abs(c - x) for x in data]
        fuelusagepart2 = [x * (x + 1) / 2 for x in fuelusagepart1]
        totalfuel = sum(fuelusagepart2)
        fuelsums.append(totalfuel)
    return (min(fuelsums))

print(crabfuelcalc(crabsubdata))

