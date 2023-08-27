print('Math Game!')
user = int(input('\nName your multilpes: '))
score = 0

for i in range(1,11):
  print(i, 'X', user, '=' )
  guess = int(input(""))
  mul = user*i
  if guess == mul:
    print("Thats absolutely correct! 🎊 ")
    score += 1
  else:
    print("Oh no, that is wrong 😟. ")
print('\n....')
print(f'\nYou scored {score} out of 10!')
  
