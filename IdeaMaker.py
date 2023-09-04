import random, time

def add():
  f = open("my.ideas","a+")
  content = input("Add an idea > ")
  f.write(f"{content}")
  f.write(f"\n")
  f.close()
  time.sleep(2)
def view():
  f = open("my.ideas","r")
  ideas = f.readlines()
  randomIdeas = random.choice(ideas)
  print(randomIdeas)
  f.close()
  time.sleep(3)
while True:
  user = input("Do you want to \n1.add\n2.view ideas > ")
  if user == '1':
    add()
  elif user == '2':
    view()
