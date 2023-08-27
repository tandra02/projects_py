mokeBeast = {
  "Name": None,
  "Type": None,
  "SpecialMove": None,
  "HP": None,
  "MP": None
}

print(
  '\n\033[1;36;40m Welcome to MokeBeast details creator. Please provide the following details about your MokeBeast: '
)
input_list = input(
  "\n\033[0;35;40mInput the name of your MokeBeast, Choose the type of your MokeBeast(Earth,Fire,Air,Water or Spirit), What the special move of your MokeBeast, Enter the starting HP of your MokeBeast, Enter the starting MP of your MokeBeast:\n "
).split()

mokeBeast["Name"] = input_list[0]
mokeBeast["Type"] = input_list[1]
mokeBeast["SpecialMove"] = input_list[2]
mokeBeast["HP"] = input_list[3]
mokeBeast["MP"] = input_list[4]

print(
  '\n\033[1;37;40mCongratulations! Here are the details of your MokeBeast:\n ')
for key, value in mokeBeast.items():
  if input_list[1].capitalize() == 'Earth': #green
    print(f"\033[32m{key:<15}: {value}")
  elif input_list[1].capitalize() == 'Fire': #red
    print(f"\033[31m{key:<15}: {value}")
  elif input_list[1].capitalize() == 'Air': #purple
    print(f"\033[35m{key:<15}: {value}")
  elif input_list[1].capitalize() == 'Water': #blue
    print(f"\033[34m{key:<15}: {value}")
  elif input_list[1].capitalize() == 'Spirit': #yellow
    print(f"\033[33m{key:<15}: {value}")
print(
  f"\nYour beast is called {input_list[0]}. It is an {input_list[1]} beast with a special move of {input_list[2]}")