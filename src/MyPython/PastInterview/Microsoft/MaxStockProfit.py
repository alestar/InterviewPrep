# you can write to stdout for debugging purposes, e.g.
# prices: { 1, 3, 5, 7}
# prices: { 1, 5, 3, 7}
# prices: { 5, 5}
# Buying price: 1, selling price : 7, profit 6
# Output: 1, 7

def profit_stock(prices):
	if not prices:
		return 0

	max_profit = 0
	min_price = prices[0]

	for price in prices:
		if min_price > price:
			min_price = price
		curr_profit = price - min_price
		max_profit = max(max_profit, curr_profit)
	return max_profit


print(profit_stock([]))
print(profit_stock([0]))
print(profit_stock([1]))
print(profit_stock([1, 1]))
print(profit_stock([5, 5, 5]))
print(profit_stock([1, 3, 5, 7]))
print(profit_stock([2, 3, 7, 1, 5]))
print(profit_stock([3, 2, 1]))
