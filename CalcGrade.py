"""Challenge: Implement error handling to ensure that the user enters valid marks (between 0 and 100) for each subject.
=================================================
Input: Ask the user to enter their marks for three subjects.
Processing: Calculate the average of the marks. Determine the grade based on the average:
90 and above: A
80-89: B
70-79: C
60-69: D
Below 60: F
Output: Display the calculated grade."""

# Ask user to input 3 subjects marks
try:
    math = float(input("Enter Math marks (0-100): "))
    science = float(input("Enter Science marks (0-100): "))
    english = float(input("Enter English marks (0-100): "))
    # Check if marks entered are with in the range of 0 and 100
    if (0 <= math <= 100) and (0 <= science <= 100) and (0 <= english <= 100):
        # Calculate average of 3 subjects
        avg = (math + science + english) / 3
        print(f"Average of {math:.2f}, {science:.2f} and {english:.2f} = {avg:.2f}")
        # Evaluate Grade based on Average
        if avg >= 90:
            print("Grade A")
        elif 80 <= avg <=89:
            print("Grade B")
        elif 70 <= avg <= 79:
            print("Grade C")
        elif 60 <= avg <= 69:
            print("Grade D")
        elif avg < 60:
            print("FAIL")
    else:
        print("ERROR: Invalid input. Please enter marks in the range of 0 and 100.")
except ValueError:
    print("ERROR: Invalid Input. Please enter a numeric value (0 - 100).")
