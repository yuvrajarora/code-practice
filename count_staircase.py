
def count_staircase(n):

	list1 = [0] * (n+1)
	list1[0] = 1
	list1[1] = 1
	for i in range(2,n+1):
		list1[i] = list1[i-1] + list1[i-2]
	print(list1)
	return list1[n]

if __name__ == '__main__':
	print("No. of ways: ",count_staircase(4))