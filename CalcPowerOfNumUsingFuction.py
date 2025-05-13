"""Challenge: Handle negative exponents efficiently.
====================================
Description: Develop a function named      power that takes two integers,
base and exponent, as input and returns base raised to the power of exponent."""

def power(b, e):
      return pow(b, e)  # Computes exponentiation(b^e)

while True:
      try:
            # Validate base input: Must be a number (integer or decimal)
            base_input = input("Enter Base value: ")
            if not base_input.lstrip("-").replace(".", "", 1).isdigit():  # Allows one decimal point
                  raise ValueError("Base must be a number.")
            base = int(base_input)  # Convert to float
            # **Check for negative base before asking for exponent**
            if base < 0:
                  print("Error: Base must be positive.")
                  continue  # Re-prompt user for input instead of proceeding

            # Validate exponent input: Must be a whole number (no decimals)
            expo_input = input("Enter Exponent value: ")
            if not expo_input.isdigit():  # Ensures only positive whole numbers
                  raise ValueError("Exponent must be a non-negative whole number.")
            expo = int(expo_input)  # Convert to integer
            # Compute and print result
            print(f"{base} raised to the power of {expo} is: {power(base, expo)}")

      except ValueError as err:
            print("Invalid Input:", err)


