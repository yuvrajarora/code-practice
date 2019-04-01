
def max_subarray_nonadjacent(arr):

	#boundary case, if the length of the array is less than 0
	if len(arr)<0:
		return 0

	elif len(arr) == 1:
		return arr[0]

	incl = arr[0]
	excl = 0

	for i in range(1,len(arr)):
		temp = incl
		incl = max(incl,arr[i]+excl)
		excl = temp

	return incl
def main():
	v = [1, 6, 10, 14, 50, -20, -5, -10]
	sum = max_subarray_nonadjacent(v)
	print ("Maximum Sum non adjacent: ",sum)

if __name__ == '__main__':
	main()