def min_coin_change(amount, coins):

	# Step - 0 Initialize the array of counts with the biggest possible amount (amount + 1):
	# The highest possible count value for any element of a[i] is 'amount + 1',
	# Because there is no possible way to pick more coins to make the target (target amount < amount + 1)
	# Otherwise, there will be extra coins and that will added up to a higher amount than the target
	arr_counts = [0] * (amount + 1)
	for i in range(0, len(arr_counts)):
		arr_counts[i] = amount + 1
	arr_counts[0] = 0

	# Step 1 - Bottom-up fill all the counts to make all the amounts, until the target one
	# Check all the different coins to see if they can make the current amount
	for curr_amount in range(1, amount + 1):
		for curr_coin in range(len(coins)):
			curr_amount_count = arr_counts[i]

			# Step 2 - Determine if selected coin can be use to or make the curr_amount:
			# If the selected coin (coins[j]) is less or equal than the 'curr_amount'
			# Then, coin(s) can be added to make the amount or the amount can be break down into the coin(s)
			# Otherwise, if the coin(s) is/are to big to make the curr_amount, those can't be used and therefore continue.
			if coins[curr_coin] <= curr_amount:

				# Step 3 - Calculate the remaining amount to be made, with the selected coin:
				# curr_amount - amount of coin 'selected'.
				remaining_amount = curr_amount - coins[curr_coin]

				# Step 4 - Look up the remaining amount count:
				# How many coins are needed to make the remaining amount,  after selecting a coin.
				remaining_amount_count = arr_counts[remaining_amount]

				# Step 5 - Assign the min coin count necessary to make the current amount:
				# Between the current amount (default 'amount + 1') and the remaining amount count plus one (this round pick).
				# If the remaining amount count is the min,
				# Then, add one (to total amount of coin counts) for this round pick,
				# because a coin is being selected/added to complete the current amount, with the remaining amount count
				arr_counts[curr_amount] = min(curr_amount_count, remaining_amount_count + 1)

	# Step 6 - Finally, If the original value was not altered
	# it means, there were no coin(s) found that are suitable to constitute/add up to the target amount
	# due to the coins being too small or too large and not the right amount to constitute/add up to the target amount
	# and since the default was initialize to 'amount + 1' bigger than amount, it return -1
	if arr_counts[amount] > curr_amount:
		return - 1
	print(arr_counts)
	return arr_counts[amount]


# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2]
c = [1, 2, 5, 15, 20]
a = 30
b = 21
d = 11
f = 10020
e = 666
message = "The minimum amount of coin count needed to constitute/add up/break down a target amount: '"
print(message + str(a) + "' is: '" + str(min_coin_change(a, c)) + "'")
print(message + str(b) + "' is: '" + str(min_coin_change(b, c)) + "'")
print(message + str(d) + "' is: '" + str(min_coin_change(d, c)) + "'")
print(message + str(f) + "' is: '" + str(min_coin_change(f, c)) + "'")
print(message + str(e) + "' is: '" + str(min_coin_change(e, c)) + "'")
