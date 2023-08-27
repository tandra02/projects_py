print("Uh, oh, you've been given a", '\033[31m', 'warning', '\033[0m', 'for being a bad, bad person ')
print("\n\033[0;32m","Thomas was sure that", "\033[0;31m", "escape", "\033[0;37m", "from the","\033[1;33m", "Maze","\033[0;33m", "would mean", "\033[0;31m", "freedom", "\033[0;35m", "for him and the Gladers.","\033[1;36m", "But WICKED isn't done with them yet.","\033[0;37m")
print("\n")
name = input("\033[1;37m What is your name? >\033[1;35m")
enemy = input("\033[1;37m What is your worst enemy's name? >\033[1;35m")
superpower = input("\033[1;37m What is your superpower? >\033[1;35m")
place = input("\033[1;37m Where do you live? >\033[1;35m")
favFood = input("\033[1;37m What is your favourite food? >\033[1;35m")
print("\n\n\033[1;36mWelcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!\033[1;37m")
print(f"\n\n\033[1;32m Hello \033[1;35m{name}!\033[1;32m Your ability to \033[1;35m{superpower}\033[1;32m will make sure you never have to look at \033[1;35m{enemy}\033[1;32m again. Go eat \033[1;35m{favFood}\033[1;32m as you walk down the streets of \033[1;35m{place}\033[1;32m and use \033[1;35m{superpower}\033[1;32m for good and not evil!\033[1;37m")

print("\n\n\n")
colors = {
    'r': '\033[31m',  # Red
    'b': '\033[34m',  # Blue
    'g': '\033[32m',  # Green
    'p': '\033[35m',  # Purple
    'y': '\033[33m',  # Yellow
    'reset': '\033[0m'  # Reset color which is an escape code
} # using a dictonary

user = input('Enter your favorite quote: ')
color_to_use = None

for letter in user:
    if letter.lower() in colors:
        color_to_use = letter.lower() # if letter matched with colors dictonary it will set to that color
    
    if letter == ' ': # for space
        color_to_use = 'reset'
    
    if color_to_use: # for already colored letters
        print(colors[color_to_use], end='')
    
    print(letter, end='')

print(colors['reset'])  # Reset color at the end