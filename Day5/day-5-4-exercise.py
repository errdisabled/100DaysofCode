# Classic FizzBuzz game code

# Print each number from 1 to 100
for number in range(1, 101):
    # add an if else statement to meet the criteria
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
