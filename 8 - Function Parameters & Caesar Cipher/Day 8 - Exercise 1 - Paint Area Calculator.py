#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    number_of_cane = (height*width)/cover
    round_up_cans = math.ceil(number_of_cane)
    print(f"You'll need {round_up_cans} cans of paint.")


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = int(input("Enter your cover: "))
paint_calc(height=test_h, width=test_w, cover=coverage,)

