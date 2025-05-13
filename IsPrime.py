"""Challenge: Optimize the function to handle large input numbers efficiently.
=====================================================
Description: Develop a function called is_prime that takes a positive integer as input
and returns True if it is a prime number, and False otherwise"""
while True:
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2 or n == 3:  # Special case for 2 and 3 (smallest primes)
            return True
        if n % 2 == 0 or n % 3 == 0:  # Eliminates multiples of 2 and 3 early. checks remainder = 0
            return False
        # Check divisibility from 5 to sqrt(n), skipping multiples of 2 and 3
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:  # Check divisibility for i and i+2
                return False
            i += 6  # Skip even numbers
        return True

    while True:
        try:
            num = int(input("Enter a number: "))
            if num < 0:
                raise ValueError("Error: Please enter a positive number.")  # Raise an error for negative numbers
            print(f"{num} is prime: {is_prime(num)}")  # Call the is_prime function
            break  # Exit loop if input is valid
        except ValueError as e:
            print("Invalid Input:", e)  # Print error message and re-prompt input
