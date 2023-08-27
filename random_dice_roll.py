import random

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518") unicode for dice art
#● ┌ ─ ┐ │ └ ┘


dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")}
diceArt = []
def rollDice(user):
  while True:
    dice = random.randint(1,user)
    print('You rolled')
    for line in dice_art[dice]:
            print(line)
    second_input = input("\nDo you want to roll again?(yes or no)")
    if second_input.lower()=="yes":
      continue
    else:
      break
user = int(input('How many sides?: '))
rollDice(user)