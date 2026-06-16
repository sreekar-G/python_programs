#Both have same mean = 50!

#But clearly Player B is inconsistent and Player A is reliable.
#Mean alone can't tell us this — we need Standard Deviation!

#Standard Deviation measures how spread out values are from the mean.
#step:1 - find the mean. 
#step:2 - Find deviation of each value from mean
#step:3 - square each deviation
#step:4 - find mean of squared deviations (called variance)
#step:5 - squared root of variance = standard deviation. 

#mean     = np.mean(player_a)
#variance = np.mean((player_a - mean) ** 2)
#std      = np.sqrt(variance)
#std = np.std(player_a)   # does all steps internally!

import numpy as np 


def balanced_parentheses(inputs) :
	result = {}
	for each_input in inputs :
		stack = []
		for each_bracket in each_input :
			#if each_bracket == "(" or each_bracket == "[" :
			if each_bracket in "({[" :
				stack.append(each_bracket) 
			elif each_bracket == ")" :
				#if stack[len(stack) -1] == "(" :
				if stack and stack[-1] == "(" :
					stack.pop()	
			elif each_bracket == "]" :
				#if stack[len(stack) -1] == "[" :
				if stack and stack[-1] == "[" :
					stack.pop()
			elif each_bracket == "}" :
				if stack and stack[-1] == "{" :
					stack.pop()
		if len(stack) == 0 :
			result[each_input] = "✅ Balanced"
		else :
			result[each_input] = "❌ Not Balanced"
	return result	

if __name__ == "__main__" :
	sales_data = np.array([
    		[120, 135, 128, 142],   # Rep A
		[80,  190, 75,  195],   # Rep B
		[150, 148, 152, 150],   # Rep C
		[100, 110, 95,  115],   # Rep D
	])
	reps = ["Rep A", "Rep B", "Rep C", "Rep D"]


	print("Task 1: Mean sales →")
	for each_rep, sales_average in zip(reps, np.mean(sales_data, axis=1)) :
		print(f"  {each_rep} : {sales_average}")


	print("Task 2: Std deviation →")
	stds = np.std(sales_data, axis=1)
	for each_rep, sales_std in zip(reps, stds) :
		print(f"  {each_rep} : {sales_std}")
	print(f"  Most consistent → {reps[np.argmin(stds)]}")

	print("Task 3: High inconsistency (std > 30) →")
	argmax_index = np.argmax(stds)

	masks = stds > 30
	reps_array = np.array(reps)
	for rep, std in zip(reps_array[masks], stds[masks]) :
		print(f"{rep} : std = {std}")
	#print(f"{reps[argmax_index]} : std = {stds[argmax_index]}")

	print("Task 4: Unusual quarters →")
	for each_rep, sales_data in zip(reps, sales_data) :
		mean = np.mean(sales_data)
		std = np.std(sales_data)
		print(f" {each_rep} : {sales_data[np.abs(sales_data - mean) > std]}")

	inputs = ["(())", "()[]{}", "(]", "([)]", "{[]}",  "(((" ]
	outputs = balanced_parentheses(inputs)

	for input, output in outputs.items() :
		print(f"{input}    → {output}")


# Bug1 : ❌ Your way — only finds the single maximum
#argmax_index = np.argmax(stds)
#print(f"{reps[argmax_index]} : std = {stds[argmax_index]}")
# ✅ Fix — filter all reps where std > 30

#Bug 2 — Balanced parentheses missing { and }

#Bug 3 — Stack crash when empty!
