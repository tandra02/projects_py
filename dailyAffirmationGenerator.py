
print("Hello. Welcome to your daily affirmation generator.")
name = input("What is your name?").capitalize()

DOW = input("What is the day of the week?").capitalize()


if name =="Mark" or name.capitalize()=="David":
 if DOW == "Monday":
   print("It is going to be a great Monday", name)
 elif DOW == "Tuesday":
   print("What a wonderful Tuesday it is", name)
 elif DOW == "Wednesday":
   print("Happy Hump Day", name)
 elif DOW == "Thursday":
   print(name,"your week is almost over!")
 elif DOW == "Friday":
   print(name, "It's FRIDAY!")
elif DOW == "Saturday":
   print(name, "Finally it's Saturday!")
elif DOW == "Sunday":
   print(name, "Today i feel amazing!")

elif name == "Afsana":
 DOW = input("What is the day of the week?")
 if DOW == "Monday":
   print("It is already Monday!!", name)
 if DOW == "Tuesday":
   print("Today can't be Tuesday", name)
 if DOW == "Wednesday":
   print("You look chipper today", name)
 if DOW == "Thursday":
   print(name,"you are doing a great job!")
 if DOW == "Friday":
   print(name, "it's FRIDAY!")
elif DOW == "Saturday":
   print(name, "Finally it's Saturday!")
elif DOW == "Sunday":
   print(name, "Ugh I can't do this anymore")
else:
 print("I do not know your name, but I hope you are having a great day!")