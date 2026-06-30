#Valid Palindrome with Two Pointers

def check_palindrome_diff_approach(sentence) :
	sentence = sentence.lower().strip().replace(" ", "")

	sentence_len = len(sentence)
	mid_range = int(sentence_len / 2)
	
	#flag = False
	for each_index in range(mid_range) :
	#	flag = True if sentence[each_index] == sentence[(sentence_len-1) - each_index] else False 		
	#	if not flag :
	#		return "❌ Not Palindrome!"

		if sentence[each_index] != sentence[(sentence_len-1) - each_index]:
    			return "❌ Not Palindrome!"

	return "✅ Palindrome"

if __name__ == "__main__" :
	sentences = [
    		"A man a plan a canal Panama",
		"race a car",
		"Was it a car or a cat I saw",
		"hello",
		"No lemon no melon"
	]
	for each_sentence in sentences :
		print(f"{each_sentence}  → {check_palindrome_diff_approach(each_sentence)}")	 
