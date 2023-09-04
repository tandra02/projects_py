import os, time, random, shutil

ToDoList = []
index = 1
fileExists = True  #determine if the "to.do" file exists
try:
  f = open("to.do", "r")
  #eval is used to read a file and convert it to python list
  ToDoList = eval(f.read())
  f.close()
except:
  fileExists = False  #the file doesnot exist or error occurs


def printList():
  print()
  for item in ToDoList:
    print(f'{item}')
    time.sleep(2)


def editList():
  time.sleep(1)
  os.system("clear")
  find = input("Name of item to edit > ")
  found = False
  for row in ToDoList:
    if find in row:
      found = True
      ToDoList.remove(row)

  if not found:
    print("Couldn't find that")
    return
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  ToDoList.append(row)
  print("Added")


def viewList():
  print()
  for index in range(1, len(ToDoList) + 1):
    print(f'{index}.{ToDoList[index - 1]}')
    time.sleep(2)


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
    date = input("Set the Due Date > ")
    priority = input("Set your preferred priority > ").capitalize()
    row = [item,date,priority]
    if item not in ToDoList:
        ToDoList.append(row)
    else:
      print('You have already entered the item.')
    time.sleep(2)
    os.system('cls')

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
    editList()
  elif menu == '4':
    viewList()
    break
  os.system('cls')

  #file backup handling
  if fileExists:  #when its true
    try:
      os.mkdir("backups")  #create a directory named "backups" and store the copy of original to.do file
    except:
      pass
    #random is used to create random backup file name so that each backup file names are unique
    name = f"backup{random.randint(1,1000000000)}.txt"
    # Use shutil.copy to copy the "to.do" file to the "backups" directory with the generated backup name
    shutil.copy("to.do", os.path.join("backups", name))

  f = open("to.do", "w")
  f.write(str(ToDoList))
  f.close()
