"""Challenge: Provide feedback to the user based on their BMI category
(e.g., underweight, normal weight, overweight, obese).
===============================
Input: Prompt the user to enter their weight in kilograms and height in meters.
Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
Output: Display the calculated BMI."""
while True:
    print("=======================================")
    print("Want to know your BMI, Let's do it!")
    print("A: Weight in kilos and Height in Meters")
    print("B: Weight in Pounds and Height in Feet/Inches")
    print("Choose in what units you want to enter values")

    # Ask user to enter their choice of units

    option = input("Enter the choice (A or B): ")
    option = option.upper() # convert to uppercase if user enters lower case option

    # Logic to convert units
    if option == "A":
        # Input values in Kilos and Meters
        Weight = float(input("Enter weight in kilos: "))
        Height = float(input("Enter height in meters: "))
    elif option == "B":
        # Input values in Pounds and Feet
        weight = float(input("Enter weight in pounds: "))
        height_feet = float(input("Enter height in feet: "))
        height_inches = float(input("Enter height in inches: "))

        # Convert pounds to kilos and feet/inches to meters
        Weight = weight / 2.2046
        Height = (height_feet * 0.3048) + (height_inches * 0.0254 )
    else:
        print("ERROR: Invalid option. Please enter A or B")
        exit()
    # Calculate BMI
    BMI = Weight / (Height ** 2)
    print(f"Your BMI is {BMI:.2f}")
    # Categorize based on BMI
    if BMI < 18.5:
        print("You are Underweight.")
    elif BMI < 24.9:
        print("You are Normal weight.")
    elif BMI < 29.9:
        print("You are Overweight.")
    else:
        print("you are Obese.")










