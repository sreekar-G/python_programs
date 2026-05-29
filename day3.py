from collections import defaultdict
def topNprod_by_total_revenue( transactions, N) :
	sorted_transactions = sorted(transactions.items(), key=lambda x: x[1]["revenue"], reverse=True)
	return sorted_transactions[:N]
def merge_transactions(transactions) :
	merge_transactions = defaultdict(lambda : {"quantity" : 0, "revenue" : 0})
	for each_transaction in transactions :
		product = each_transaction.get("product")
		quantity = each_transaction.get("quantity")
		revenue = quantity * each_transaction.get("price")
		merge_transactions[product]["quantity"] += quantity
		merge_transactions[product]["revenue"] += revenue
	return merge_transactions

def display_transactions(transactions) :
	for rank, (product, details) in enumerate(transactions, start=1) :
		print(f"{rank}.  {product} revenue  → {details['revenue']}")
def word_frequency_counter(sentence) :
	sentence_array = sentence.split(" ")
	output_array = {}
	for each_word in sentence_array : 
		word = each_word.lower()
		value = output_array.get(word,0)
		output_array[each_word.lower()] =  value+1
	return output_array

def display_frequency(arr) :
	for each_word in arr.keys()  :
		times = "times" 
		if arr[each_word] == 1 :
			times = "time"
		print(f"{each_word}  → {arr[each_word]} {times}")

if __name__ == "__main__" :
	#sentence = "the cat sat on the mat the cat sat on a mat"
	#result = word_frequency_counter(sentence)
	#display_frequency(result)
	transactions = [
	    {"product": "apple", "quantity": 3, "price": 10},
	    {"product": "banana", "quantity": 5, "price": 5},
	    {"product": "apple", "quantity": 2, "price": 10},
	    {"product": "banana", "quantity": 1, "price": 5},
	    {"product": "cherry", "quantity": 4, "price": 20},
	    {"product": "mango", "quantity": 6, "price": 15},
	    {"product": "grape", "quantity": 2, "price": 25},
	]
	merge_result = merge_transactions(transactions)
	topN_result = topNprod_by_total_revenue(merge_result,3)
	display_transactions(topN_result)

#stage2 corrections 
#for word_frequency_counter
#Mistake | Fix
#dict.append() doesn't exist | Use dict[key] = valueget(key) 
#returns None | Use get(key, 0) for default value
#Result not captured | result = word_frequency_counter(sentence)
#display_frequency() called empty | Pass result as argument


#lessons learnt
#DICTONARIES vs DEFAULT_DICTIONARIES
#normal_dict crashes if key not found. (always check if key exist before you access)
#from collections import defaultdict.
#uses factory function to create missing values. so no check needed. 
#Missing key (you don't have worry about returns 0)
#counting pattern (you don't need to check and assign)
#code lines are reduced. 
#LAMBDA FUNCTIONS
#one-liner anonymous function - a function without name
#for sorting (based a small logic)
#you can use sorting multiple_keys, maps (to apply for every element), filter (for getting matched elements), 
#lambda args: expresssion; Anonymous; one line only; simple one-liner passed as argument. 


