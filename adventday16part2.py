#input data- read files

rawdata = open("C:\codingstuff\day16input.txt")
datastring = rawdata.read()
rawdata.close()
testdataraw = open("C:\codingstuff\day16testinput.txt")
testdatastring = testdataraw.read()
testdataraw.close()

testline= "A0016C880162017C3686B18A3D4780"

# -- import timing,
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
        packet_dictionary["start position"]= position
        packet_dictionary["version"]= int(binary_input[position: position + 3], 2)
        position += 3
        packet_dictionary["type_id"]= int(binary_input[position: position + 3], 2)
        position += 3
        if packet_dictionary["type_id"] == 4:
            packet_dictionary["has_subpackets"] = False
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
            packet_dictionary["end position"] = position
            packets.append(packet_dictionary)
        else:
            packet_dictionary["has_subpackets"]= True
            if binary_input[position] == '0':
                packet_dictionary["subpackets_length"] = int(binary_input[position+1:position+16], 2)
                position += 16
            elif binary_input[position] == '1':
                packet_dictionary["subpackets_number"] = int(binary_input[position+1:position+12], 2)
                position += 12
            packet_dictionary["end position"] = position
            packets.append(packet_dictionary)

packet_reader(binary_message)

#print(packets)


# part 1- sum of all the versions
version_sum= 0
for p in packets:
    version_sum += p["version"]
print('version sum: ', version_sum)

#part 2 - find the value of the packets

full_packet= []

def packet_processor (packets_list, output_packet_list):
    close_parenthasis_count = []
    subpacket_level_length_count = {-2:0 , -1: -10, 0: 1, 1:1, 2:1, 3:1}
    litteral_packet_count= 0
    sub_level= 0
    for packet in packets_list:
        counter= 0
        if subpacket_level_length_count[sub_level] != "n":
            subpacket_level_length_count[sub_level] -= 1
        if packet["has_subpackets"] == True:
            sub_level += 1
            if sub_level not in subpacket_level_length_count:
                subpacket_level_length_count[sub_level] = 1
            try:
                subpacket_level_length_count[sub_level] = packet['subpackets_number']
            except KeyError:
                close_parenthasis_count.append(packet['subpackets_length'] + packet['end position'])
                subpacket_level_length_count[sub_level] = "n"

        if packet['type_id'] == 4:
            output_packet_list.append(str(packet['literal_value']))
            output_packet_list.append(',')

        elif packet['type_id'] == 0:
            output_packet_list.append("sum(")
        elif packet['type_id'] == 1:
            output_packet_list.append("prod(")
        elif packet['type_id'] == 2:
            output_packet_list.append("min(")
        elif packet['type_id'] == 3:
            output_packet_list.append("max(")
        elif packet['type_id'] == 5:
            output_packet_list.append("greater_than(")
        elif packet['type_id'] == 6:
            output_packet_list.append("less_than(")
        elif packet['type_id'] == 7:
            output_packet_list.append( "equal_to(")

        while counter < 100:
            if sub_level < 0:
                break
            counter += 1
            if subpacket_level_length_count[sub_level] == "n":
                if len(close_parenthasis_count) != 0:
                    if packet['end position'] == close_parenthasis_count[-1]:
                        close_parenthasis_count.pop(-1)
                        subpacket_level_length_count[sub_level] = 1
                        sub_level -= 1
                        output_packet_list.append(")")
                        output_packet_list.append(",")
            if subpacket_level_length_count[sub_level] == 0:
                sub_level -= 1
                output_packet_list.append(")")
                output_packet_list.append(",")


packet_processor(packets, full_packet)

def sum (*args):
    sum = 0
    for arg in args:
        sum+= arg
    return sum

def prod(*args):
    product= 1
    for arg in args:
        product= arg * product
    return product

def min(*args):
    minimum= 999999999999999999999
    for arg in args:
        if arg < minimum:
            minimum = arg
    return minimum

def max(*args):
    maximum= 0
    for arg in args:
        if arg > maximum:
            maximum = arg
    return maximum

def greater_than(x, y):
    if x > y:
        return 1
    else:
        return 0 

def less_than (x, y):
    if x < y:
        return 1
    else:
        return 0

def equal_to (x, y):
    if x == y:
        return 1
    else:
        return 0




print(full_packet)


#need to add a loop that adds the missing commas


for index, x in enumerate(full_packet):
    if x == ")":
        if full_packet[index-1] == ",":
            full_packet[index-1] = " "
    if index == len(full_packet)-1:
        if x == ",":
            full_packet[-2:]= " "



operation_string= ""
for x in full_packet:
    operation_string += x

print ("operation string: \n", operation_string)

print("message: \n", eval (operation_string))



#print(sum(prod(9,less_than(90,258)),max(14,2),min(15083,4,10),min(46486,946644),47731,prod(86,167,76,41,75),prod(902426,less_than(5448597,5448597)),12,3150483273,46921,1756,prod(3098,equal_to(241,11104915)),prod(greater_than(2338,2338),185954532),prod(105,146,64,124),1619,prod(183,less_than(440674,103)),max(6937079,92140,209,592),max(prod(min(min(max(sum(max(prod(max(sum(min(sum(sum(min(max(sum(max(prod(min(min(5056208039)))))))))))))))))))),455,256083,sum(prod(9,6,4),prod(14,4,8),prod(5,3,12)),min(11,208,70,1647,130),prod(3586,greater_than(sum(14,2,7),sum(5,6,3))),prod(1045,equal_to(7539326,139)),prod(28505,less_than(1344,46)),prod(equal_to(310846,310846),55133606844),2158747088,max(50614281761),prod(44),prod(sum(10,15,9),sum(8,10,11),sum(8,7,9)),prod(40917,less_than(206,206)),prod(152,greater_than(664377,115979877)),prod(140,less_than(sum(10,14,15),sum(13,6,7))),sum(3,204,122),max(277,62608,143,3234,3179),min(188615,4835,64264,685172),prod(greater_than(sum(9,11,15),sum(9,7,10)),7877750),prod(22,equal_to(sum(15,15,4),sum(11,9,12))),prod(greater_than(31223,31223),126),max(139455,2126,1316140047),sum(57417,5),prod(greater_than(2997,24470),177),13,prod(97,128),sum(85,37726,178,7,277352178),prod(3851,greater_than(233881589634,2158)),sum(15),prod(8,less_than(6,2589)),prod(greater_than(3811248452,33),64983444992),prod(less_than(sum(3,2,4),sum(6,15,5)),78),sum(1842,372,5732528,1),min(17588),prod(22,202,77)))
#print(sum(prod(9,less_than(90,258)),max(14,2),min(15083,4,10),min(46486,946644),47731,prod(86,167,76,41,75),prod(902426,less_than(5448597,5448597)),12,3150483273,46921,1756,prod(3098,equal_to(241,11104915)),prod(greater_than(2338,2338),185954532),prod(105,146,64,124),1619,prod(183,less_than(440674,103)),max(6937079,92140,209,592),max(prod(min(min(max(sum(max(prod(max(sum(min(sum(sum(min(max(sum(max(prod(min(min(5056208039)))))))))))))))))))),455,256083,sum(prod(9,6,4),prod(14,4,8),prod(5,3,12)),min(11,208,70,1647,130),prod(3586,greater_than(sum(14,2,7),sum(5,6,3))),prod(1045,equal_to(7539326,139)),prod(28505,less_than(1344,46)),prod(equal_to(310846,310846),55133606844),2158747088,max(50614281761),prod(44),prod(sum(10,15,9),sum(8,10,11),sum(8,7,9)),prod(40917,less_than(206,206)),prod(152,greater_than(664377,115979877)),prod(140,less_than(sum(10,14,15),sum(13,6,7))),sum(3,204,122),max(277,62608,143,3234,3179),min(188615,4835,64264,685172),prod(greater_than(sum(9,11,15),sum(9,7,10)),7877750),prod(22,equal_to(sum(15,15,4),sum(11,9,12))),prod(greater_than(31223,31223),126),max(139455,2126,1316140047),sum(57417,5),prod(greater_than(2997,24470),177),13,prod(97,128),sum(85,37726,178,7,277352178),prod(3851,greater_than(233881589634,2158)),sum(15),prod(8,less_than(6,2589)),prod(greater_than(3811248452,33),64983444992),prod(less_than(sum(3,2,4),sum(6,15,5)),78),sum(1842,372,5732528,1),min(17588),prod(22,202,77)))


# timing
end_time = datetime.datetime.now()
print("total time: ", end_time - start_time)
