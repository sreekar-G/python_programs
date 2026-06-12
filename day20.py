#NumPy Basics
import numpy as np

#numpy basics

if __name__ == "__main__" :
	
	#numpy_basics
	python_list = [1, 2, 3, 4, 5]
	numpy_array = np.array([1, 2, 3, 4, 5])

	print(f"python_list * 2 {python_list * 2}")
	print(f"numpy_array * 2 {numpy_array * 2}")


	### numpy basics
	import numpy as np

	scores = np.array([85, 92, 78, 90, 56, 88, 34, 72, 95, 61])
	
	#Task 1 → Print min, max, mean, median
	print(f"Task 1  :\n\tMin  : {np.min(scores)}\n\tMax : {np.max(scores)}\n\tMean : {np.mean(scores)}\n\tMedian : {np.median(scores)}")
	
	#Task 2 → Print all scores above 80
	print(f"Task 2 : {scores[scores > 80]}")

	#Task 3 → Normalize scores to 0-1 range
        #formula: (x - min) / (max - min)
	normalized_scores = (scores - 0) / (1 - 0)
	print(f"Task 3: {normalized_scores}")	

	#Task 4 → Add 5 bonus points to all scores
        #cap at 100 (no score above 100!)	
	bonus_scores = scores + 5
	print(f"Task 4: {np.clip(bonus_scores, 0, 100)}")

	#Task 5 → Count how many students passed (score >= 60)
	print(f"Task 5: {np.sum(scores >= 60)} students passed") 


	### numpy matrix

	marks = np.array([
	    [85, 92, 78],    # Alice
	    [45, 55, 60],    # Bob
	    [91, 88, 95],    # Carol
	    [70, 65, 72],    # David
	    [78, 82, 80],    # Eve
	])
	students = ["Alice", "Bob", "Carol", "David", "Eve"]
	subjects = ["Math", "Science", "English"]

	
	#Task 1 → Shape of matrix (rows, cols)
	print(f"Task 1: Shape → {marks.shape}")

	#Task 2 → Average score per student (row-wise)
	print("Task 2: Per student avg → ")
	for name, avg in zip(students, np.mean(marks, axis=1)):
		print(f"  {name} : {round(avg, 2)}")

	#Task 3 → Average score per subject (col-wise)
	print(f"Task 3: Per subject avg → ")
	for subject, score in zip(subjects, np.mean(marks, axis=0)) :
		print(f"  {subject} : {score}")

	#Task 4 → Highest scorer per subject
	print(f"Task 4: Top scorer per subject → ")
	for subject, score in zip(subjects, np.max(marks, axis=0)) :
		print(f"  {subject} : {score}")

	#Task 5 → Normalize entire matrix to 0-1
	print(f"Task 5: Normalized matrix → ")
	print(f"{(marks - marks.min()) / (marks.max() - marks.min()) }")


## ✅ Fix — use actual min and max of scores!
#normalized_scores = (scores - np.min(scores)) / (np.max(scores) - np.min(scores))

