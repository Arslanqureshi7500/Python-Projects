#Functions that allows for input
# def greet(something):
#     print(f"Hello Mr/Mrs. {something}")
#     print(f"What's going on your life Mr/Mrs. {something}?")
# 
# something = input("Please enter your name: ")
# greet(something)

#Functions with more than 1 input

def greet(name, location):
    print(f"Hello Mr/Mrs. {name}")
    print(f"Your location is. {location}?")

name = input("Please enter your name: ")
location = input("Please enter your location: ")
greet(name, location)
