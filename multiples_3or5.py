# Sum of all multiples of 3 or 5 less than 1000, and how you calculated it 
sum = 0
#run a for loop for 1000 numbers and check if divisible by 3 or 5 and sum it.
for i in range(0,1000):
    if (i % 3 == 0 or i % 5 == 0):
        sum = sum + i
print(sum)