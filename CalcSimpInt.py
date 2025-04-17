#Calculate Simple Interest
#Give Principal Amount(Principal), Interest Rate(Rate) and Time Period(Time)
try:
    Principal = float(input("Enter Principal Amount(PA): "))
    Rate = float(input("Enter Interest Rate in percentage(IR): "))
    Time = float(input("Enter Time Period in years(TP): "))
    Simple_Interest = (Principal*Rate*Time)/100
    print("Simple Interest is {:.2f}".format(Simple_Interest))
except ValueError:
    print("Error:Please enter Numeric values")
