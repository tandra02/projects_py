print('Character Stat Generator')
import random

def generate_health():
    dice = random.randint(1, 6)
    another = random.randint(1, 6)
    return dice * another
  
while True:
    name = input('\nName your warrior: ')
    character_health = generate_health()
    print(f"Their character health is {character_health}")

    character_input = input("Do you want to create another character? (yes/no): ")
    if character_input.lower() != "yes":
        break
