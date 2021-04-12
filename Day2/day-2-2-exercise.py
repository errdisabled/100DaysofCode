# BMI calculator

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

calculation = int(weight) / float(height) ** 2

bmi = str(int(calculation))

print("Your BMI is " + bmi)
