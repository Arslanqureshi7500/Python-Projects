#Write your code below this row 👇
#if we can take a with for loop than we use this program 👇
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)


# #if we can take a number from user than we use this program 👇
# user_as_int = input("Enter a digit: ")
# user = int(user_as_int)
# # for number in range(1, 101):
# if user%3==0 and user%5==0:
#     print("FizzBuzz")
# elif user%3==0:
#     print("Fizz")
# elif user%5==0:
#     print("Buzz") 
# else:
#     print(user)
