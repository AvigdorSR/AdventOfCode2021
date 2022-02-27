#input data
data_dictionary = {"player_1_position": 10, "player_2_position": 2, "player_1_score": 0, "player_2_score": 0}
test_dictionary = {"player_1_position": 4, "player_2_position": 8, "player_1_score": 0, "player_2_score": 0}

#---------what data am i testing----------
data= data_dictionary

dice= [x for x in range(100, 0, -1)]*10

#print(dice)

# ---part 1 ----------
def DiracDice (game_dictionary):
    while game_dictionary["player_1_score"] < 1000 and game_dictionary["player_2_score"] < 1000:
        roll= 0
        roll= dice.pop() + dice.pop() + dice.pop()
        counter= 0
        while counter < roll:
            if game_dictionary["player_1_position"] == 10:
                game_dictionary["player_1_position"]= 0
            game_dictionary["player_1_position"] += 1
            counter += 1
        game_dictionary["player_1_score"] += game_dictionary["player_1_position"]
        if game_dictionary["player_1_score"] >= 1000:
            print("player 1 wins!", game_dictionary, "dice rolls:", 1000- len(dice))
            print("solution:", game_dictionary["player_2_score"] * (1000 - len(dice)))
            break
        roll= 0
        roll= dice.pop() + dice.pop() + dice.pop()
        counter= 0
        while counter < roll:
            if game_dictionary["player_2_position"] == 10:
                game_dictionary["player_2_position"]= 0
            game_dictionary["player_2_position"] += 1
            counter += 1
        game_dictionary["player_2_score"] += game_dictionary["player_2_position"]
        if game_dictionary["player_2_score"] >= 1000:
            print("player 2 wins!", game_dictionary, "dice rolls:", 1000- len(dice))
            print("solution:", game_dictionary["player_1_score"]* (1000- len(dice)))
            break

DiracDice(data)