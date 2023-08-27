#using split
print('SuperHero Name Generator')

string = input ('\nEnter your full name, maiden name and city you were born: ').split()
fname = string[0].capitalize().strip()
sname =string[1].lower().strip()
mname = string[2].capitalize().strip()
city = string[3].lower().strip()

print(f'\nYour SuperHero name is: {fname[0:3]}{sname[0:3]}\t{mname[0:2]}{city[-3:]}') #first 3 letters from first and sur name, first 2 letters of maiden name and last 3 letters of the city
