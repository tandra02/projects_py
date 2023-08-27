print('Quiz game')
print('--------------')
print()
print()
name = input('What is your name?')
print('\nHello!', name, 'I hope you are having a good day.')
print()

questions = ("What is Shakespeare's shortest play?",
             "In Harry Potter, where does Vernon Dursley work?",
             "Who has won the most Oscar of all the time?",
             "Who designed the Eiffel Tower?", "How many digits are in Pi?")

answers = ("The Comedy of Errors", "Grunnings", "Walt Disney",
           "Gustave Eiffel", "infinite numbers")
score = 0
guesses = []
question_number = 0
ready = input('Are you ready for the game?\n')
if ready == 'yes'.lower():
  for question in questions:
    print()
    print(question)
    guess = input("Answer: ")
    if guess == answers[question_number]:
      score += 1
      print("Correct!")
    else:
      print("Incorrect.")
      print(f'{answers[question_number]} is the correct answer.')
    question_number += 1

print()

score = int(score / len(questions) * 100)  #typecast it as an integer 
# here len(questions) checks the total number of questions
print(f"Your score is {score}%")
