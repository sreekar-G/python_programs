import numpy as np


if __name__ == "__main__" :
	#print(np.random.seed(42))
	
	sales = np.array([120, 135, 98, 142, 167, 155,
                  189, 145, 132, 178, 165, 190])
	
	months = np.array(["Jan","Feb","Mar","Apr","May","Jun",
          "Jul","Aug","Sep","Oct","Nov","Dec"])

	sales_average = np.mean(sales)
	print(f"Task 1: Average Sales {sales_average}")
	
	print("Task 2: Above average months →")
	mask = sales > sales_average 

	filtered_sales = sales[mask]
	filtered_months = months[mask]
	
	for month, sale in zip(filtered_months, filtered_sales) :
		print(f"	{month} : {sale}")

	print("Task 3: →")
	first_half_avg = np.mean(sales[:6])
	second_half_avg = np.mean(sales[6:])
	print(f"	First half avg  → {first_half_avg}")
	print(f"	Second half avg  → {second_half_avg}")	
	if first_half_avg > second_half_avg :
		print("		First half was better!")
	elif first_half_avg < second_half_avg :
		print("		Second half was better!")
	else :
		print("Both halves did the same")

	print("Task 4: Difference from mean →")	
	std_deviation = sales - sales_average
	for month, std_devi in zip(months, std_deviation) :
		print(f"	{month} : {round(std_devi, 2)}")
