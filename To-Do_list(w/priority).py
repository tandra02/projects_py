import os, time

ToDoList = []
index = 1


def addList():
  print()
  global ToDoList
  item = input(
    '\033[1;31m\nWhat the to do list is about:\n').capitalize().strip()
  dueTime = input('\nWhen the To-do list is due (dd/mm/yy)?\n').strip()
  priority = input('\nSet the priority(High, Medium, Low):\n').strip()
  row = [item, dueTime, priority]
  if row not in ToDoList:
    ToDoList.append(row)
  else:
    print('You have already entered the item.')
  time.sleep(2)
  os.system('clear')


def removeList():
  global ToDoList
  item = input('\033[1;31mEnter an item to be removed: ').capitalize().strip()
  if item in ToDoList:
    sure = input("Are you sure you want to remove the item?(Yes/No): ")
    if sure == 'yes':
      user = input(
        'Do you want to completely remove the To-do list?(Yes/No): ')
      if user == 'yes':
        ToDoList = []
      else:
        ToDoList.remove(item)
    else:
      print("Item removal canceled.")
  else:
    print(f"{item} not found in the To-Do list.")
  time.sleep(3)


def viewByPriority(priority):
  print()
  print(f'\n{"Title":^15}{"Due Time":^15}{"Priority":^15}')
  print("-" * 45)
  for item in ToDoList:
    if item[2] == priority:
      print(f'{item[0]:<20}{item[1]:<15}{item[2]:<10}')
  print()


def viewList():
  print("\n\033[1;34m Your To-Do List:")
  item = input('Do you want to view all (v) or priority (p) wise?\n')
  if item.lower() == 'v':
    print(f'\n{"Title":^15}{"Due Time":^15}{"Priority":^15}')
    print("-" * 45)
    for row in ToDoList:
      print(f'{row[0]:^15}{row[1]:^15}{row[2]:^15}')
    print()

  elif item.lower() == 'p':
    user = input('\n1.High\n2.Medium\n3.Low priority?\n')
    if user == '1':
      viewByPriority(
        "High")  # Call the viewByPriority function for High priority
    elif user == '2':
      viewByPriority(
        "Medium")  # Call the viewByPriority function for Medium priority
    elif user == '3':
      viewByPriority(
        "Low")  # Call the viewByPriority function for Low priority
  time.sleep(2)


def editList():
  user = input("Enter the item you want to edit:\n").capitalize()
  for i in range(len(ToDoList)): #iterates through each item in ToDoList
    if ToDoList[i][0] == user: #compares each element(items{first element of each list}) of ToDoList with user input
      new = input('\033[1;31m What information you want to edit \n1.Item\n2.Due date\n3.Priority:\n')
      if new == '1':
        new_item = input('\033[1;31m Enter the new item: ')
        ToDoList[i][0] = new_item #updates current item's title with new title
      elif new == '2':
        new_date = input('\033[1;31m Edit the due date: ')
        ToDoList[i][1] = new_date
      elif new == '3':
        new_priority = input('\033[1;31m Edit the priority: ')
        ToDoList[i][2] = new_priority
      break


while True:
  title = ('To Do List')
  subtitle = ('------Menu-----')
  print(f'\033[1;35m {title:>33}')
  print(f'\n\033[1;34m{subtitle:>37}')
  menu = input("\n\033[1;36m If you want to \n\n 1.Add \n 2.Remove \n 3.Edit \n 4.View \n 5.Quit the list?:\t")
  print("\033[0m")
  if menu == '1':
    addList()

  elif menu == '2':
    removeList()

  elif menu == '3':
    editList()

  elif menu == '4':
    viewList()
  elif menu =='5':
    exit()

  os.system('clear')