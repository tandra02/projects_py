print('\nLoan Calculator\n')
print('$1000 over 10 years at 5% APR\n')
dollar = 1000
APR = 0.05
for year in range(10):
  dollar += (dollar*APR)
  print('year', year+1, 'is', round(dollar,2))