import os, time, random

round = 0


#Legend 1
#health = (6-sided roll * 12-sided roll/2 )+10
def health_stat1():
  d1 = random.randint(1, 6)
  d2 = random.randint(1, 12)
  stat = (d1 * d2) // 2
  return stat + 10

#strength = (6-sided roll * 12-sided roll/2 )+12
def strength_stat1():
  d1 = random.randint(1, 6)
  d2 = random.randint(1, 12)
  s = (d1 * d2) // 2
  return s + 12


#Legend 2
def health_stat2():
  d1 = random.randint(1, 6)
  d2 = random.randint(1, 12)
  stat = (d1 * d2) // 2
  return stat + 10


def strength_stat2():
  d1 = random.randint(1, 6)
  d2 = random.randint(1, 12)
  s = (d1 * d2) // 2
  return s + 12


while True:
  print('⚔️ 🗡️  Character Builder 🗡️ ⚔️️')
  time.sleep(1)
  name1 = input('\nName your Legend: ')
  time.sleep(1)
  character_type = input(
    'Character Type(Human 👩🏽, Elf 🧝🏽‍♀️, Wizard 🧝🏽‍♀️, Orc 🧟‍♂️): ')
  time.sleep(1)
  print(f"\n{name1}\nTheir character health is 🩹 {health_stat1()}")
  time.sleep(1)
  print(f"Their character strength is 🏋🏼 {strength_stat1()}")
  time.sleep(1)

  print('\nWho are they battling? ')
  name2 = input('\nName your Legend: ')
  time.sleep(1)
  character_type = input('Character Type(Human, Elf, Wizard, Orc): ')
  time.sleep(1)
  print(f"\n{name2}\nTheir character health is 🩹 {health_stat2()}")
  time.sleep(1)
  print(f"Their character strength is 🏋🏼 {strength_stat2()}")
  time.sleep(1)
  character_input = input(
    "Do you want to create another character? (yes/no): ")
  if character_input.lower() != "yes":
    break
os.system('clear')
print('🏴󠁡󠁦󠁷󠁡󠁲󠁿 BATTLE TIME 🏴󠁡󠁦󠁷󠁡󠁲󠁿')
print('\nThe battle begins! 🤺 ')


def battle_player():
  return random.randint(1, 6)


while True:
  round += 1
  print(f'\nRound {round}\n')
  player1_strength = strength_stat1()
  player2_strength = strength_stat2()

  player1_roll = battle_player()
  player2_roll = battle_player()
  if player1_roll > player2_roll:
    print(f'{name2} takes a hit with 8 damage')
    time.sleep(3)
    player2_strength -= 8
  else:
    print(f'{name1} takes a hit with 8 damage')
    time.sleep(3)
    player1_strength -= 8
  print(f"\n{name1}\nTheir character health is 🩹 {player1_strength}")
  print(f"\n{name2}\nTheir character health is 🩹 {player2_strength}")

  os.system('clear')
  if player1_strength < player2_strength:
    if round > 4 or player1_strength <= 0:
      print(f"\n{name2} wins the battle 🏆 !")
      time.sleep(3)
      break
  elif player2_strength < player1_strength:
    if round > 4 or player2_strength <= 0:
      print(f"\n{name1} wins the battle 🏆 !")
      time.sleep(3)
      break
  print(f"\n{name1}\n\nTheir final character health 🩹 is {player1_strength}")
  time.sleep(3)
  print(f"\n{name2}\nTheir final character health 🩹 is {player2_strength}")
  time.sleep(3)
