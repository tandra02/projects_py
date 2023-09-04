def palindrome(word):
  if len(word)<=1: # because a single lettered word is palindrome
    return True
  if word[0] != word[-1]:
    return False
  return palindrome(word[1:-1]) #removes first and last character of the word and checks recursively
user_input = input("Enter a word to check palindrome > ")
print(palindrome(user_input))