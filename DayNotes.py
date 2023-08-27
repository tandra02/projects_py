print('30 Days Down - What did you think?')

for i in range(1, 31):
  d1 = input(f'\nDay {i} : ')
  speech = f'You thought Day {i} was'
  print(f'{speech:^55}\n{d1:^55}')