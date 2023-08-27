import random

number = input('Type a number:\n')
try:
    number = int(number)
    if number <= 0:
        print("Please enter a value greater than 0.")
        quit()
except ValueError:
    print("Please enter a valid number.")
    quit()


randomNumber = random.randint(0, number)
guess = 0

while True:
    guess += 1
    userGuess = input('Guess a number:\n')
    try:
      userGuess = int(userGuess)
      if number <= 0:
          print("Please enter a value greater than 0.")
          quit()
    except ValueError:
        print("Please enter a valid number.")
        continue
    if userGuess == randomNumber:
        print("This is the lucky number!")
        break
    elif userGuess > randomNumber:
        print("Too high")
    else:
        print("Too low")
print(' You got it  in', guess, 'guesses')
