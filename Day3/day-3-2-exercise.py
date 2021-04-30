# get initial values to work with
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# calculations and result below
bmi = round(weight / (height ** 2))

# formulate the output in loops
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
