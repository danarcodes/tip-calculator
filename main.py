#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")

totalbill = float(input("What was the total bill? \n$"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15\n"))
split_bill = int(input("How many people to split the bill? \n"))
tip_as_percent = percentage_tip / 100
total_tip_amount = tip_as_percent * totalbill
bill_tip = total_tip_amount + totalbill
bill_per_person = bill_tip / split_bill
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")