#ML model sees size as 500x more important
#just because of its scale — completely wrong!
#Solution → bring everything to the same scale!

import numpy as np

def Min_Max_Normalization(array) :
#	  value - min
#X_norm = ───────────
#          max - min
	min_max = (array - np.min(array)) / (np.max(array) - np.min(array))
	return min_max

def ZScore(array) :
#         value - mean
#Z_score = ────────────
#               std
	zscore = (array - np.mean(array)) / np.std(array)
	return zscore

def verify_mean_std(array) :
	mean_ok = np.round(np.abs(np.mean(array)), 1) == 0.0
	std_ok = np.round(np.std(array), 1) == 1.0
	return "✅" if mean_ok and std_ok else "❌"
	#if round(np.abs(np.mean(array)), 2) == 0.0 and np.std(array) == 1.0:
	#	return "✅"
	#else :
	#	return "❌"

def brute_force_approach(numbers, target) :
	indices = []
	for i_index, i  in enumerate(numbers) :
		for j_index, j in enumerate(numbers) : 
			if (i_index != j_index and i + j == target) :
				indices = [i_index, j_index]
				break
		if len(indices) != 0 :
			break
	return indices
  
def hash_map_approach(numbers, target) :
	seen = {}
	for index, each_number in enumerate(numbers) :
		complement = target - each_number
		if complement in seen :
			return [seen[complement], index]	
		seen[each_number] = index
	return []

if __name__ == "__main__" :

	# Student exam data — different scales!
	students = ["Alice", "Bob", "Carol", "David", "Eve"]

	math_scores    = np.array([45, 78, 92, 60, 85])   # 0-100
	attendance_pct = np.array([60, 85, 95, 70, 80])   # 0-100
	study_hours    = np.array([2,  5,  8,  3,  6])    # 0-10
	
	print("Task 1: Min-Max Normalized →")
	#print(f"	math_scores    : {Min_Max_Normalization(math_scores)}")
	#print(f"	attendance_pct : {Min_Max_Normalization(attendance_pct)}")
	#print(f"	study_hours    : {Min_Max_Normalization(study_hours)}")
	print(f"       math_scores    : {np.round(Min_Max_Normalization(math_scores), 3)}")
	print(f"       attendance_pct : {np.round(Min_Max_Normalization(attendance_pct), 3)}")
	print(f"       study_hours    : {np.round(Min_Max_Normalization(study_hours), 3)}")
	
	print("Task 2: Z-Score Normalized →")
	#zscore_math_scores = ZScore(math_scores)
	#print(f"	math_scores    : {zscore_math_scores}")
	#print(f"	mean ≈ {round(np.abs(np.mean(zscore_math_scores)), 2)}  std ≈ {np.std(zscore_math_scores)} {verify_mean_std(zscore_math_scores)}")
	#zscore_attendance_pct = ZScore(attendance_pct)
	#zscore_study_hours = ZScore(study_hours)

	features = {
		"math_scores" : ZScore(math_scores),
		"attendance_pct" : ZScore(attendance_pct),
		"study_hours" : ZScore(study_hours)
	}
	
	for name, zs in features.items():
		print(f"  {name} : {np.round(zs, 2)}")
		print(f"  mean ≈ {round(np.abs(np.mean(zs)), 1)}  std ≈ {round(np.std(zs), 1)}  {verify_mean_std(zs)}")
	

	print("Task 3: Combined matrix (5x3) →")
	#row_sums = np.column_stack([zscore_math_scores, zscore_attendance_pct, zscore_study_hours])
	#print(row_sums)
	zscore_math       = ZScore(math_scores)
	zscore_attendance = ZScore(attendance_pct)
	zscore_hours      = ZScore(study_hours)
	matrix = np.column_stack([zscore_math, zscore_attendance, zscore_hours])
	print(np.round(matrix, 3))

	row_sums = np.sum(matrix, axis=1)
	best_index = np.argmax(row_sums)	
	print(f"Task 4: Highest combined score → {students[best_index]}")


	inputs = [
	    ([2, 7, 11, 15], 9),    # → [0, 1]  (2+7=9)
	    ([3, 2, 4],      6),    # → [1, 2]  (2+4=6)
	    ([3, 3],         6),    # → [0, 1]  (3+3=6)
	    ([1, 5, 3, 7],   8),    # → [1, 3]  (5+7=8) or [2,3]? no! 3+7=10
	]
	
	print("Brute Force Approach")
	for each_arr, each_target in inputs :
		print(f"{each_arr}      target={each_target}  → indices {brute_force_approach(each_arr, each_target)}")
		        
	print("Hash Map Approach")
	for each_arr, each_target in inputs :
		print(f"{each_arr}      target={each_target}  → indices {hash_map_approach(each_arr, each_target)}")	
