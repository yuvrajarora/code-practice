# Implement an algorithm to determine if a string has all unique characters
# can't use additional data structures

# Questions:
# 1. Are the characters of ASCII or Unicode encoding?
#    if ASCII. Standard or Extended Set?
# 	 if Unicode. Then how many bits? 8,16,32?
# 2. Do we have additional space?

# Approach:
# 1. Compare every character in the string to every other.
# 2. If allowed to modify string, then sort the string and compare 
#    the neighbouring characters
# 3. Make a bit vector, Assuming standard ASCII 128 length.
#    Iterate through the string and calculate ASCII value of
#	 that character and set it to True in the bit vector.
#	 If already set to True, then return False
# 	 Else return True.

def is_unique(string):
	bit = [False for _ in range(128)]
	for s in string:
		value = ord(s)
		if bit[value]:
			return False
		bit[value] = True
	return True

if __name__ == '__main__':
	print(is_unique('abcd'))
	print(is_unique('abbcd'))

# Time Complexity:
# O(len(str)) - iterating through the string once and setting the 
# bit vector accordingly