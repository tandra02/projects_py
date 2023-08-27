import os,time

ToDoList = []


def printList():
  print()
  counter = 1
  for item in ToDoList:
    print(f'{counter}.{item}')
    counter += 1
  time.sleep(2)  
  print()


while True:
  title = ('To Do List')
  subtitle = ('------Menu-----')
  print(f'\033[1;35m {title:>33}')
  print(f'\n\033[1;34m{subtitle:>37}')
  menu = input("\n\033[1;36m If you want to \n\n 1.Add \n 2.Remove \n 3.View the list?: \t")
  if menu == "1":
    item = input("What do you want to add to your list?: ")
    ToDoList.append(item)
  elif menu == "2":
    item = input("What is the last item you put in the list?: ")
    if item in ToDoList:
      ToDoList.remove(item)
    else:
      print(f"{item} was not in the list")
  elif menu == "3":
    printList()
  time.sleep(2)
  os.system('clear')
printList()
