# Importing the getpass module and renaming it as 'input' for better readability.
from getpass import getpass as input

# Function to get a valid move from the player.
def validMove():
    move = input('Select your move (R, P, or S):')
    if move in ['R', 'P', 'S']:
        return move
    else:
        print('Enter a valid move.')

# Printing the title for the game.
print("\n.....................................")
print('  E P I C   🪨  📄  ✂️    B A T T L E')
print(".....................................\n")

# Initializing variables to keep track of the game.
Round = 0
player1_wins = 0
player2_wins = 0

while True:
    # Incrementing the round counter.
    Round += 1

    # Displaying the current round number.
    print(f'\nRound {Round}\n')

    # Getting the moves from both players.
    player1 = validMove()
    player2 = validMove()

    # Comparing the moves and determining the outcome of the round.
    if player1 == 'R' and player2 == 'S':
        print('\nplayer2 is destroyed by player1 🪨 !')
        player1_wins += 1

    elif player1 == 'P' and player2 == 'R':
        print('\nplayer2 is covered by player1 📄 !')
        player1_wins += 1

    elif player1 == 'S' and player2 == 'P':
        print('\nplayer2 is in pieces by player1 ✂️ !')
        player1_wins += 1

    elif player1 == 'S' and player2 == 'R':
        print('\nplayer1 is destroyed by player2 🪨 !')
        player2_wins += 1

    elif player1 == 'R' and player2 == 'P':
        print('\nplayer1 is covered by player2 📄 !')
        player2_wins += 1

    elif player1 == 'P' and player2 == 'S':
        print('\nplayer1 is in pieces by player2 ✂️ !')
        player2_wins += 1

    else:
        print('It is a tie')

    # Checking if any player has won the game (reached 2 wins) and declaring the winner.
    if player1_wins >= 2 and player1_wins > player2_wins:
        print('Player 1 is the winner')
        break
    elif player2_wins >= 2 and player2_wins > player1_wins:
        print('Player 2 is the winner')
        break

    # Checking if there's a tie after Round 2 and declaring no clear winner.
    elif Round == 2 and player1_wins == player2_wins:
        print('It is a tie. No clear winner.')
        break