"""Challenge: Ensure that the user enters only a single character and handle cases where the input is not a letter.
=====================================================
Input: Ask the user to enter a single character.
Processing: Determine whether the entered character is a vowel (a, e, i, o, u) or a consonant.
Output: Display whether the entered character is a vowel or a consonant."""

# Ask user to enter a character
char = input("Enter an alphabet (A-Z)(a-z): ")
# To check input is an alphabet
if char.isalpha():
    char = char.lower()         # Converting input in to lower case if given in upper case
    # Evaluating input is vowel or consonant
    if char in 'aeiou':
        print(f"{char} is a vowel")
    else:
        print(f"{char} is a consonant")

else:
    # Error handling if the input is numeric
    print("ERROR: Invalid Input: You entered a numeric value. Please enter a character.")









