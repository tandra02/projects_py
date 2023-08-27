print('\nExam Grade Calculator \n')
exam = input('\nPlease enter the name of the exam: \n')
maxScore = int(input('\nPlease enter the max. possible score: \n'))
yourScore = int(input('\nPLease enter your score: \n'))
result = float((yourScore / maxScore) * 100)
final = round(result,2)
if result >= 90 or result == 100:
  print('You got', final,'% which is an A+')
elif result >= 80 and result <= 89:
  print('You got', final,'% which is an A')
elif result >= 70 and result <= 79:
  print('You got', final,'% which is a B+')
elif result >= 60 and result <= 69:
  print('You got', final,'% which is a B')
elif result >= 50 and result <= 59:
  print('You got', final,'% which is a C+')
elif result >= 40 and result <= 49:
  print('You got', final,'% which is a C')
elif result >= 30 and result <= 39:
  print('You got', final,'% which is a D')
else:
   print('You got', final,'% which is a F')