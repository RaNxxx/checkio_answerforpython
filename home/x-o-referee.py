def checkio(game_result):

    #チェックする行の全ての並びをgame_listにする
    game_list = [element for element in game_result]

    game_list.append(game_list[0][0]+game_list[1][0]+game_list[2][0])
    game_list.append(game_list[0][1]+game_list[1][1]+game_list[2][1])
    game_list.append(game_list[0][2]+game_list[1][2]+game_list[2][2])
    game_list.append(game_list[0][0]+game_list[1][1]+game_list[2][2])
    game_list.append(game_list[0][2]+game_list[1][1]+game_list[2][0])

    #game_listのうちに、x/oかdを判定

    result = ""

    if "XXX" in game_list:
        result = "X"
    elif "OOO" in game_list:
        result = "O"
    else:
        result = "D"

    return result
