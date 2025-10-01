print("Welcome to the tip Calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15 "))
people = int(input("How many people to split the bill? "))
tip_percent = tip / 100
bill_tip = bill * tip_percent
final_bill = bill + bill_tip
each_people = final_bill / people
each_people = round(each_people, 2)
print(f"Each person should pay: ${each_people}")