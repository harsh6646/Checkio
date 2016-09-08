def checkio(game_result):
    sets =[]
    for x in game_result:
        sets.append(x)
    for x in range(3):
        sets.append(game_result[0][x]+game_result[1][x]+game_result[2][x])
    sets.append(game_result[0][0]+game_result[1][1]+game_result[2][2])
    sets.append(game_result[2][0]+game_result[1][1]+game_result[0][2])
    for x in sets:
        if x.count("X") == 3:
            return "X"
        elif x.count("O") == 3:
            return "O"
    return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

