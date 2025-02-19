import random
random_numbers = []  # Creates an empty list to store random numbers
# Generates 10 random numbers between 1 and 100
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# replace numbers > 50 with a random number between (20-30),
# and numbers <= 50 with "XX"
for i in range(len(random_numbers)):  # Loop through each index
    if random_numbers[i] > 50:  # If the number is greater than 50
        random_numbers[i] = random.randint(20, 30)  # Replace with a number between 20 and 30
    else:  # If the number is less than or equal to 50
        random_numbers[i] = "XX"  # Replace with "XX"

# Print the modified list
print(random_numbers)