#inputs 
#students = [
#    {"name": "Alice",   "score": 85},
#    {"name": "Bob",     "score": 42},
#    {"name": "Carol",   "score": 91},
#    {"name": "David",   "score": 55},
#    {"name": "Eve",     "score": 78},
#    {"name": "Frank",   "score": 38},
#    {"name": "Grace",   "score": 95},
#    {"name": "Hank",    "score": 60},
#], 
#Grade rules = 90 - 100  → A
#	75 - 89   → B
#	60 - 74   → C
#	below 60  → F
#outputs
#A → Grace, Carol
#B → Alice, Eve
#C → Hank
#F → Bob, David, Frank
from collections import defaultdict

def group_by_grade(students) :
	output_grades = defaultdict(list)
	for each_student in students :
		student_score = each_student.get("score");
		if (student_score >= 90) :
			student_grade = "A"
		elif (student_score  >= 75) :
			student_grade = "B"
		elif (student_score >= 60) :
			student_grade = "C"
		elif (student_score < 60) :
			student_grade = "F"
		output_grades[student_grade].append(each_student.get("name"))
	return output_grades

def display_grades (grades_dict) :
	sorted_grades = sorted(grades_dict.items(), key=lambda x : x[0])
	for each_grade, students in sorted_grades : 
		print(f"{each_grade}  → {', '.join(students)}")

if __name__ == "__main__" :
	students = [
	    {"name": "Alice",   "score": 85},
	    {"name": "Bob",     "score": 42},
	    {"name": "Carol",   "score": 91},
	    {"name": "David",   "score": 55},
	    {"name": "Eve",     "score": 78},
	    {"name": "Frank",   "score": 38},
	    {"name": "Grace",   "score": 95},
	    {"name": "Hank",    "score": 60},
	]
	output_grades = group_by_grade(students)
	display_grades(output_grades)



# Bug1 : Wrong — match/case doesn't support conditions like this
# match student_score:
#    case >= 90 and <= 100:
# Fix — use if/elif instead

# Bug 2 : defaultdict(lambda: []) is correct but can be simpler
#  Simpler — list is already a factory function
#  defaultdict(list)

# Bug 3 : .get() on defaultdict defeats the purpose; output_grades.get(student_grade)
# use square brackets directly output_grades[student_grade].append(each_student.get("name"))

# Bug 4 : enumerate wrong for dict, use .items(); for each_grade, students in enumerate(grades_dict):
# for each_grade, students in grades_dict.items():

# Bug 5 : printf and f-string syntax wrong; printf("{each_grade}  → str(students)")
# print(f"{each_grade}  → {', '.join(students)}")

# Bug 6 : if __main__ condition flipped; if __main__ = "__name__":
# if __main__ = "__name__":

