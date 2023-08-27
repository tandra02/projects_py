import os, time

listOfEmail = []


def view():
  os.system("clear")
  print("List of Emails")
  print()
  for index in range(len(listOfEmail)):
    print(f"{index}: {listOfEmail[index]}")
  time.sleep(1)


def spam():
  os.system('clear')
  print("listOfEmail")
  print()
  for extra in range(len(listOfEmail)):
    print(
      f"\nDear {listOfEmail[extra]},\n It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter because that's neat. We might just do that anyway.\n\n Love and hugs,\n Ian Spammington III"
    )
  time.sleep(12)


while True:
  title = ('SPAMMER Inc.')
  subtitle = ('------Menu-----')
  print(f'\033[1;35m {title:>34}')
  print(f'\n\033[1;34m{subtitle:>36}')
  menu = input(
    "\n1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu == "2":
    email = input("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    view()
  elif menu == '4':
    spam()
  time.sleep(1)
  os.system("clear")
