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
firsttestline= ["[({(<(())[]>[[{[]{<()<>>"]
#---------what data am i testing----------
data= datalines

# ---part 1---------find the closing tags that are out of place ---------------

opentagdictionary = {")": "(", "]": "[", "}": "{", ">": "<"}
openners = ["(", "{", "[", "<"]
closers = [")", "}", "]", ">"]

errorstringsfordeletion = []
firsterrors= []

def syntaxcheckerlooper (navsystemtagslines):

    def syntaxchecker (navsystemtagsline1):
        navsystemtags= [x for x in navsystemtagsline1]
        #print (navsystemtags)
        #errorfound= ""
        for c, t in enumerate(navsystemtags):
            if t in closers and opentagdictionary[t]== navsystemtags[c-1]:
                del navsystemtags[c]
                del navsystemtags[c-1]
                syntaxchecker(navsystemtags)
                break
            elif t in closers and opentagdictionary[t] != navsystemtags[c - 1]:
                #print ("error!", t)
                firsterrors.append(t)
                errorstringsfordeletion.append(line)
                #return t
                #errorfound = t
                #return errorfound
                break
            else:
                continue

    for line in navsystemtagslines:
        syntaxchecker(line)


syntaxcheckerlooper(data)

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

#-------------part 2- ----------

tagvaluedictionary = {"(": 1, "[": 2, "{": "3", "<": 4}

incompletestrings= [x for x in data if x not in errorstringsfordeletion]


scrubbedincompletelines= []

def linecompleterlooper (navsystemtagslines):
    for line in navsystemtagslines:
        linescrubber(line)

def linescrubber (navsystemtagsline1):
    navsystemtags= [x for x in navsystemtagsline1]
    for c, t in enumerate(navsystemtags):
        if t in closers and opentagdictionary[t]== navsystemtags[c-1]:
            del navsystemtags[c]
            del navsystemtags[c-1]
            linescrubber(navsystemtags)
            break
        else:
            continue
    if not any(item in navsystemtags for item in closers) :
        if navsystemtags not in scrubbedincompletelines :
            scrubbedincompletelines.append(navsystemtags)


linecompleterlooper(incompletestrings)


#scorecalc
autocompletescores= []
def completioncalc (scrubbedunclosedtagslist):
    for list in scrubbedunclosedtagslist:
        score= 0
        neededtags= list[::-1]
        for tag in neededtags:
            score = score* 5 + int(tagvaluedictionary[tag])
        autocompletescores.append(score)

completioncalc(scrubbedincompletelines)

autocompletescores= sorted(autocompletescores)
middlevalue= int( len(autocompletescores)/2)

print("autocomplete middle score:" , autocompletescores[middlevalue])