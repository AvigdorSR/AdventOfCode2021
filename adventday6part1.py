
rawdata = open("C:\codingstuff\day6input.txt")
datastring = rawdata.read()
rawdata.close()
datastring

testdata = [3,4,3,1,2]
fishdata= [int(x) for x in datastring.strip().split(",")]

def lanternfishcalc (data, days):
    fish = data
    counter= 0
    while counter < days:
        fish[:]= [f- 1 for f in fish]
        for f in fish:
            if f == -1:
                fish.append(8)
        fish[:] = [f if f >= 0 else 6 for f in fish]
        counter += 1
    else:
        return fish

print(len(lanternfishcalc(fishdata, 80)))



