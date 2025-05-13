"""Challenge: Use nested loop structures to print the pattern efficiently and neatly.
Allow the user to specify the character used for the pattern.
=========================================
Description: Develop a program that prompts the user to enter the number of rows for a pattern and
then prints a pattern of asterisks (*) in the form of a right triangle."""

char = input("Enter the character for the pattern: ")
rows = int(input("Enter number of rows for a pattern: "))

for i in range(0, rows):            # Controls the number of rows
    for j in range(0, i+1):         # Controls the columns (stars printed per row)
        print(char, end= " ")       # Prints the character on the same line
    print()                         # Moves to the next row






