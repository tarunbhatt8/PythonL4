''' Q.3- Take the input age of 3 people and determine oldest and youngest among them. '''
age1=int(input("Enter age of person 1: "))
age2=int(input("Enter age of person 2: "))
age3=int(input("Enter age of person 3: "))

oldest,youngest=0,0

if age1>=age2 and age1>=age3:
	oldest=1
	if age2>=age3:
		youngest=3
        
	else:
		youngest=2
                

if age2>=age1 and age2>=age3:
	oldest=2
	if age1>=age3:
		youngest=3
                
	else:
		youngest=1
                

if age3>=age2 and age3>=age1:
	oldest=3
	if age2>=age1:
		youngest=1
                
	else:
		youngest=2
                

print("Oldest is Person{0} and Youngest is Person{1}".format(oldest,youngest))




	
