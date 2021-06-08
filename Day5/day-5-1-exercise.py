# Get a list of student heights and print them in a list
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# Get the average height without using len() or sum()
# this can be done completely with for loops

# define some new variables to store height and number of students in
height = 0
student = 0
# for loop to add the heights
for heights in student_heights:
    height += heights
# for loop to get the number of items
for students in student_heights:
    student += 1

# equation to get the average
average = round(height // student)
# print the final result
print(f"The average height for students is: {average}")
