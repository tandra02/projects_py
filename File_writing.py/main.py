 #saving to files
f = open("high.score", "a+") #'a' means append - add to the end of the file. it will crash the file if it doesn't exist.
#'a+' means 'add to the end of the file, or create a new one if it doesn't exist'.

while True:
  user = input("Enter your three letter initials > ")
  f.write(f"{user}\t")
  userAgain = input("and score > ")
  f.write(f"{userAgain}\n")
  repeat = input("Do you want to add more(y/n):") 
  if repeat == 'y':
   continue
  else:
    break
f.close()
