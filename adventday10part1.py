#input data- read files
rawdata = open("C:\codingstuff\day10input.txt")
datastring = rawdata.read()
rawdata.close()
testdataraw = open("C:\codingstuff\day10testinput.txt")
testdatastring = testdataraw.read()
testdataraw.close()

#input data- lists/strings
datalines = datastring.split("\n")
testlines = testdatastring.split("\n")

#---------what data am i testing----------
data= datalines

# ---part 1---------find the closing tags that are out of place ---------------

opentagdictionary = {")": "(", "]": "[", "}": "{", ">": "<"}
openners = ["(", "{", "[", "<"]
closers = [")", "}", "]", ">"]

firsterrors= []
def syntaxchecker (navsystemtagsline):
    navsystemtags= [x for x in navsystemtagsline]
    #print (navsystemtags)
    #errorfound= ""
    for c, t in enumerate(navsystemtags):
        if t in closers and opentagdictionary[t]== navsystemtags[c-1]:
            del navsystemtags[c]
            del navsystemtags[c-1]
            syntaxchecker(navsystemtags)
            break
        elif t in closers and opentagdictionary[t] != navsystemtags[c - 1]:
            print ("error!", t)
            firsterrors.append(t)
            return t
            #errorfound = t
            #return errorfound
            break
        else:
            continue
    #return errorfound
    #return firsterrors.append(errorfound)

#syntaxchecker("{([(<{}[<>[]}>{[]{[(<()>")

print(list(map(syntaxchecker, data)))

print(firsterrors)
def firsterrorsscore (listoffirsterrors):
    score= 0
    for x in listoffirsterrors:
        if x == ")":
            score += 3
        if x == "]":
            score+= 57
        if x == "}":
            score += 1197
        if x == ">":
            score += 25137
    return score

print (firsterrorsscore((firsterrors)))
#-------------part 2- ----------
