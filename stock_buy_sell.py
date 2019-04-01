#Given a list of daily stock prices, return the buy and sell prices for making 
#the maximum profit

#use kadane's algorithm
import math
def stock_buy_sell(arr):
	if len(arr) <=2 and arr == None:
		return None
	current_buy = arr[0]
	current_profit = -math.inf 
	global_sell = arr[1]
	global_profit = global_sell - current_buy
	for i in range(0,len(arr)):
		# if the profit is greater than current profit the
		# then update global profit
		if current_profit > global_profit:
			global_profit = current_profit
			global_sell = arr[i]
		if arr[i] < current_buy:
			current_buy = arr[i]
	print (global_sell-global_profit, global_sell)


array = [8,6,5,4,3,2,1]
stock_buy_sell(array)