#input data- read files

rawdata = open("C:\codingstuff\day16input.txt")
datastring = rawdata.read()
rawdata.close()
testdataraw = open("C:\codingstuff\day16testinput.txt")
testdatastring = testdataraw.read()
testdataraw.close()

testline= "A0016C880162017C3686B18A3D4780"

# -- import timing, numpy
import datetime
start_time = datetime.datetime.now()


#---------what data am i testing----------
data= datastring

#-------------

def hex_to_binary_converter (hex_input):
    hex_dictionary= {"0" : "0000", "1" : "0001", "2": "0010" , "3" : "0011", "4" : "0100" , "5" : "0101" , "6" : "0110", "7" : "0111", "8" : "1000", '9':'1001', 'A': '1010', "B" : "1011", "C": "1100", 'D' : '1101' , "E" : '1110', 'F' : '1111'}
    binary_output= ""
    for h in hex_input:
        binary_output += hex_dictionary[h]
    return binary_output

binary_message= hex_to_binary_converter(data)

print("binary of the message:", binary_message)
#---part 1 - -----

packets= []

def packet_reader (binary_input):
    position= 0
    while int(binary_input[position:]) != 0 :
        packet_dictionary= {}
        packet_dictionary["version"]= int(binary_input[position: position + 3], 2)
        position += 3
        packet_dictionary["type_id"]= int(binary_input[position: position + 3], 2)
        position += 3
        if packet_dictionary["type_id"] == 4:
            literal_binary_value= ""
            keep_going = True
            while keep_going:
                if binary_input[position] == '1':
                    keep_going = True
                if binary_input[position] == '0':
                    keep_going = False
                literal_binary_value += binary_input[position+1 : position + 5]
                position += 5
            packet_dictionary["literal_value"]= int(literal_binary_value, 2)
            packets.append(packet_dictionary)
        else:
            if binary_input[position] == '0':
                packet_dictionary["subpackets_length"] = int(binary_input[position+1:position+16], 2)
                position += 16
            elif binary_input[position] == '1':
                packet_dictionary["subpackets_number"] = int(binary_input[position+1:position+12], 2)
                position += 12
            packets.append(packet_dictionary)

packet_reader(binary_message)

print(packets)


version_sum= 0
for p in packets:
    version_sum += p["version"]

print('version sum: ', version_sum)




# timing
end_time = datetime.datetime.now()
print("total time: ", end_time - start_time)