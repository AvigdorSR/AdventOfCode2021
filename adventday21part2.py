import copy

#input data
data_dictionarys = [{"player_1_position": 10, "player_2_position": 2, "player_1_score": 0, "player_2_score": 0, "whos_turn": "player_1", "freq": 1}]
test_dictionarys = [{"player_1_position": 4, "player_2_position": 8, "player_1_score": 0, "player_2_score": 0,  "whos_turn": "player_1", "freq": 1}]

#---------what data am i testing----------

game_states= data_dictionarys


win_list= {"player_1":0 , "player_2": 0}

# ---part 2 ----------
def DiracDice (game_states):
    while len(game_states) != 0 :
        for index, game in enumerate(game_states):
            lowest_score= 999
            lowest_scored_game_index = 0
            if game[game["whos_turn"] + "_score"] < lowest_score:
                lowest_score = game[game["whos_turn"] + "_score"]
                lowest_scored_game_index = index
        current_game= game_states.pop(lowest_scored_game_index)
        #current_game = game_states.popleft()
        dice_rolls =  [(3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)] #tuples of rolls and frequency
        for r in dice_rolls:
            # using our list of roll frequencies
            universe_1 = copy.deepcopy(current_game)
            universe_1[universe_1["whos_turn"] + "_position"] += r[0]
            universe_1["freq"] = universe_1["freq"] * r[1] # multiply the frequency by the number of universes it happens in
            if universe_1[universe_1["whos_turn"] + "_position"] > 10: #update position
                universe_1[universe_1["whos_turn"] + "_position"] -= 10
            universe_1[universe_1["whos_turn"] + "_score"] += universe_1[universe_1["whos_turn"] + "_position"] #update score
            if universe_1[universe_1["whos_turn"] + "_score"] >= 21: #if the score is 21 or more add the winner and the frequency of the game state to the list of winners
                win_list[universe_1["whos_turn"]] += universe_1["freq"]
            else: #if nobody won, switch who's turn it is
                if universe_1["whos_turn"]== "player_1":
                    universe_1["whos_turn"] = "player_2"
                elif universe_1["whos_turn"] == "player_2":
                    universe_1["whos_turn"] = "player_1"
                #check if this game state already exists, and if it does add it to the frequency
                found_it = False
                for game in game_states:
                    if game["player_1_position"] == universe_1["player_1_position"] and game["player_2_position"] == universe_1["player_2_position"] and game["player_1_score"] == universe_1["player_1_score"] and game["player_2_score"] == universe_1["player_2_score"] and game["whos_turn"] == universe_1["whos_turn"]:
                        game["freq"] += universe_1["freq"]
                        found_it = True
                if not found_it: #otherwise, append it to the list of game states
                    game_states.append(universe_1)


DiracDice(game_states)

print(win_list)

