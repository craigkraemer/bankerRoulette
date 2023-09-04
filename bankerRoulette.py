# Import the random module
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# Count number of names in the list
count = len(names)
# Run the list thru the random number generator and correct the count for the index
number = random.randint(0, count - 1)
# Print the name associated with the randomly generated number allong with the output message
print(names[number] + " is going to buy the meal today!")