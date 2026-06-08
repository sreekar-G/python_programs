import math
import numpy as np

def screentime_prediction(desktop, mobile, young, adult) :
	predicted_time = 0.8 * desktop + 0.5 * mobile + 0.5 * young + 0.2 * adult + 1.5
	return predicted_time

def rsme(labels, predictions) :
        n = len(labels)
        differences = np.subtract(labels, predictions)
        return np.sqrt(1.0/n * (np.dot(differences, differences)))

def mean_absolute_error(labels, predictions) :
	n = len(labels)
	absolute_differences = np.absolute(np.subtract(labels, predictions))
	return (1.0/n * (np.sum(absolute_differences)))

def model(sizes_of_house) :
	predicted_prices = [2* each_size + 50 for each_size in sizes_of_house]
	return np.array(predicted_prices)

def calculator(opr, operand1, operand2) :
	try : 
		if opr == "divide":
			try :
				return operand1 / operand2 
			except ZeroDivisionError:
				return "❌ Error: Cannot divide by zero"
		elif opr == "sqrt" :
			try :
				return math.sqrt(operand1)
			except ValueError:
				return "❌ Error: Cannot sqrt a negative number"
		elif opr ==  "power" :
			try :
				return operand1 ** operand2
			except ValueError:
                                return "❌ Error: Cannot do power of this number"
		elif opr == "log" :
			try :
				return math.log(operand1)
			except ValueError:
				return "❌ Error: Cannot log a negative number"
	except TypeError:
		return "Error: Invalid input type"

#Attributes:
#  - owner name
#  - balance (default 0)
#
#Methods:
#  - deposit(amount)     → add money
#  - withdraw(amount)    → remove money (can't go below 0!)
#  - get_balance()       → return current balance
#  - __str__()           → string representation
	 	
class BankAccount:
	
	def __init__(self, owner, balance=0):
		self.owner = owner
		self.balance = balance
	
	def deposit(self, amount):
		if amount > 0 :
			self.balance += amount
			print(f"Deposited {amount} → {self.get_balance()}")
		else :
			print("only positive numbers for deposit!")

	def withdraw(self, amount) :
		if amount > 0 :
			if self.balance > amount :
				self.balance -= amount
				print(f"Withdrew {amount} → {self.get_balance()}")
			else :
				print(f"❌ Insufficient funds! Balance: {self.get_balance()}")
	
	def get_balance(self) :
		return self.balance
		
	def __str__(self) :
		return f"BankAccount[{self.owner}] → {self.get_balance()}"

if __name__ == "__main__" :
	#Exercise - 3.1
	predicted_time = screentime_prediction(1, 0, 0, 1)
	print(f"If a user is 30 years old and on a desktop; predicted_time would be {predicted_time}")
	predicted_time = screentime_prediction(0, 1, 0, 1)
	print(f"If a user is 45-year-old and on a mobile; predicted_time would be {predicted_time}")

	#Exercise - 3.3
	labels = np.array([200, 475, 400, 520, 735])
	features = np.array([100, 200, 200, 250, 325])	
	
	model_predictions = model(features)
	print(f"a. Model predictions : {model_predictions}")
	print(f"b. Mean Absolute Error : {mean_absolute_error(labels, model_predictions)}")
	print(f"c. Root Mean Square Error : {rsme(labels, model_predictions)}")

	calculations = [
	    ("divide", 10, 2),
	    ("divide", 10, 0),      # division by zero!
	    ("sqrt",   25, None),
	    ("sqrt",  -16, None),   # negative square root!
	    ("power",  2, 10),
	    ("log",   100, None),
	    ("log",    -5, None),   # log of negative!
	    ("divide", "ten", 2),   # invalid type!
	]

	for operation, operand1, operand2 in calculations : 
		print(f"{operation}({operand1}, {operand2})   → {calculator(operation, operand1, operand2)}") 

	account = BankAccount("Sreekar", 1000)
	account.deposit(500)
	account.withdraw(200)
	account.withdraw(2000)   # should fail gracefully!
	print(account)


# One Minor Issue — > should be >=; bug : if self.balance > amount:; if self.balance >= amount:

#class BankAccount:          # blueprint / template
#    def __init__(self):     # constructor — runs when object created
#        self.balance        # instance variable — belongs to each object
#
#account = BankAccount()     # object — instance of the class
#account.deposit(500)        # calling a method on the object
#print(account)              # triggers __str__ automatically


#The nested try/except inside each elif — flattening it makes it cleaner:
#Less nesting = more readable! 
## Predictable → check first
#if operand1 < 0:
#    return "❌ cannot sqrt negative"
#
## Unpredictable → catch it
#except TypeError:
#    return "❌ invalid type"
