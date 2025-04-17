"""Calculate Area Of a Rectangle
Input Length and Width"""

Length = float(input("Enter Length:"))
Width = float(input("Enter Width:"))
#Check for negative values
if Length < 0 or Width <0:
    print("Error: Please enter positive values for both Length and Width")
else:
    # calculate area and display
    Area = Length*Width
    print("Area of Rectangle =",Area)
