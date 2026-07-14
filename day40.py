def find_missing_number_ap1(sequence,  num) :
	print(typeof(sequence))

	return sum(range(0, num)) - sum(sequence)

if __name__ == "__main__" :
	test_cases = [
	    ([0, 1, 3, 4, 5], 5),       # → 2 missing
	    ([1, 2, 3, 4, 5], 5),       # → 0 missing
	    ([0, 1, 2, 3, 4], 5),       # → 5 missing
	    ([3, 0, 1], 3),             # → 2 missing
	]
	
	for sequence, sum in test_cases :
		missed_num = find_missing_number_ap1(sequence, sum)
		print(f"{sequence}   → missing: {missed_num}")
