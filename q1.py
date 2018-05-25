#Q.1- Take an input year from user and decide whether it is a leap year or not.

year=int(input("Enter an year: "))
if year%4==0:
	print("{} is leap year".format(year))
else:
	print("{} is not a leap year".format(year))
