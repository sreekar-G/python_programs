### doing the linear regression with random values and square trick ###

import random ## to generate random values for slope (price per room) and y-intercept (base price of house0

import numpy as np

############### from yesterday's implementation of square trick over here ###

#m' = predicted price per room
#r = no.of rooms
#b' = base price of house
#p^ = predicted price per room
#               
#for rotating etta * no.ofrooms * (actual_price - predicted price)
#for translating etta * (actual_price - predicted price)
def square_trick(base_price, no_of_rooms, price_per_room, price, learning_rate) :
        predicted_price = base_price + no_of_rooms * price_per_room
        base_price = learning_rate * (price - predicted_price)
        price_per_room = learning_rate * no_of_rooms * (price - predicted_price)
        return base_price, price_per_room

#############################################################################


def linear_regression(features, labels, learning_rate=0.1, epochs=1000) :
	price_per_room = random.random() # generate the random value for slope 
	base_price = random.random()	# generate the random value for y-intercept
	for epoch in range(epochs):	# repeat it for so many times (each_iteration calling as epoch0
		i = random.randint(0, len(features) - 1)
		no_of_rooms = features[i]
		price = labels[i]
		price_per_room, base_price = square_trick(base_price, 
								no_of_rooms, 
								price_per_room, 
								price, 
								learning_rate)
	return price_per_room, base_price


def loading_data() :
	features = np.array([1, 2, 3, 5, 6, 7])
	labels = np.array([155, 197, 244, 356, 407, 448 ])
	
	return features, labels


# Anagram Checker
def check_anagram(word1, word2) :
	sorted_word1 = ''.join(sorted(word1.lower(), key=lambda x : ord(x[0])))
	sorted_word2 = ''.join(sorted(word2.lower(), key=lambda x : ord(x[0])))
	if sorted_word2 == sorted_word1 :
		print(f"'{word1}' '{word2}'    → ✅ Anagram")
	else :
		print(f"'{word1}' '{word2}'   → ❌ Not an Anagram")
	
if __name__ == "__main__" :
	#features, labels = loading_data() 
	#linear_regression(features, labels, learning_rate=0.01, epochs=10000)
	
	check_anagram("liSten", "silent")
	check_anagram("hello", "world")
	check_anagram("Dusty", "Study")
	check_anagram("abc", "ab")

# only one correction
# sorted() on a string already sorts characters in alphabetical order (which is the same as ord() order) — so the key argument adds no value here.
