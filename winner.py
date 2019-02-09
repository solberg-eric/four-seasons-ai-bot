# From main, self_declare_winner()
def has_won(game):
    if len(game["p1"].hand) == 0:
        game["p1"].has_won = False
        game["p2"].has_won = True
        return True
    elif len(game["p2"].hand) == 0 and len(game["p2"].cards_in_play) == 0:
        game["p1"].has_won = True
        game["p2"].has_won = False
        return True
    else:
        return False

# From main
def declare_winner(game):
    if has_won(game):
        if game["p1"].has_won:
            print("Player One wins!")
        else:
            print("Player Two wins!")