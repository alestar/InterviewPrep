"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
"""


# O(n^2)
def buy_and_sell_brute(arr):
	max_profit = 0

	for i in range(len(arr)):
		for j in range(i, len(arr)):
			max_profit = max(max_profit, arr[j] - arr[i])
	return max_profit


# O(n)
def buy_and_sell_iter_reverse(arr):
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


def buy_and_sell_iter(prices):
	if not prices:
		return 0

	max_profit = 0
	min_price = prices[0]

	for p in prices:
		if min_price > p:
			min_price = p
		max_profit = max(max_profit, p - min_price)
	return max_profit


print(buy_and_sell_brute([9, 11, 8, 5, 7, 10]))  # 5
print(buy_and_sell_iter_reverse([9, 11, 8, 5, 7, 10]))  # 5
print(buy_and_sell_iter([9, 11, 8, 5, 7, 10]))  # 5

