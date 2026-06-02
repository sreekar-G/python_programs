### linear regression problem ### 
### with square trick ###

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


#p^ = m'r + b'
def absolute_trick(base_price, no_of_rooms, price_per_room, price, learning_rate) :
	predicted_price = base_price + no_of_rooms * price_per_room
	if (price > predicted_price) : 
		price_per_room += learning_rate * no_of_rooms
		base_price += learning_rate
	else :
		price_per_room -= learning_rate * no_of_rooms
		base_price -= learning_rate
	return price_per_room, base_price


#Caesar Cipher
#Write a function that encodes and decodes a message by shifting each letter by N positions. Non-letter characters stay unchanged.

def ceaser_cipher(message, shift) :
	encoded_message = "" 
	for each_char in message : 
		if each_char.isupper() : 
			encoded_message += chr((ord(each_char) - ord('A') + shift) % 26 + ord('A'))
		elif each_char.islower() : 
			encoded_message += chr((ord(each_char) - ord('a') + shift) % 26 + ord('a'))
		else : 
			encoded_message += each_char
	return encoded_message

if __name__ == "__main__" :
	message = "Hello, World!"
	shift = 3
	encoded_message = ceaser_cipher(message, shift)
	decoded_message = ceaser_cipher(encoded_message, -shift)
	print(f"Encoded  → {encoded_message}\nDecoded  → {decoded_message}")
	
