#Using recursion
def factorial(value):
  if value == 1:  # end condition
    return 1
  else:
    return value * factorial(value - 1)
  
# Get user input
user_input = int(input("Enter a number to calculate its factorial: "))
result = factorial(user_input)
print(f"The factorial of {user_input} is {result}")