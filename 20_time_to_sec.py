days = int(input("Enter days:"))
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes:"))
seconds = int(input("Enter seconds:"))
perdayseconds= (days*86400)
perhourseconds = (hours*3600)
perminutessecond= (minutes*60)
second= perdayseconds+perhourseconds+perminutessecond+seconds
print (second)