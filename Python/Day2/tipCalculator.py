print("Welcome to the tip calculator!")
food_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
num_people = int(input("How many people to split the bill?"))

contribution_each = (food_bill + percentage_tip*food_bill/100) / num_people
print(f"Each person should pay: ${round(contribution_each, 2)}")
