# 2d Dictionaries
mokeBeast = {}


def prettyPrint(mokeBeast):
  print("\033[37m Mokébeast Details:\n")
  print("\tName\t\tType\t\tSpecial Move\t\tHP\t\tMP")
  for name, value in mokeBeast.items():
    if value['Type'] == 'Earth':
      color_code = "\033[32m"  # Green for Earth
    elif value['Type'] == 'Fire':
      color_code = "\033[31m"  # Red for Fire
    elif value['Type'] == 'Air':
      color_code = "\033[35m"  # Magenta for Air
    elif value['Type'] == 'Water':
      color_code = "\033[34m"  # Blue for Water
    elif value['Type'] == 'Spirit':
      color_code = "\033[33m"  # Yellow for Spirit

    row = f"{color_code}{name:^12}|{value['Type']:^10}|{value['SpecialMove']:^22}|{value['HP']:^6}|{value['MP']:^6}"
    print(row)
  print("\033[0m")  # Reset color


print(
  '\n\033[1;36m Welcome to MokéBeast details creator. Please provide the following details about your MokéBeast:\n'
)

while True:

  input_list = input(
    "\n\033[0;35mInput the name of your MokéBeast, Choose the type of your MokéBeast(Earth, Fire, Air, Water, or Spirit), What the special move of your MokéBeast, Enter the starting HP of your MokéBeast, Enter the starting MP of your MokéBeast:\n "
  ).split()

  name = input_list[0]
  type = input_list[1]
  special_move = input_list[2]
  hp = input_list[3]
  mp = input_list[4]

  mokeBeast[name] = {
    "Type": type,
    "SpecialMove": special_move,
    "HP": hp,
    "MP": mp
  }

  user = input(
    "\033[30;40m\n Do you want to continue creating another MokéBeast (Yes or No)?:\n"
  )
  if user.lower() == "yes":
    continue
  else:
    break

prettyPrint(mokeBeast)