def pig_latin(string):
	string = string.lower()
	consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
	first_letter = string[0]
	pig_latin = ''
	for consonant in consonants:
		if first_letter == consonant:
			pig_latin = string.split(consonant, 1)[1] + first_letter +"ay"
			return pig_latin
	else:
		pig_latin = string + "way"
		return pig_latin

print(pig_latin("Banana"))
print(pig_latin("example"))
print(pig_latin("hello hello"))

def palindrome(string):
	num = len(string) - 1
	second_half = ''
	mid = len(string) - 1
	while (num > mid/2):
		second_half += string[num]
		num -=1

	first_half = string[:len(string)/2]
	if first_half == second_half:
		return True
	else:
		return False

print(palindrome("racecar"))
print(palindrome("poop"))
print(pig_latin("panama"))