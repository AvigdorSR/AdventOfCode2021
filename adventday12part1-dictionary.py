#input data- read files
rawdata = open("C:\codingstuff\day12input.txt")
datastring = rawdata.read()
rawdata.close()
testdataraw = open("C:\codingstuff\day12testinput2.txt")
testdatastring = testdataraw.read()
testdataraw.close()

#input data- list of strings
datalines = datastring.split("\n")
testlines = testdatastring.split("\n")
firsttestline= ["start-A", "start-b", "A-c", "A-b", "b-d", "A-end", "b-end"]
#---------what data am i testing----------
data= datalines

#import deep copy module
import copy

# -- timing
import datetime
start_time = datetime.datetime.now()



#create a database of cave connections, and caves, particularly a dictionary that tells us what caves we can get to from the cave we're in
caves = set()
connections= []
caveconnectionsdict= {}
def cavecharter (data_in):
    for d in data_in:
        c1, c2 = list(d.split('-'))
        connections.append((c1, c2))
        caves.add(c1)
        caves.add(c2)
    for cave in caves:
        caveconnectionsdict[cave]=[]
        for x in connections:
            if cave in x:
                caveconnectionsdict[cave]+= [y for y in x if y != cave]


cavecharter(data)
print("caves: " , caves)
print("connections: ", connections)
print("caveconnections dictionary:", caveconnectionsdict)


# ---part 1 ------------------
# calculate possible routes with no doubling up of small caves

def routcounter (caveconnectionsdict):
    total_complete_routes = 0
    current_exploration_status = [{"lowercase_caves_visited": [], "cave_I_am_in": "start"}]
    while len(current_exploration_status) != 0:
        status= current_exploration_status.pop(0)
        #print("lets check where we can go from:", status)

        for c in caveconnectionsdict[status["cave_I_am_in"]]:
            #print("maybe i can go to cave:", c)
            if c == "end":
                total_complete_routes += 1
                #print("yay, found a way to the end cave")
            elif c.islower() and c != "start":
                if c not in status["lowercase_caves_visited"]:
                    new_status = copy.deepcopy(status)
                    new_status["cave_I_am_in"] = c
                    new_status["lowercase_caves_visited"].append(c)
                    current_exploration_status.append(new_status)
                    #print("yes, i can go to cave: ", c)
            elif c.isupper():
                new_status = copy.deepcopy(status)
                new_status["cave_I_am_in"] = c
                current_exploration_status.append(new_status)
                #print("yes, i can go to cave: ", c)

            #print("current path count: ", total_complete_routes)
        #print("current exploration status: ", current_exploration_status)

    #print( "final current pending exploration status: ", current_exploration_status)
    print("total number of routes: ", total_complete_routes)

routcounter (caveconnectionsdict)


# timing
end_time = datetime.datetime.now()
print("total time: ", end_time - start_time)