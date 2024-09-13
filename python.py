# Python3 program to add two numbers
num1 = 15
num2 = 12

# Adding two nos
sum = num1 + num2

# printing values
print("Sum of", num1, "and", num2 , "is", sum)


#prime numbers @Contributor-1
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_between(a, b):
    primes = []
    for num in range(a, b + 1):
        if is_prime(num):
            primes.append(num)
    return primes
