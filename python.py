def menu():
    print("""
    Choose an operation:
    1. Add two numbers (Tarun's Contribution)
    2. Swap first and last elements in a list (Tathya's Contribution)
    3. Check prime numbers and generate odd primes (Ashish's Contribution)
    4. Sieve of Eratosthenes to find primes (Rigal's Contribution)
    5. Odd or Even check (Vipul's Contribution)
    6. Simple Guessing Game (Ayush Dubey's Contribution)
    7. Find Majority Element (Shourya's Contribution)
    8. Multiply two numbers (Shreyash's Contribution)
    9. Factorial of a number (Gokul's Contribution)
    10. Find square root of a number (Veeraj's Contribution)
    11. Exit
    """)

# Addition by Tarun
def tarun_add():
    num1 = 15
    num2 = 12
    sum = num1 + num2
    print("Sum of", num1, "and", num2, "is", sum)

# Swap first and last elements by Tathya
def tathya_swap():
    my_list = [1, 2, 3, 4, 5]
    my_list[0], my_list[-1] = my_list[-1], my_list[0]
    print("List after swapping first and last elements:", my_list)

# Check prime numbers and generate odd primes by Ashish
def ashish_prime():
    limit = 100
    odd_prime_numbers = generate_odd_primes(limit)
    print("Odd prime numbers up to", limit, "are:", odd_prime_numbers)

def generate_odd_primes(limit):
    odd_primes = []
    for num in range(3, limit + 1, 2):
        if is_prime(num):
            odd_primes.append(num)
    return odd_primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Sieve of Eratosthenes by Rigal
def rigal_sieve():
    n = 30
    prime_numbers = sieve_of_eratosthenes(n)
    print(f"Prime numbers up to {n}: {prime_numbers}")

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes

# Odd or Even by Vipul
def vipul_odd_even():
    n1 = 3
    if n1 % 2 == 0:
        print("This is Even number")
    else:
        print("This is Odd number")

# Simple Guessing Game by Ayush Dubey
def ayush_guessing_game():
    import random
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

# Find Majority Element by Shourya
def shourya_find_majority():
    arr = [1, 1, 1, 1, 2, 3, 4]
    n = len(arr)
    majority = findMajority(arr, n)
    print("The majority element is:", majority)

def findMajority(arr, n):
    candidate = -1
    votes = 0
    for i in range(n):
        if votes == 0:
            candidate = arr[i]
            votes = 1
        else:
            if arr[i] == candidate:
                votes += 1
            else:
                votes -= 1
    count = 0
    for i in range(n):
        if arr[i] == candidate:
            count += 1
    if count > n // 2:
        return candidate
    else:
        return -1

# Multiplication by Shreyash
def shreyash_multiply():
    number1 = 20
    number2 = 30
    multip = number1 * number2
    print("Product of", number1, "and", number2, "is", multip)

# Factorial by Gokul
def gokul_factorial():
    num = 7
    factorial = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial *= i
        print("The factorial of", num, "is", factorial)

# Square Root by Veeraj
def veeraj_square_root():
    num = 8
    num_sqrt = num ** 0.5
    print('The square root of %0.3f is %0.3f' % (num, num_sqrt))

# Main Driver Function
while True:
    menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        tarun_add()
    elif choice == 2:
        tathya_swap()
    elif choice == 3:
        ashish_prime()
    elif choice == 4:
        rigal_sieve()
    elif choice == 5:
        vipul_odd_even()  # Updated contribution
    elif choice == 6:
        ayush_guessing_game()
    elif choice == 7:
        shourya_find_majority()
    elif choice == 8:
        shreyash_multiply()
    elif choice == 9:
        gokul_factorial()
    elif choice == 10:
        veeraj_square_root()
    elif choice == 11:
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please choose a number between 1 and 11.")
