#Ref: https://stackoverflow.com/questions/22743860/python-fizzbuzz
#Note I changed the function name too!

def myFizzBuzzSol():

	for i in range(1,101):
		print {
			3: "FIzz",
			5: "Buzz",
			15: "FizzBuz"}.get(15*(not i%15)or 5*(not i%5) or 
3*(not							 i%3), 
'{}'.format(i))

myFizzBuzzSol() 

