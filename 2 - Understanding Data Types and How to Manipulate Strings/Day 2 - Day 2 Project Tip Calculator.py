#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

Bill = float(input("Enter Your Bill Amount: $"))
tip = int(input("How much tip would you like to give in percentage? 10%, 12%, 15%:"))
people = int(input("How many people to split the bill?"))

tip_as_per = tip/100
total_tip_amount = Bill * tip_as_per
total_bill = Bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round (bill_per_person, 2)

print(f"Each Person pay: {final_amount}")