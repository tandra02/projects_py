import random
greeting = ["Kamisaki", "Hello", "Hola", "হ্যালো", "Aloha", "Buna ziua", "Nnọọ", "Halló", "Witam"]
randomGreet = random.choice(greeting)
print(f"i am saying \033[1;31m{randomGreet}\033[0;37m, which is a greetings!")