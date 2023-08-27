print('\nGeneration Identifier\n')
birthYear = int(input("Which year were you born?\n"))
if birthYear >= 1883 and birthYear <= 1900:
  print("Oh! Lost Generation it is.")
elif birthYear >= 1901 and birthYear <= 1927:
  print("Greatest Generation!")
elif birthYear >= 1928 and birthYear <= 1945:
  print("Silent Generation!")
elif birthYear <= 1946 and birthYear <= 1964:
  print("Baby Boomers")
elif birthYear >= 1965 and birthYear <= 1980:
  print("Generation X!")
elif birthYear >= 1981 and birthYear <= 1996:
  print("Millenials")
elif birthYear >= 1997 and birthYear <= 2012:
  print("Generation Z")
else:
  print('Generation Alpha')