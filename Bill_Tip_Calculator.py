print('\nTip Calculator\n')
myBill = float (input('How much did you spend?:\n '))
tip = float (input('What percentage do you want to tip?:\n'))
numberOfPeople = int(input('How many people in the group?:\n '))
amount = (tip/100)*100
answer = amount + myBill
final = answer/numberOfPeople
final = round(final, 2)
print('You all owe', final)