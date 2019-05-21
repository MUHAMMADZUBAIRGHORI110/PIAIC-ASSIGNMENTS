principle = float(input("Enter Principle Amount: "))
interest = float(input("Enter Interest rate "))
years = float(input("Enter Number of years"))
calc = principle*(1+(0.01*interest))**years
print (calc)