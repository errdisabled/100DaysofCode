import random

# split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# write code below

# Get the total number of items in the list
x = len(names)
# Get a random value from the list using the len above
random_choice = random.randint(0, x - 1)

lucky_person = names[random_choice]

print(f"{lucky_person} will pay the bill today!")


# Easier way below!!

#lucky_person = random.choice(names)
