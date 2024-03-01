def war(deck1, deck2):
    # Check if any player runs out of cards
    if not deck1:
        print("Player 2 is victorious!")
        return [], deck2
    elif not deck2:
        print("Player 1 victorious!")
        return deck1, []
    
    # Draw top cards
    card1 = deck1[0]
    card2 = deck2[0]
    
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
    print("War: Player 1 face down card:", deck1[0] )
    print("War: Player 2 face down card:", deck2[0] )
    print("War: Player 1 face up card:",  deck1[1] )
    print("War: Player 2 face up card:",  deck2[1])

    if deck1[1] > deck2[1]:
        winner = 1
        deck1 = deck1[2:] + [deck1[0], deck2[0], deck1[1], deck2[1]]
        deck2 = deck2[2:]
    elif deck1[1] < deck2[1]:
        winner = 2
        deck2 = deck2[2:] + [deck1[0], deck2[0], deck1[1], deck2[1]]
        deck1 = deck1[2:]
    else:
        print("War: Another Tie. War is declared.")
        winner, rd1, rd2 = gotoWar(deck1[2:], deck2[2:])
        if winner == 1:
            deck1 = deck1[2:] + rd1 + [deck1[0], deck2[0], deck1[1], deck2[1]]
            deck2 = rd2
        elif winner == 2:
            deck2 = deck2[2:] + rd2 + [deck1[0], deck2[0], deck1[1], deck2[1]]
            deck1 = rd1



    return winner, deck1, deck2



print("Prepare for War (The CardGame).")
player1_deck = [12, 9, 7, 4]
player2_deck = [12, 7, 8, 5]

war(player1_deck, player2_deck)

