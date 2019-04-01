# Given a string, write a function to check if it is a permutation of a palindrome. 
# A palindrome is a rearrangement of letters. The palindrome does not need to be 
# limited to just dictionary words.

# Example:
# Input: tact Coa
# Output: "taco cat", "atco cta"

# Questions:
# 1. Case Sensitive?


# Approach:
# The input string should have two instances of every character - For even length string
# The input string should have no more than one character that is odd - For odd length string

def palindrome_permutation(string):
	d = {}
	found = False
	for str in string:
		value = char_number(str)
		if value == -1:
			continue
		if value in d:
			d[value] += 1
		else:
			d[value] = 1
	# to check if there are no more than one character that is odd
	for n in d.values():
		if n % 2 == 1:
			if found:
				return False
			found = True
	return True

#For case sensitive
def char_number(c):
	a = ord('a')
	z = ord('z')
	A = ord('A')
	Z = ord('Z')
	val = ord(c)

	#Scaling the characters
	if a<= val <= z:
		return val-a
	elif A<= val <= Z:
		return val-A 
	return -1


if __name__ == "__main__":
	print(palindrome_permutation('Tact Coa'))
	print(char_number('b'))