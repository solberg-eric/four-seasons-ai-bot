from L2 import *

#1.0
def setup_game(depth_factor): # From 0.0
    class Player:
        def __init__(self, hand, cards_in_play, cards_in_play_ranks, trick_pile, cost, gain, has_won):
            self.hand = hand
            self.cards_in_play = cards_in_play
            self.cards_in_play_ranks = cards_in_play_ranks
            self.trick_pile = trick_pile
            self.cost = cost
            self.gain = gain
            self.has_won = has_won
    #p1 = Player(["AH", "KH", "QH", "JH", "AS", "KS", "QS", "JS", "AD", "KD", "QD", "JD", "AC", "KC", "QC", "JC"], [], [0, 0], [], 0, 0, False)
    #p2 = Player(["AH", "KH", "QH", "JH", "AS", "KS", "QS", "JS", "AD", "KD", "QD", "JD", "AC", "KC", "QC", "JC"], [], [0, 0], [], 0, 0, False)
    #p1 = Player(["AH", "KH", "AS", "KS", "AD", "KD", "AC", "KC"], [], [0, 0], [], 0, 0, False)
    #p2 = Player(["AH", "KH", "AS", "KS", "AD", "KD", "AC", "KC"], [], [0, 0], [], 0, 0, False)
    p1 = Player(["AH", "KH", "QH", "AS", "KS", "QS", "AD", "KD", "QD", "AC", "KC", "QC"], [], [0, 0], [], 0, 0, False)
    p2 = Player(["AH", "KH", "QH", "AS", "KS", "QS", "AD", "KD", "QD", "AC", "KC", "QC"], [], [0, 0], [], 0, 0, False)    
    game = {
        "p1" : p1,
        "p2" : p2,
        "depth_factor" : depth_factor,
        "depth" : depth_factor * 4,
        "alpha" : -float("Inf"),
        "beta" : float("Inf"),
        "trump_order" : ["Hearts", "Spades", "Diamonds", "Clubs"],
        "lead_player" : lead_player(), # To 2.0
        "lead_suit" : None, #"H", "S", "D", or "C"
        "player_winning_trick" : None, #eventually "p1" or "p2"
        "hand_finished" : False,
        "value" : 0,
        "player_optimizing" : "p1"
    }
    return game

#1.1
def play_game(game): # From 0.0
    while not has_won(game): # To 2.1
        while not game["hand_finished"]:
            trick(game) # To 2.2
        setup_next_hand(game) # To 2.3
    declare_winner(game) # To 2.4
