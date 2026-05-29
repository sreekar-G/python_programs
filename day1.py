#input - transactions = [
#    {"product": "apple", "quantity": 3, "price": 10},
#    {"product": "banana", "quantity": 5, "price": 5},
#    {"product": "apple", "quantity": 2, "price": 10},
#    {"product": "banana", "quantity": 1, "price": 5},
#    {"product": "cherry", "quantity": 4, "price": 20},
#]
#output - apple   → total quantity: 5,  total revenue: 50
#banana  → total quantity: 6,  total revenue: 30
#cherry  → total quantity: 4,  total revenue: 80

def beautify_transactions(transactions) :
	merge_transactions = {}
	for each_transaction in transactions :
		product = each_transaction.get("product")
		existing_product = merge_transactions.get(product)
		quantity = each_transaction.get("quantity")	
		revenue = each_transaction.get("quantity") * each_transaction.get("price")
		if( existing_product == None) :
			merge_transactions[product] = [quantity,revenue]
		else :
			existing_revenue = existing_product[1]
			existing_quantity = existing_product[0]
			merge_transactions[product] =[existing_quantity+quantity,existing_revenue+revenue]

	for each_product in merge_transactions :
		details = merge_transactions[each_product]
		print(each_product+"   → total quantity: "+str(details[0])+",  total revenue: "+str(details[1]))
if __name__ == "__main__" : 
	transactions = [
	    {"product": "apple", "quantity": 3, "price": 10},
	    {"product": "banana", "quantity": 5, "price": 5},
	    {"product": "apple", "quantity": 2, "price": 10},
	    {"product": "banana", "quantity": 1, "price": 5},
	    {"product": "cherry", "quantity": 4, "price": 20},]
	beautify_transactions(transactions)
# stage2 corrections
# == None → not in
# String concat → f-strings
# Plain list → named dict {"quantity": 0, "revenue": 0}

# stage3 correction
# Optimised with defaultdict
# Removed if/else entirely
# Auto-initialises missing keys

# stage4 correction
# Split into aggregate() + display()
# Separation of concerns
# Two loops is correct & intentional
