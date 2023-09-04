import time
inventory = []
count = 0
try:
  f = open("inventory.txt","r")
  inventory = eval(f.read())
  f.close()
except:
  print("ERROR: No existing inventory list, using a blank list.")
def viewList():
  print()
  seen = [] #empty list will keep track of the processed items
  for item in inventory:
    if item not in seen: #only takes item which does not exists in seen[] means has not been printed yet.
      print(f"{item} {inventory.count(item)}") #tracks occurrences of the item in the inventory list.
      seen.append(item)
  time.sleep(2)
  print()
def removeList():
  print()
  if item in inventory:
    inventory.remove(item)
    print(f"{item} has been removed to your inventory.")
  else:
    print(f"{item} doesn't exist in inventory.")
    time.sleep(2)

while True:
  user = input("\nDo you want to\ni.Add,\nii.View\niii.Remove >\n")
  if user =='i':
    item = input("What item you want to add to your inventory > ").capitalize()
    inventory.append(item)
    print(f"{item} has been added to your inventory.")
    time.sleep(2)
  elif user == 'ii':
    viewList()
  elif user == "iii":
    item = input("What item you want to remove from your inventory >\n").capitalize()
    removeList()
    
  f = open("inventory.txt", "w")
  f.write(str(inventory))
  f.close()  

