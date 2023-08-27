#storing user input in the dictionary
myUser = {}

myUser["name"] = input("Input your name > ").capitalize().strip()
myUser["DOB"] = input("Input your date of birth > ").capitalize().strip()
myUser["phone"] = input("Input your telephone number > ").capitalize().strip()
myUser["email"] = input("Input your email > ").capitalize().strip()
myUser["address"] = input("Input your address > ").capitalize().strip()


print()
title = ('Contact Card.')
print(f"""\033[1;34m{title:^62}""")
print(f"""\033[0;37mName: {myUser["name"]}""")
print(f"""DOB: {myUser["DOB"]}""")
print(f"""Phone number: {myUser["phone"]}""")
print(f"""Email: {myUser["email"]}""")
print(f"""Address: {myUser["address"]}""")
print(
  f"""\nHi {myUser['name']}. Our dictionary says that you were born on {myUser['DOB']}, we can call you on {myUser['phone']}, email {myUser['email']}, or write to {myUser['address']}.""")