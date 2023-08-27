print('List Generator\n\n')

start = int(input('Start at: '))
end = int(input('End before: '))
increment = int(input('Increment between vales: '))
print('\n')

for i in range (start, end, increment):
  print(i)