# Tip calculator for when you go out
print("Welcome to the tip calculator!")

# Ask for the bill total
bill = float(input("What was the total bill? $"))

# Determine the tip percentage
tip_percent = int(input(
    "What percentage tip would you like to give? 10, 12, or 15? "))

# Calculate bill with tip
bill_with_tip = tip_percent / 100 * bill + bill

# How many people are splitting the bill?
total_people = int(input("How many people are splitting the bill? "))

# Final total
final_total = "{:.2f}".format(bill_with_tip / total_people)

# Print out the final
print(f"Each person should pay: ${final_total}")
