weight1 = float(input("Enter weigth in kg: "))
height1 = float(input("Enter height in  meter: "))
pounts1 = float(input("Enter weight in pounds: "))
inches1 = float(input("Enter wight in inches: "))
heigh1cal = height1**2
inches1cal =  inches1**2
metricbmi = weight1/heigh1cal
impericalbmi = (pounts1/inches1cal)*(703)
print ("Your METRIC BMI weight is" , metricbmi)
print ("Your IMPERICAL BMI weight is" , impericalbmi)