''' Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service. 

1. if employee is female, then she will work only in urban areas.
2. if employee is a male and age is in between 20 to 40 then he may work in anywhere
3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
4. And any other input of age should print "ERROR". '''

sex=input("Enter sex(M or F): ")
ms=input("Enter marital status(Y or N): ")
age=int(input("Enter age of Employee: "))

if sex=='F':
	if age>20 and age<=60:
		print("Employee will work only in urban areas")
	else:
		print("ERROR")
elif sex=='M':
	if age>20 and age<=40:
		print("Employee can work anywhere")
	elif age>40 and age<=60:
		print("Employee will work only in urban areas")
	else:
		print("ERROR")
	
