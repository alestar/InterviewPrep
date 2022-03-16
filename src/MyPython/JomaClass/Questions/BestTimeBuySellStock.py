# O(n^2)
def buy_and_sell_brute(arr):
	max_profit = 0

	for i in range(len(arr)):
		for j in range(i, len(arr)):
			max_profit = max(max_profit, arr[j] - arr[i])
	return max_profit

# O(n)
def buy_and_sell_iter(arr):
	max_current_price = 0
	max_profit = 0

	# Iterate throw the array in reverse to always obtain the current max profit
	# Update the current max price by comparing the max current price so far, with every new price
	# Update the current profit, which is the digg max_curr_price so far and current price
	# Update the max current profit by comparing the max current profit so far, with current profit
	for price in arr[::-1]:
		max_current_price = max(max_current_price, price)
		max_profit = max(max_profit, max_current_price - price)
	return max_profit


print(buy_and_sell_brute([9, 11, 8, 5, 7, 10]))  # 5
print(buy_and_sell_iter([9, 11, 8, 5, 7, 10]))  # 5
