import time

pizza = []
try:
  f = open("pizza.txt", "r")
  pizza = eval(f.read())
  f.close()
except:
  print("ERROR: No existing pizza list, using a blank list")

def addPizza():
    print()
    quantity = int(input("How many pizza you want to order >\n"))
    size = int(input("\nWhat size would that be(in inch) >\n"))
    name = input("\nName please >\n").capitalize()
    row = [quantity,size,name]
    if row not in pizza:
        pizza.append(row)
        cost = quantity * size
        print(f"Thanks for ordering from us {name}, Your total is {cost} doller.")
        print()

def viewPizza():
  print(f'\n{"Name":^15}{"Quantity":^15}{"Size":^15}')
  print("-" * 45)
  for row in pizza:
    print(f'{row[2]:^15}{row[0]:^15}{row[1]:^15}')
  print()
  time.sleep(4)
  
while True:
    user = input("Do you want to\n1.Add,\n2.View the order? ")
    if user == "1":
        addPizza()
    elif user == "2":
        viewPizza()
        exit()

    f = open("pizza.txt", "w")
    f.write(str(pizza))
    f.close()
