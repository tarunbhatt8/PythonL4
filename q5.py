''' Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user. '''

quantity=int(input("Enter quantity of purchase: "))
cost=float(quantity*100)

print("Initial cost of {0} items = {1}".format(quantity,cost))

if cost>1000:
	print("Giving 10% discount")
	cost=cost*0.9
else:
	print("No discount given")

print("Total Cost={}".format(cost))


	
