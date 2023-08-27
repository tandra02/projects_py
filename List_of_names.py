import os, time

listOfNames = []

def addNames():
  fname = input("What's your first name?: ").strip().capitalize()
  sname = input("What's your last name?: ").strip().capitalize()
  full_name = f'{fname} {sname}'.strip()
  if full_name not in listOfNames:
    listOfNames.append(full_name)
    print(f'\nAdded: {full_name}')
  else:
    print("ERROR: Duplicate name")
  time.sleep(1)

def viewList():
  print("")
  for index in range(1,len(listOfNames) + 1):
    print(f'{index}-> {listOfNames[index - 1]}')
    time.sleep(2)


while True:
  user = input('Do you want to 1.Add,2.Quit or 3.View: ')
  if user == '1':
    addNames()
  elif user == '2':
    exit()
  elif user == '3':
    viewList()
  time.sleep(1)
  os.system('clear')
