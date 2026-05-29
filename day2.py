def valdiate_password(password):
	uppercase_valid = False
	lowercase_valid = False
	digit_valid = False
	specialchar_valid = False #correction

	specialchars = "!@#$%&" #correction
	if(len(password) < 8) :
		return "❌ Weak   (too short)"

	for each_letter in password :
		uppercase_valid = uppercase_valid or each_letter.isupper()
		lowercase_valid = lowercase_valid or each_letter.islower()
		digit_valid = digit_valid or each_letter.isdigit()
		specialchar_valid = specialchar_valid or each_letter in specialchars
	
	message = ""
	if(not(uppercase_valid)) :
		message += "no uppercase,"

	if(not(lowercase_valid)) : 
		message += "no lowercase,"	

	if(not(digit_valid)) : 
		message += "no digit,"
	
	if(not(specialchar_valid)) :
		message += "no special char," #correction
	

	if(not(uppercase_valid and lowercase_valid and digit_valid and specialchar_valid)) :
		return f"❌ Weak   ({message})"
	else :
		return "✅ Strong"


if __name__ == "__main__" :
	passwords = ["hello", "Hello@1", "HELLO123", "Hello@123", "abc!DEF8"]
	for each_password in passwords :
		print(f"{each_password}  → {valdiate_password(each_password)}")
#stage2 corrections
#Special char check🐛 Wrong method
#Weak condition🐛 Wrong operator
#Typo (!=)🐛 Small mistake

#stage3 using any operator
#uppercase_valid = any(char.isupper() for char in password)
#lowercase_valid = any(char.islower() for char in password)
#digit_valid     = any(char.isdigit() for char in password)
#special_valid   = any(char in "!@#$%&" for char in password)
