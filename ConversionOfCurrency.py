"""Challenge: Allow the user to choose from multiple currency pairs and implement appropriate error handling for invalid currency inputs.
==============================================
Input: Ask the user to enter an amount in one currency (e.g., USD).
Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
Output: Display the converted amount in the target currency."""

#Set currency exchange rates as of 4/22/2025
USD_To_INR = 85.23
EUR_To_INR = 97.97
Bitcoin_To_USD = 88,462.73
Dogecoin_To_USD = 0.16
GBP_To_USD = 1.34 # British Pound
CNY_To_USD = .14 # Chinese Yuan
USD_To_EUR = 0.88
USD_To_GBP = 0.78

# Display Available currency conversions

print("Please select from the available currency conversions below:")
print("1: USD_To_INR")
print("2: EUR_To_INR")
print("3: GBP_To_USD")
print("4: CNY_To_USD")
print("5: USD_To_EUR")
print("6: USD_To_GBP")

while True:   # loop until valid pair number is entered
    # Ask user for a choice
    try:
        choice = int(input("Enter the currency pair number (1-6): "))
        if choice in range(1, 7): # check if input is in between 1 and 6
            break  # exit loop if correct pair number entered(Successful)
        else:
            print("Invalid choice. Please select number between 1 and 6.")
    except ValueError:
        print("Invalid input. Please enter a numeric number between 1 and 6.")
amount_input = input("Enter the amount: ")
if amount_input.replace(".", "", 1).isdigit(): #check if float values are numeric or not
    amount = float(amount_input) # convert input value to float
else:
    amount = 0  # To prevent warning "Name 'amount' can be undefined"
    print("Error: Invalid amount. Please enter numeric value.")
if amount == 0:
    exit()
else:
# Perform conversion
    if choice == 1:
        converted = amount * USD_To_INR
        print(f"{amount:.2f} USD is equal to {converted:.2f} INR.")
    elif choice == 2:
        converted = amount * EUR_To_INR
        print(f"{amount:.2f} EUR is equal to {converted:.2f} INR.")
    elif choice == 3:
        converted = amount * GBP_To_USD
        print(f"{amount:.2f} GBP is equal to {converted:.2f} USD.")
    elif choice == 4:
        converted = amount * CNY_To_USD
        print(f"{amount:.2f} CNY is equal to {converted:.2f} USD.")
    elif choice == 5:
        converted = amount * USD_To_EUR
        print(f"{amount:.2f} USD is equal to {converted:.2f} EUR.")
    elif choice == 6:
        converted = amount * USD_To_GBP
        print(f"{amount:.2f} USD is equal to {converted:.2f} GBP.")
    else:
        print("Invalid currency choice! Please enter EUR or GBP.")













