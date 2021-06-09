# Get a list of scores (provided code)
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# Write your code below
# Get the highest value without using max()

# Set the solution variable
highest_score = 0
# Create a loop that compares each score as it iterates over the list
for score in student_scores:
    if score > highest_score:
        highest_score = score

# print out the highest score
print(f"The highest score in the class is: {highest_score}")
