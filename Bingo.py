import random

bingo = [] #empty list

def randomNumber(): #subroutine
  number = random.randint(1,90)
  return number

def rowPrint():
  for row in bingo:
    for item in row:
      print(f'{item:^10}', end =" | ")
    print()
numbers = []
for i in range(8):
  numbers.append(randomNumber())

#numbers.sort() #sorting numbers list in an ascending order

bingo = [ [ numbers[0], numbers[1], numbers[2]],
          [ numbers[3], "BINGO", numbers[4] ],
          [ numbers [5], numbers[6], numbers[7]]
        ]
while True:
  rowPrint()
  repeat = input("\nDo you want to repeat(yes/no)?\t")
  if repeat == "yes":
   continue
  else:
   break