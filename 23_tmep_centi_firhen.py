temp = float(input("Enter Temperature: "))
degree = input("Enter in which degree you want to convert C or F: ")
centi= int(temp-32)*(5/9)
frie = int(temp*9/5)+(32)
if degree == "c" :
    print (centi)
elif degree == "f":
    print (frie)
