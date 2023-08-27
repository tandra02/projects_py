import random, os, time

listOfWords = ["apple", "orange", "grapes","pear","banana","jackfruit","coconut","mango"] # given list
letterPicked = [] # empty list which will be used for transferring 'GUESSED LETTER'
lives = 7

word = random.choice(listOfWords) # for randomization of string

while True:
  time.sleep(1)
  os.system("clear")
  #hangman art
  print("""
   _________
  |         |
  |         {0}
  |        {3}{1}{2}
  |        {4} {5}
  |
__|__
|   |
|___|
""".format(
    "O" if lives < 7 else "",
    "|" if lives < 6 else "",
    "\\" if lives < 5 else "",
    "/" if lives < 4 else "",
    "/" if lives < 3 else "",
    "\\" if lives < 2 else "",
    "\\" if lives < 1 else ""
))
  letter = input("Choose a letter(fruits edition): ").lower()
  
  if letter in letterPicked: # checks the existance of current letter in the 'EMPTY LIST'
    print("You've tried that before")
    continue
  else:  
    letterPicked.append(letter) # This line adds the guessed letter to the list
    
  if letter in word:
    print("You found a letter")
  else:
    print("Nope, not in there")
    lives -= 1
  
  allLetters = True # keeps track of all the guessed letter in the word
  print()
  for i in word: # iterates each charcter(i) the word
    if i in letterPicked: #checks if the current character(i) already exists in the list
      print(i, end="") # if true then the character prints as it is, breaks the loop then go straight to check if allLetters,when that's false go through this if loop again.
    else:
      print("_", end="") # this represents unguessed letter
      allLetters = False
  print() # prints a new line

  if allLetters:
    print(f"You won with {lives} left!")
    break

  if lives<=0:
    print(f"You ran out of lives! The answer was {word}")
    break
  else:
    print(f"Only {lives} left")