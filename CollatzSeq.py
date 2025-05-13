"""Challenge: Use a loop structure to generate the Collatz sequence until it reaches 1. Handle cases where the user enters a non-numeric input.
=================================
Description: Write a program that generates the Collatz sequence for a given positive integer entered by the user. The Collatz sequence is generated iteratively by repeatedly applying the following rules:
If the current number is even, divide it by 2.
If the current number is odd, multiply it by 3 and add 1."""

while True:
    n = input("Enter a number: ")           # Get user input
    # Check if input is a digit and a positive numeric value
    if n.isdigit() and int(n) > 0:          # Validate input
        num = int(n)                        # Convert to integer after validation
        print("Valid input: The number is a positive integer.")
        break                               # Exit loop on valid input
    else:
        print("Invalid input: The value cannot be negative, a decimal number, or contain non-numeric characters.")
        print("Please enter a positive integer.")
print("This is calculation for Collatz sequence!")
while num != 1:                             # Loop until reaching 1
    print(num, end="-->")                   # Print current number
    if num % 2 == 0:
        num = num // 2                      # If even, divide by 2(Integer Division)
    else:
        num = 3 * num + 1                   # If odd, apply 3n + 1 rule

print(num)                                  # Print the final number (1)