# Given a dictionary of words and an input string tell whether the input string can be 
#completely segmented into dictionary words

def string_segmentation(str1,dict1,solved):
	for i in range(1,len(str1)+1):
		first_word = str1[:i]
		print(i,first_word)
		if first_word in dict1:
			second_word = str1[i:]
			if not second_word:
				return True
			if second_word not in solved:
				if string_segmentation(second_word,dict1,solved):
					return True		
				solved.add(second_word)
	return False

def can_segment_string(s, dict):
  solved = set([])
  return string_segmentation(s, dict, solved)
  
  
if __name__ == '__main__':
  s = "applepie";
  dict = set(["pie","pear","apple","peach"])
  if can_segment_string(s, dict):
    print ("can break.")
  else:
    print ("can't break.")
