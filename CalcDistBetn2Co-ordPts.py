"""Challenge: Implement error handling to ensure that the user enters numeric values for the coordinates.
============================================
Input: Prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2).
Processing: Calculate the distance between the two points using the
distance formula: Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
Output: Display the calculated distance between the two points."""


# Evaluate input to be numeric values
try:
    # Input coordinate values for 2 points
    x1 = float(input("Enter coordinate x1: "))
    y1 = float(input("Enter coordinate y1: "))
    x2 = float(input("Enter coordinate x2: "))
    y2 = float(input("Enter coordinate y2: "))
    # Calculate Distance between given points
    x_squared = (x2 - x1) ** 2
    y_squared = (y2 - y1) ** 2
    distance = (x_squared + y_squared) ** 0.5
    print(f"Distance between two points = {distance :.2f} units")
except ValueError:
    print("ERROR: Enter numeric values")







