
class Student:
	def __init__(self, name, grade_list) :
		self.name = name
		self.grade_list = grade_list
		self.grade = ""
		self.average = 0.00
	
	def __str__(self) :
		return f"{self.name}  → avg: {self.average}  grade: {self.grade}"

	def avg_mark_with_grade (self) :
		grade_values = self.grade_list
		avg_mark = sum(grade_values) / len(grade_values)
		if avg_mark >= 90 :
			student_grade = "A"
		elif avg_mark >= 75 :
			student_grade = "B"
		elif avg_mark >= 60 :
			student_grade = "C"
		elif avg_mark < 60 :
			student_grade = "F"
		self.average = round(avg_mark, 2)
		self.grade = student_grade

def read_csv_file(input_file) :
	with open(input_file, "r") as f:
	    lines = f.readlines()
	    header = lines[0]        # skip first line!
	    data = lines[1:]
	return data

def process_avg_mark_with_grade(data):
	student_list = []
	for line_index, each_line in enumerate(data) :
		each_line = each_line.split()
		student_name = ""
		student_grade_list = []
		for word_index, word in enumerate(each_line) : 
			each_word = word[:-1] if word[-1:] == "," else word
			if word_index == 0 :
				student_name = each_word
			else :
				student_grade_list.append(float(each_word))
		student = Student(student_name, student_grade_list)
		student.avg_mark_with_grade()
		student_list.append(student)
	return student_list

def write_text_file(content, output_file) :
	content = "=== Student Report ===\n" + content
	with open(output_file, "w") as f:
    		f.write(content)

def display(student_grade_list) :
	sorted_list = sorted(student_grade_list, key= lambda x :  x.average, reverse=True)
	content = ""
	for index, each_student in enumerate(sorted_list, start=1) :
		display_content = f"{index}. {each_student}"
		print(display_content)
		content += (display_content+"\n")
	return content

if __name__ == "__main__" :
	input_file = "./file_ops/students.csv"
	output_file = "./file_ops/report.txt"
	csv_output = read_csv_file(input_file)
	result = process_avg_mark_with_grade(csv_output)
	file_content = display(result)
	write_text_file(file_content, output_file)

#bug:1 ~each_word = word[:-1] if word[-1:] == "," else word
#each_word = word.strip(",").strip()

#bug:2 ~"each_line.split() Alice, 85, 92" splits into ["Alice,", "85,", "92"]
each_line.strip().split(",")

#bug:3 ~manual_looping
#for word_index, word in enumerate(each_line):
#    each_word = word[:-1] if word[-1:] == "," else word
#    if word_index == 0:
#        student_name = each_word
#    else:
#        student_grade_list.append(float(each_word))

#parts = [p.strip() for p in each_line.strip().split(",")]
#grade_list = [float(p) for p in parts[1:]]
