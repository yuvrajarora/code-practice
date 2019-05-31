# perform basic string compression using the counts of repeated characters
# aabcccccaaa -> a2b1c5a3
# if compressed string would not become smaller than the original string, return original string

# Approach:
# 1. loop through the string and check if current character is not equal to previous character,
#    then reset the counter to 0 and add current count and previous character to new list
# 2. create a hash map which counts the occurrence of a character

def compress_string(string):
	compress = []
	counter = 0
	for i in range(len(string)):
		if string[i] != string[i-1] and i!=0:
			compress.append(string[i-1] + str(counter))
			counter = 0
		counter += 1

	#add the last occurrence to compress string
	compress.append(string[-1] + str(counter))

	return min(''.join(compress),string,key=len)

def main():
	print(compress_string("aabccccaaa"))

if __name__ == '__main__':
	main()
