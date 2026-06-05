import numpy as np
from collections import defaultdict

#Root Square Mean Error
def rsme(labels, predictions) :
	n = len(labels)
	differences = np.subtract(labels, predictions)
	return np.sqrt(1.0/n * (np.dot(differences, differences)))


#You have a list of students with marks in multiple subjects. Write a function that:
#Calculates average score for each student
#Assigns a grade based on average (reuse Day 3 rules!)
#Prints a sorted report by average score descending

def avg_mark_with_grade (students_list) :
	avg_mark_with_grade_list = defaultdict(list)
	for each_student in students_list :
		student_name = each_student["name"]
		total_marks = sum(each_student["marks"])
		no_of_marks = len(each_student["marks"])
		avg_mark = total_marks / no_of_marks
		if avg_mark >= 90 :
                        student_grade = "A"
		elif avg_mark >= 75 :
			student_grade = "B"
		elif avg_mark >= 60 :
			student_grade = "C"
		elif avg_mark < 60 :
			student_grade = "F"
		avg_mark_with_grade_list[student_name] = {"avg_mark" : float(total_marks/ no_of_marks), "grade" : student_grade }
	return avg_mark_with_grade_list

def display_grade_list(grade_list) :
	sorted_grade_list = sorted(grade_list.items(), key=lambda x : x[1]["grade"])
	for each_student in sorted_grade_list :
		print(f"{each_student[0]}  → avg: {each_student[1]['avg_mark']} grade: {each_student[1]['grade']}")	


def palindrome_checker(words_list) :
	for each_word in words_list :
		original_word = each_word.lower().replace(" ","")
		reveresed_word = original_word[::-1]
		if original_word == reveresed_word :
			print(f"{each_word}  → ✅ Palindrome  ")
		else :	
			print(f"{each_word}  → ❌ Not a Palindrome ")
if __name__ == "__main__" :
	students = [
    		{"name": "Alice",  "marks": [85, 92, 78, 90]},
    		{"name": "Bob",    "marks": [45, 55, 60, 40]},
    		{"name": "Carol",  "marks": [91, 88, 95, 92]},
    		{"name": "David",  "marks": [70, 65, 72, 68]},
    		{"name": "Eve",    "marks": [78, 82, 80, 75]},
	]
	grade_list = avg_mark_with_grade(students)
	display_grade_list(grade_list)
	
	words = ["racecar", "hello", "madam", "python", "level", "A man a plan a canal Panama"]
	palindrome_checker(words)
	

#Bug 1 — Sorting by grade letter instead of avg_mark
#sort by avg_mark descending
#sorted(grade_list.items(), key=lambda x: x[1]["grade"]); sorted(grade_list.items(), key=lambda x: x[1]["avg_mark"], reverse=True)
#Bug 2 — Ranking number missing in print
#for rank, (name, details) in enumerate(sorted_grade_list, start=1):
#Notice : ❌ Unnecessary — you're not auto-initialising
# ✅ Plain dict is enough; result = {};result[student_name] = .. 
