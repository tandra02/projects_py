import random

card = [
  'Professors X', 'Cyclops', 'Rogue', 'NIghtcrawler', 'Mystique',
  'Quicksilver', 'Wolverine'
]  #stores superheroes in a list

superHero = {}
score = 0
player1_score = 0
player2_score = 0

while True:
  title = ('Superpower Faceoff: Player vs. Random')
  print(f'\n\033[1;7;36;40m{title:^99}')
  print("\033[0m")
  #choosing random cards from 2 players
  player1_card = random.choice(card)
  player2_card = random.choice(card)
  print(f"\n\033[1;39mPlayer 1's card is \033[1;32m{player1_card}")
  print(f"\n\033[39mplayer2's card is \033[35m{player2_card}")

  #getting input from user based on the stats
  intelligence = int(input('\n\033[1;32mEnter the Intelligence level of player 1:\n\033[1;32m'))
  agility = int(input('\nEnter the Agility level of player 1:\n'))
  healing_power = int(input('\nEnter the Healing Power level of player 1:\n\033[1;32m'))
  telekinetic = int(input('\nEnter the Telekinetic level of player 1:\n\033[1;32m'))

  # Store the stats in a list
  stat_choice = ['intelligence', 'agility', 'healing_power', 'telekinetic']
  #choosing random stats from the list
  random_stat_choice = random.choice(stat_choice)
  print(f"\n\033[39mRandom stats choice is \033[35m{random_stat_choice}")

  # Generate random stats for Player 2
  player2_stat = random.randint(1, 100)  # Replace 1 and 100 with your desired range
  print(f"\033[39mPlayer 2's {random_stat_choice}: \033[35m{player2_stat}")

  # Comparing stats and determining the winner
  if random_stat_choice == 'intelligence':
    if intelligence > player2_stat:
      print("\033[1;32mPlayer 1 wins this round!")
      player1_score += 1
    elif intelligence < player2_stat:
      print("\033[35mPlayer 2 wins this round!")
      player2_score += 1
    else:
      print("It's a tie!")
  elif random_stat_choice == 'agility':
    if agility > player2_stat:
      print("\033[1;32mPlayer 1 wins this round!")
      player1_score += 1
    elif agility < player2_stat:
      print("\033[35mPlayer 2 wins this round!")
      player2_score += 1
    else:
      print("It's a tie!")
  elif random_stat_choice == 'healing_power':
    if healing_power > player2_stat:
      print("\033[1;32mPlayer 1 wins this round!")
      player1_score += 1
    elif healing_power < player2_stat:
      print("\033[35mPlayer 2 wins this round!")
      player2_score += 1
    else:
      print("It's a tie!")
  elif random_stat_choice == 'telekinetic':
    if telekinetic > player2_stat:
      print("\033[1;32mPlayer 1 wins this round!")
      player1_score += 1
    elif telekinetic < player2_stat:
      print("\033[35mPlayer 2 wins this round!")
      player2_score += 1
    else:
      print("It's a tie!")

  play_again = input(
    "\033[39mDo you want to play again? (\033[31myes or no): ")
  if play_again.lower() == "yes":
    continue
    print("\033[0m")  # Reset color
  else:
    break