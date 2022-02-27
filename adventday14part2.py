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
polymer_growth_dictionary_template= {}
lettercount= {}
for s in strings_of_the_instructions:
    c12, c3 = list(s.replace(" -> ", ",").split(','))
    instructionslist.append((c12, c3))
    instructionsdictionary[c12]= [c12[0] + c3, c3 + c12[1], c3]
    lettercount[c12[0]]= 0
    lettercount[c12[1]]= 0
    lettercount[c3]= 0
    polymer_growth_dictionary_template[c12]= 0
print ("instructions lits", instructionslist, "\n instructions dictionary", instructionsdictionary)

for k in lettercount.keys():
    polymer_growth_dictionary_template[k]= 0

print("polymer growth  tracker template ", polymer_growth_dictionary_template)

#get started with out initial data

polymer_start_dictionary = polymer_growth_dictionary_template.copy()
for i in range(len(polymer_template_string)):
    polymer_start_dictionary[polymer_template_string[i]]+=1
    if i < len(polymer_template_string)-1:
        polymer_start_dictionary[polymer_template_string[i:i + 2]] += 1

print('polymer start dictionary:' , polymer_start_dictionary)



def polymerizer (start_polymer, instructionsdictionary):
    new_polymer= polymer_growth_dictionary_template.copy()
    for k in start_polymer.keys():
        if len(k) == 1:
            new_polymer[k] += start_polymer[k]
        if len(k) == 2:
            new_polymer[instructionsdictionary[k][0]] +=  start_polymer[k]
            new_polymer[instructionsdictionary[k][1]] +=  start_polymer[k]
            new_polymer[instructionsdictionary[k][2]] +=  start_polymer[k]
    return new_polymer

#print(polymerizer(polymer_start_dictionary, instructionsdictionary))

def polymeriterator (polymerfunc, start_polymer, instructionsdictionary, total_cycles):
    counter= 0
    new_polymer = start_polymer
    while counter < total_cycles:
        counter += 1
        new_polymer = polymerfunc (new_polymer, instructionsdictionary)
        polymerfunc(new_polymer, instructionsdictionary)
    print("our new polymer:", new_polymer)
    max_element = 0
    min_element = 999999999999999999999999999999999
    for k in new_polymer.keys():
        if len(k) == 1:
            max_element = max(max_element, new_polymer[k])
            min_element = min(min_element, new_polymer[k])
    print("max element minus min element:", max_element - min_element, "max", max_element, "min", min_element)


polymeriterator(polymerizer, polymer_start_dictionary, instructionsdictionary, 40)

