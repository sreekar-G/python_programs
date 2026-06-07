## Training linear regression with real-life dataset of housing prices in hyderabad with Turi

#import pandas as pd
#import turi as tc

#url = "https://raw.githubusercontent.com/luisguiserrano/manning/master/Chapter_03_Linear_Regression/Hyderabad.csv"
#data = pd.read_csv(url)
#data = pd.read_csv("Hyderabad.csv")
#$print(data.head())


#num_rows, num_cols = data.shape
#print("The dataset has ", num_rows, "rows, and ", num_cols, " columns")

# train the model
#data = tc.SFrame("Hyderabad.csv");
#model = tc.linear_regression.create(data, target="Price")

# Normal loop
#result = []
#for x in items:
#    if condition:
#        result.append(transform(x))
#
## Same thing — list comprehension
#result = [transform(x) for x in items if condition]

def square_number(num) :
	return num * num
	
def filter_numbers(numbers, is_even) : 
	result = []
	if is_even :
		result = [i for i in numbers if i%2 == 0 ]
	else :
		result = [i for i in numbers if i%2 != 0 ]
	return result

def display_results(task_name, result) :
	print(f"{task_name} → {result}")

def word_frequency_counter(sentence) :
        sentence_array = sentence.split(" ")
        output_array = {}
        for each_word in sentence_array :
                word = each_word.lower()
                value = output_array.get(word,0)
                output_array[each_word.lower()] =  value+1
        return output_array

def top_words_from_file(filename, N):
	content = None
	with open(filename, "r") as f:
		content = f.read()
	content = " ".join(content.split("\n"))
	word_frequency = word_frequency_counter(content)
	sorted_array = sorted(word_frequency, key=lambda x : word_frequency[x], reverse=True)
	#sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
	#print(sorted_words)
	return [(key,   word_frequency[key]) for key in sorted_array[:N]]

def display_topNwords_from_file(words_list) :
	for sequence, (word, frequency) in enumerate(words_list, start=1) :
		print(f"{sequence}. {word}   → {frequency} times")

if __name__ == "__main__" :
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	words   = ["hello", "world", "python", "ai", "code"]

	even_numbers = filter_numbers(numbers, True)
	display_results("Task 1", even_numbers)
	
	odd_numbers = filter_numbers(numbers, False)
	squared_odd_numbers = [square_number(i) for i in odd_numbers]
	display_results("Task 2", squared_odd_numbers)
	
	filtered_wordlist = [word.upper() for word in words if len(word) > 4]
	display_results("Task 3", filtered_wordlist)

	squared_natural_numbers = [(i, square_number(i)) for i in numbers]
	display_results("Task 4", squared_natural_numbers)

	topNwords_from_file = top_words_from_file("file_ops/sample.txt", 5)
	display_topNwords_from_file(topNwords_from_file)


#filter_numbers — can be one clean function 
#squared_odds = [i**2 for i in numbers if i % 2 != 0]

#square_number() — Python has built-in ** operator

# sorted() on dict — already know .items() is cleaner
# sorted_array = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

# New Thing — .split() vs .split(" ")
# Always use .split() for word splitting — handles tabs, newlines, multiple spaces! 
