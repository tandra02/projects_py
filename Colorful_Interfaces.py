#Interface 1
def colorChange(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")

title = f" 🎘  {colorChange('red')}={colorChange('white')}={colorChange('blue')}= {colorChange('yellow')}Music App {colorChange('blue')}={colorChange('white')}={colorChange('red')}={colorChange('white')} 🎘"
    

print(f'{title:^95}')
emoji =('🔥 ▶️')
song = ('Radio Gaga')
artist = ('Queen')
print(f'\n{emoji:>8} {song:>12}\n \033[33m{artist:>15}')
prev = ('PREV')
next = ('NEXT')
pause = ('PAUSE')
print(f'\n\n \033[37m {prev:>9}\n \033[32m {next:>15}\n \033[35m {pause:>22}')

#Interface 2
title = ('WELCOME TO')
emoji2 = ('--')
print(f'\n\n \033[0;37m{title:>37}\n \033[0;34m {emoji2:>25}  ARMBOOK  {emoji2}')
speech = ('Definitely not a rip off of')
speech2 = ('a certain other social')
speech3 = ('networking site.')
print(f'\n \033[1;33m{"":>29}{speech:<45}')  
print(f'{"":>35}{speech2:<45}')
print(f'{"":>42}{speech3:<45}')
honest =("Honest.")
username =('Username:')
password = ('Password:')
print(f'\033[0;31m{honest:>37}')
print(f'\n\033[0;37m{username:>38}\n{password:>38}')