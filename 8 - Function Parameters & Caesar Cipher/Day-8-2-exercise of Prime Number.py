def prime_checker(number):
    is_prime = False
    for i in range(2, number):
        if number % i == 0:
            is_prime = True
    if is_prime:
        print("It's a prime Number.")
    else:
        print("It's not a prime Number.")
        
n = int(input("Check this number:"))
prime_checker(number=n)