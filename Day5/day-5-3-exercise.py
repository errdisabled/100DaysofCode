# Add only the even numbers from 1 to 100 to themselves

# Initialize result variable
total = 0

# Create the loop that gets the result
for number in range(1, 101):
    if number % 2 == 0:
        total += number

# Print the result
print(total)
