def war(deck1, deck2):
    # Check if any player runs out of cards
    if not deck1:
        print("Player 2 is victorious!")
        return [], deck2
    elif not deck2:
        print("Player 1 victorious!")
        return deck1, []
    
    print("Battle: Player 1 played", deck1[0])
    print("Battle: Player 2 played", deck2[0])
    
    # Determine the winner
    if deck1[0] > deck2[0]:
        deck1 = deck1[1:] + [deck1[0], deck2[0]]
        deck2 = deck2[1:]
        print("Player 1 won this battle")
    elif deck1[0] < deck2[0]:
        deck2 = deck2[1:] + [deck1[0], deck2[0]]
        deck1 = deck1[1:]
        print("Player 2 won this battle")
    else:
        print("Players tie on this battle")
        print("War is declared")
        winner, rd1, rd2 = gotoWar(deck1[1:], deck2[1:])
        if winner == 1:
            print("Player 1 won this war.")
            deck1 = rd1 + [deck1[0], deck2[0]]
            deck2 = rd2
        else:
            print("War: Player 2 won this war")
            deck2 = rd2 + [deck1[0], deck2[0]]
            deck1 = rd1
        
    print("After Battle: Player 1 Deck contains ", deck1)
    print("After Battle: Player 2 Deck contains ", deck2)

    # Continue the game with a recursive call
    return war(deck1, deck2)

def gotoWar(deck1, deck2):
    winner = 0
    stash = []
    while winner == 0:
        stash = [deck1[0], deck2[0], deck1[1], deck2[1]] + stash
        print("War: Player 1 face down card:", deck1[0] )
        print("War: Player 2 face down card:", deck2[0] )
        print("War: Player 1 face up card:",  deck1[1] )
        print("War: Player 2 face up card:",  deck2[1])

        if deck1[1] > deck2[1]:
            winner = 1
            deck1 = deck1[2:] + stash
            deck2 = deck2[2:]
        elif deck1[1] < deck2[1]:
            winner = 2
            deck2 = deck2[2:] + stash
            deck1 = deck1[2:]
        else:
            print("War: Another Tie. War is declared.")
            deck1 = deck1[2:]
            deck2 = deck2[2:]

    return winner, deck1, deck2



print("Prepare for War (The CardGame).")
# eg2: player 1 wins no wars
# player1_deck = [14, 11, 9, 6]
# player2_deck = [11, 7, 8, 4]

# eg3: player 2 wins no wars
# player1_deck = [1,2,3]
# player2_deck = [7,8,9]

# eg4: player 2 wins 1 war
# player1_deck = [12, 9, 7, 4]
# player2_deck = [12, 7, 8, 5]

# eg5: player 1 wins 2 wars
# player1_deck = [12, 7, 9, 11, 7]
# player2_deck = [12, 2, 9, 14, 2]

# eg6: player 2 wins multiple battles
# player1_deck = [12, 11, 9, 8]
# player2_deck = [13, 10, 7, 8]

# eg7: player 1 wins with a number of wars
# After Battle: Player 1 Deck contains [4, 4, 9, 7, 8, 7, 8, 8, 4, 
# 2, 9, 9, 6, 3, 10, 10, 4, 5, 11, 11, 9, 8, 12, 12, 8, 6, 13, 13, 14, 14]
player1_deck = [14, 8, 13, 9, 12, 4, 11, 6, 10, 4, 9, 8, 8, 4, 9]
player2_deck = [14, 6, 13, 8, 12, 5, 11, 3, 10, 2, 9, 7, 8, 4, 7]

war(player1_deck, player2_deck)

