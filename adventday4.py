rawdata = open("C:\codinginput\day4.txt")
datastring = rawdata.read()
rawdata.close()

datalist = datastring.split("\n\n")
drawstring = datalist.pop(0)
boardlist = datalist
drawlist = [int(x) for x in drawstring.split(',') if x.strip().isdigit()]

print(drawlist)


# print (boardlist)

def bingoboard(boardstring):
    card = {
        "b": [],
        "i": [],
        "n": [],
        "g": [],
        "o": [],
    }
    rows = boardstring.split("\n")
    card["b"] = [int(x) for x in rows[0].split()]
    card["i"] = [int(x) for x in rows[1].split()]
    card["n"] = [int(x) for x in rows[2].split()]
    card["g"] = [int(x) for x in rows[3].split()]
    card["o"] = [int(x) for x in rows[4].split()]
    return card


bingoboarddictionarylist = []
for board in boardlist:
    bingoboarddictionarylist.append(bingoboard(board))


# print (bingoboarddictionarylist)


def playingbingo(bingoboards, bingoballsdraws):
    winningboards = []
    for x in bingoballsdraws:

        # check and mark if it's on a board
        for board in bingoboards:
            for letter in board.keys():
                for i in range(5):
                    if board[letter][i] == x:
                        board[letter][i] = "X"
            # return board
            # print(board)
        # checki if there's a winner
        for board in bingoboards:
            for letter in board.keys():
                if board[letter][0] == "X" and board[letter][1] == "X" and board[letter][2] == "X" and board[letter][
                    3] == "X" and board[letter][4] == "X":
                    # print(board, "wins! \n", "and %d is the winning ball" % x)
                    winningboards.append([board, "wins! \n", "and %d is the winning ball" % x])
                    try:
                        for i in range(len(bingoboards)):
                            if bingoboards[i] == board:
                                del bingoboards[i]
                    except IndexError:
                        continue

            for i in range(5):
                if board["b"][i] == "X" and board["i"][i] == "X" and board["n"][i] == "X" and board["g"][i] == "X" and \
                        board["o"][i] == "X":
                    winningboards.append([board, "wins! \n", "and %d is the winning ball" % x])
                    # print(board, "wins! \n", "and %d is the winning ball" % x)
                    try:
                        for i in range(len(bingoboards)):
                            if bingoboards[i] == board:
                                del bingoboards[i]
                    except IndexError:
                        continue

    # print (winningboards)
    return winningboards


winningboardslist = playingbingo(bingoboarddictionarylist, drawlist)
print("first winner is: \n ", winningboardslist[0], "\n last winner is:  \n ", winningboardslist[-1], )

remainingfirstwinnervalues = list(winningboardslist[0][0].values())
sumfirstvalues = [int(x) for x in remainingfirstwinnervalues[.split(',') if x.strip().isdigit()]

print(sumfirstvalues)
"""
totalfirstwinnersum= sum(remainingfirstwinnervalues)
winningball= [int(x) for x in winningboardslist[0][1].split() if x.strip().isdigit()]
solutiontofirstwinner= winningball[0]*totalfirstwinnersum
print("the solution to the board that will win first is %d" % solutiontofirstwinner)
"""

# def solutioncalc(boardlist):
#    remainingfirstwinnervalues= winningboardslist[0][0].values()
#    totalfirstwinnersum= sum(remainingfirstwinnervalues)
#    winningball= [int(x) for x in winningboardslist[0][1].split() if x.strip().isdigit()]
#    solutiontofirstwinner= winningball[0]*totalfirstwinnersum
#    print("the solution to the board that will win first is %d" % solutiontofirstwinner)
#    remaininglasttwinnervalues= winningboardslist[-1][0].values()
#    totallastwinnersum= sum(remaininglasttwinnervalues)
#    lastwinningball= [int(x) for x in winningboardslist[-1][1].split() if x.strip().isdigit()]
#    solutiontoflastwinner= lastwinningball[0]*totallastwinnersum
#    print("the solution to the board that will win last is %d" % solutiontoflastwinner)

# solutioncalc(winningboardslist)

# winnernumber(winningboardslist, -1)
# playingbingo(bingoboarddictionarylist, drawlist)