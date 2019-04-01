# Given two strings, write a method to decide if one is a permutation of the other

# Example:
# 1. 'abcd' is a permutation of 'dcab'
# 2. 'abcde' is not a permutation of 'abcd'. Different lengths

# Questions:
# 1. How to handle white spaces?
# 2. Case sensitivity of characters? Is 'Abcd' same as 'abcd'?

# Approach:
# 1. Sort the strings. Compare the final strings to one another.
# 2. Use a hash table.
# 3. Use a structure similar to bit vector. Assuming the string follows the ASCII
#    standard character set.
# 	 Increment the value for an index by one for the first string. 
# 	 Decrement the value for a particular index by one for the second string
# 	 if for the second string, any of the value is < 0, return False

def check_permutation(string1, string2):
	if len(string1) != len(string2):
		return False
	bit = [0 for _ in range(128)]
	for str1 in string1:
		value = ord(str1)
		bit[value] += 1
	for str2 in string2:
		value = ord(str2)
		bit[value] -= 1
		if bit[value] <0:
			return False
	return True

if __name__ == '__main__':
	print(check_permutation('abcd', 'dcba'))
	print(check_permutation('abed', 'dcba'))
	print(check_permutation('abcde', 'dcba'))

# Time Complexity: 
# O(len(longest string))