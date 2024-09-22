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

#I am vipul bagde and this is my contribution

// C++ program to implement the approach

#include <bits/stdc++.h>
using namespace std;

// Function to check if both arrays are equal
bool checkArrays(int arr1[], int arr2[],
				int n, int m)
{
	// If lengths of array are not equal
	// means array are not equal
	if (n != m)
		return false;

	// Sort both arrays
	sort(arr1, arr1 + n);
	sort(arr2, arr2 + m);

	// Linearly compare elements
	for (int i = 0; i < n; i++)
		if (arr1[i] != arr2[i])
			return false;

	// If elements are same
	return true;
}

// Driver Code
int main()
{
	int arr1[] = { 1, 2, 3, 4, 5 };
	int arr2[] = { 5, 4, 3, 2, 1 };
	int N = sizeof(arr1) / sizeof(int);
	int M = sizeof(arr2) / sizeof(int);

	// Function call
	if (checkArrays(arr1, arr2, N, M))
		cout << "Equal";
	else
		cout << "Not Equal";
	return 0;
}

