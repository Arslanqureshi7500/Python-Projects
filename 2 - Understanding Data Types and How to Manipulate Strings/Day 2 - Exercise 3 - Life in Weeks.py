# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


years = 90 - int(age)
days = round (years * 365)
week = round (years * 52)
month = round (years * 12)

print(f"You have {days} days, {week} weeks, and {month} months left.")