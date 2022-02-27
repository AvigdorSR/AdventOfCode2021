#input data
rawdata = open("C:\codingstuff\day6input.txt")
datastring = rawdata.read()
rawdata.close()
datastring

testdata = [3,4,3,1,2]
fishdata= [int(x) for x in datastring.strip().split(",")]

#make a dictionary of fishvalues
lanternfish_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
for fish in fishdata:
    lanternfish_dict[fish] += 1


#fish calculator by dictionary
def lanternfishcalc (dictionary, days):
    for x in range(days):
        new_fish_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for key in dictionary.keys():
            new_fish_dict[key - 1] = dictionary[key]
        for key in new_fish_dict:
            if key == -1:
                new_fish_dict[8] = new_fish_dict[-1]
                new_fish_dict[6] += new_fish_dict[-1]
        dictionary = new_fish_dict
        del dictionary[-1]
    return dictionary

final_lanternfish = lanternfishcalc(lanternfish_dict, 256)
print (final_lanternfish)

print ("the total number of lanternfish is: ", sum([x for x in final_lanternfish.values()]))




