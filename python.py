# Python3 program to add two numbers
num1 = 15
num2 = 12

# Adding two nos
sum = num1 + num2

# printing values
print("Sum of", num1, "and", num2 , "is", sum)

#<<<<<<< collabRigal


#Collaborator - Rigal 21BEC037
#Multiply
number1 = 20
number2 = 30

multip = number1 * number2

#print
print("Product of ", number1, "and ", number2, "is", multip)

#end
=======
# Initialize a list Done By Tathya
my_list = [1, 2, 3, 4, 5]

# Interchange first and last elements  Done By Tathya
my_list[0], my_list[-1] = my_list[-1], my_list[0]

# Print the modified list  Done By Tathya
print("List after swapping first and last elements:", my_list)
#<<<<<<< ashishbranch
# this is me ashish 

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_odd_primes(limit):
    """Generate a list of odd prime numbers up to the specified limit."""
    odd_primes = []
    for num in range(3, limit + 1, 2):
        if is_prime(num):
            odd_primes.append(num)
    return odd_primes

# Example usage:
limit = 100  # You can adjust this limit as needed
odd_prime_numbers = generate_odd_primes(limit)
print("Odd prime numbers up to", limit, "are:", odd_prime_numbers)




# 21BEC037 - Rigal - Code to find prime numbers in a given range (SIEVE OF ERATOSTHENES)
def sieve_of_eratosthenes(n):
    # Create a boolean array "is_prime[0..n]" and initialize
    # all entries as true. A value in is_prime[i] will finally be false if i is Not a prime, else true.
    is_prime = [True] * (n + 1)
    p = 2  # Start with the first prime number

    while (p * p <= n):
        # If is_prime[p] is true, then it is a prime
        if is_prime[p]:
            # Updating all multiples of p to not prime
            for i in range(p*p, n+1, p):
                is_prime[i] = False
        p+=1

    # Collecting all prime numbers
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes

# Example usage
if __name__ == "__main__":
    n = 30  # Find all primes up to 30
    prime_numbers = sieve_of_eratosthenes(n)
    print(f"Prime numbers up to {n}: {prime_numbers}")




# Odd and Even python program Done by Ayush Dubey
n1 = 3
if n1 % 2==0:
    print("This is Even number")
else:
    print("This is Odd number")
#<<<<<<< dubey



# Python program for a simple guessing game by Ayush Dubey
import random

def guessing_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    guess = None

    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

guessing_game()
#=======
#>>>>>>> main
#>>>>>>> main
#>>>>>>> main

#I am Shreyash

#I am Shourya prakash
# Python implementation for the above approach

# Function to find majority element
def findMajority(arr, n):
    candidate = -1
    votes = 0
    
    # Finding majority candidate
    for i in range (n):
        if (votes == 0):
            candidate = arr[i]
            votes = 1
        else:
            if (arr[i] == candidate):
                votes += 1
            else:
                votes -= 1
    count = 0
    
    # Checking if majority candidate occurs more than n/2
    # times
    for i in range (n):
        if (arr[i] == candidate):
            count += 1
            
    if (count > n // 2):
        return candidate
    else:
        return -1

# Driver Code 

arr = [ 1, 1, 1, 1, 2, 3, 4 ]
n = len(arr)
majority = findMajority(arr, n)
print(" The majority element is :" ,majority)
    
    
