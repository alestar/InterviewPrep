def min_coin_change(amount, coins):
	a = [0] * (amount + 1)
	for i in range(0, len(a)):
		a[i] = amount + 1  # Step - 0 Initialize the array with the biggest possible amount (amount + 1):
	# The highest possible count value for any element of a[i] is 'amount + 1',
	# Because there is no possible way to pick more coins to make the target (target amount < amount + 1)
	# Otherwise, there will be extra coins and that will added up to a higher amount than the target
	a[0] = 0

	for i in range(1,
				   amount + 1):  # Step 1 - Bottom-up fill all the counts to make all the amounts, until the target one
		for coin in range(len(coins)):  # Check all the different coins to see if they can make the current amount
			curr_amount = a[i]

			if coins[coin] <= i:  # Step 2 - Determine if selected coin can be use to or make the curr_amount:
				# If the selected coin (coins[j]) is less or equal than the curr_amount
				# Then, coin(s) can be added to make the amount or the amount can be break down into coin(s)
				# Otherwise, if the coin(s) is/are to big to make the curr_amount, those can't be used and therefore continue.

				# Step 3 - Calculate the remaining amount to be made, with the selected coin:
				# curr_amount - amount of coin 'selected'.
				remaining_amount = i - coins[coin]

				# Step 4 - Look up the remaining amount count:
				# How many coins are needed to make the remaining amount,  after selecting a coin.
				remaining_amount_count = a[remaining_amount]

				# Step 5 - Assign the min coin count necessary to make the current amount:
				# Between the current amount (default 'amount + 1') and the remaining amount count plus one.
				# If the remaining amount count is the min, then add one (to total amount of coin) for this round pick,
				# because there is still a coin to be selected/added to complete the current amount
				a[i] = min(curr_amount, remaining_amount_count + 1)

	if a[amount] > amount:  # Step 6 - Finally, If the original value was not altered
		return - 1  # it means, there were no coin(s) found that are suitable to constitute/add up to the target amount
	# due to the coins being to small or to large and not the right amount to constitute/add up to the target amount
	# and since the default was initialize to 'amount + 1' bigger than amount, it return -1
	print(a)
	return a[amount]


# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2]
coins = [1, 15, 20]
amount = 30
message = "The minimum amount of coin count needed to constitute/add up/break down target amount: '"
print(message + str(amount) + "' is: '" + str(min_coin_change(amount, coins)) + "'")
