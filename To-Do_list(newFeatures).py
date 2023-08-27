import os, time

ToDoList = []
index = 1


def printList():
  print()
  for item in ToDoList:
    print(f'{item}')
    time.sleep(2)


def viewList():
  print()
  for index in range(1,len(ToDoList) + 1):
    print(f'{index}.{ToDoList[index-1]}')
    time.sleep(2)

def editList():
  global ToDoList
  item_found = False
  for i in range(len(ToDoList)):
      if ToDoList[i] == item:
       ToDoList[i] = new
       item_found = True
       break
  if not item_found:
      print("Item not found in the list.")

while True:
  title = ('To Do List')
  subtitle = ('------Menu-----')
  print(f'\033[1;35m {title:>33}')
  print(f'\n\033[1;34m{subtitle:>37}')
  menu = input(
    "\n\033[1;36m If you want to \n\n 1.Add \n 2.Remove \n 3.Edit \n 4.View the list?: \t"
  )
  if menu == '1':
    item = input('\033[1;31m Enter an item to be added: ').capitalize().strip()
    if item not in ToDoList:
      ToDoList.append(item)
    else:
      print('You have already entered the item.')
    time.sleep(2)
    os.system('clear')
  elif menu == '2':
    item = input('\033[1;31m Enter an item to be removed: ')
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
        break
  elif menu == '3':
    item = input('\033[1;31m Enter the item you want to edit: ')
    new = input('\033[1;31m Edit the item: ')
    editList()
    print(ToDoList)
    time.sleep(2)
    
  elif menu == '4':
    viewList()
    break
  os.system('clear')
