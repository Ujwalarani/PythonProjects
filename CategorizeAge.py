"""Challenge: Implement error handling to ensure that the user enters a positive integer for the age.
==================================
Input: Prompt the user to enter their age.
Processing: Classify the age into different categories:
Under 18: Minor
18-65: Adult
Above 65: Senior citizen
Output: Display the category based on the entered age."""

# input age
try:
    age = float(input("Enter age: "))
    if age < 0:
        print("ERROR: Age can not be negative.")
    elif age < 18:
        print("Minor")
    elif 18 <= age <= 65:
        print("Adult")
    else:
        print("Senior Citizen")

except ValueError:
    print("ERROR: Invalid input. Please enter numeric value.")
