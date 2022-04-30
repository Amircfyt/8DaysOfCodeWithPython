# Project 2 - Tip Calculater

# If the bill was $150.00, split between 5 people, with 12% tip. 
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
bill   = float(input("What was the total bill? $"))
tip    = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

payment = (bill / people) * (1 + (tip/100))
payment = "{:.2f}".format(payment)
print(f"Each person should pay: ${payment}")

