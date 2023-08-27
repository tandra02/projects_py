import random, os, time

bingo = []

def randomNumber(): #for generating random numbers
  number = random.randint(1,90)
  return number

def rowPrint(): 
  for row in bingo: # Iterates through each row in the bingo list
    for item in row: # Iterates through each item in the current row
      print(f'{item:^10}', end ='|') # Prints the item with centered alignment and adds a vertical bar
    print()  # Prints an empty line to move to the next line after printing a row


def createCard():
  global bingo
  numbers = []  # This is like an empty bag where we'll put our bingo numbers
  for i in range(8): #generate 8 random numbers and sort them ascending order
    num = randomNumber()

    # Now we're checking if we already have this number in our bag
    while num in numbers:
      num = randomNumber() #If we do we need a new number
    numbers.append(randomNumber()) # We're putting the number we got into our bag
  
  numbers.sort()
  
  bingo = [ [ numbers[0], numbers[1], numbers[2]],
            [ numbers[3], "BG", numbers[4] ],
            [ numbers [5], numbers[6], numbers[7]]
          ]

createCard()
while True:
  rowPrint()
  num = int(input("Next Number: "))
  for row in range(3):
    for item in range(3):
      if bingo[row][item] == num:
        bingo[row][item] = "X"

  exes = 0
  for row in bingo:
    for item in row:
      if item=="X":
        exes+=1

  if exes == 8:
    print("You have won")
    break

  time.sleep(1)
  os.system("clear")
