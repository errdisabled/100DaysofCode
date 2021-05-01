print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

total_name = lower_name1 + lower_name2

t = total_name.count("t")
r = total_name.count("r")
u = total_name.count("u")
e = total_name.count("e")

true = t + r + u + e

l = total_name.count("l")
o = total_name.count("o")
v = total_name.count("v")
e = total_name.count("e")

love = l + o + v + e

score = int(str(true) + str(love))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
