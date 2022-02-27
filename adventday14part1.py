#input data- read files
rawdata = open("C:\codingstuff\day14input.txt")
datastring = rawdata.read()
rawdata.close()
testdataraw = open("C:\codingstuff\day14testinput.txt")
testdatastring = testdataraw.read()
testdataraw.close()

#---------what data am i testing----------
data= datastring

#convert data into coordinates and instructions,
datasplit = data.split("\n\n")
polymer_template_string = datasplit[0]
instructions_string = datasplit[1]
strings_of_the_instructions = instructions_string.split("\n")

#make a dictionary of the instructions
instructionslist= []
instructionsdictionary= {}
lettercount= {}
for s in strings_of_the_instructions:
    c12, c3 = list(s.replace(" -> ", ",").split(','))
    instructionslist.append((c12, c3))
    instructionsdictionary[c12]= c3
    lettercount[c12[0]]= 0
    lettercount[c12[1]]= 0
    lettercount[c3]= 0
print ("instructions lits", instructionslist, "\n instructions dictionary", instructionsdictionary)


def polymerizer (start_polymer, instructionsdictionary):
    new_polymer=""
    for i in range(len(start_polymer)):
        new_polymer+= start_polymer[i]
        if start_polymer[i:i+2] in instructionsdictionary.keys():
            new_polymer += instructionsdictionary[start_polymer[i:i+2]]
        #print(new_polymer)
    return new_polymer

def polymeriterator (polymerfunc, start_polymer, instructionsdictionary, total_cycles):
    counter= 0
    new_polymer = start_polymer
    while counter < total_cycles:
        counter += 1
        new_polymer = polymerfunc (new_polymer, instructionsdictionary)
        polymerfunc(new_polymer, instructionsdictionary)
    for l in new_polymer:
        lettercount[l] += 1
    print(lettercount)

polymeriterator(polymerizer,polymer_template_string, instructionsdictionary, 10)

#print (polymerizer(polymer_template_string, instructionsdictionary))