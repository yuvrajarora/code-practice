# There are three types of edits that can be performed on strings: insert a character, remove a character, or
# replace a character. Given two strings, write a function to check if they are one edit or zero edits away

# Example:
# pale, ple -> true
# pale, bake -> false

# Approach:
# 1. write conditions for checking replace, insert and delete. Insert and Delete will be similar
# O(n) length of shorter string

def oneEditAway(first, second):
	if len(first) == len(second):
		return oneEditReplace(first,second)
	elif len(first)+1 == len(second): #Aple and Apple
		return oneEditInsert(first, second) #for insertion
	elif len(first)-1 == len(second): #Apple and Aple
		return oneEditInsert(second,first) #for deletion

def oneEditReplace(s1, s2):
	foundDiff = False 
	for i in range(0,len(s1)):
		if s1[i] != s2[i]:
			if foundDiff:
				return False
			foundDiff = True 

def oneEditInsert(s1,s2):
	idx1 = 0
	idx2 = 0
	while idx1 < len(s1) and idx2 < len(s2):
		if s1[idx1] != s2[idx2]:
			if idx1 != idx2:
				return False
			idx2+=1
		else:
			idx2+=1
			idx1+=1
	return True

def main():
	s1 = "Apple"
	s2 = "Appppe"
	print(oneEditAway(s1,s2))

if __name__ == '__main__':
	main()
