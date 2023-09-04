f = open("high.score", "r")
lines = f.readlines()

# Using a list comprehension to extract scores as integers
scores = [int(line.split()[1]) for line in lines]

# Finding the maximum score and its index
max_score = max(scores)
max_score_index = scores.index(max_score)

# Getting the corresponding winner's name using the index
winner_name = lines[max_score_index].split()[0]

print(f"The winner is {winner_name} with a score of {max_score}")
