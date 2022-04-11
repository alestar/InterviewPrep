"""
Contiguous Subarrays
You are given an array arr of N integers. For each index i, you are required to determine the number of contiguous subarrays that fulfill the following conditions:
	The value at index i must be the maximum element in the contiguous subarrays, and
	These contiguous subarrays must either start from or end on index i.
Signature
	int[] countSubarrays(int[] arr)
Input
	Array arr is a non-empty list of unique integers that range between 1 to 1,000,000,000
	Size N is between 1 and 1,000,000
Output
	An array where each index i contains an integer denoting the maximum number of contiguous subarrays of arr[i]
Example:
	arr = [3, 4, 1, 6, 2]
	output = [1, 3, 1, 5, 1] = [1, 2, 1, 2, 1]
							 = [1, 2, 1, 4, 1]
							 = [2, 4 ,2, 6, 2]
Explanation:
	For index 0 - [3] is the only contiguous subarray that starts (or ends) with 3, and the maximum value in this subarray is 3.
	For index 1 - [4], [3, 4], [4, 1]
	For index 2 - [1]
	For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
	For index 4 - [2]
	So, the answer for the above input is [1, 3, 1, 5, 1]

Solution approach 1
	L[i] be the number of valid subarrays ending at index i, and
	R[i] be the number of valid subarrays beginning at index i,
	output[i] = L[i] + R[i] - 1.
	Computing R[1..N] is equivalent to computing L[1..N] if array were reversed,
	allowing us to reduce the problem to computing L[1..N] for an array of N distinct integers.

Example:
	arr = [3, 4, 1, 6, 2]
	output = [1, 3, 1, 5, 1]
	output[0] = >  max val '3' => left:[3] + right:[3] = L[0] + R[0] - 1 = 1 + 1 - 1 = 1
	output[1] = >  max val '4' => left:[3, 4], [4] + right: [4], [4,1]= L[1] + R[1] - 1 = 2 + 2 - 1 = 3
	output[2] = >  max val '1' => left:[1] + right: [1] = L[2] + R[2] - 1 = 1 + 1 - 1 = 1
	output[3] = >  max val '6' => left: [1, 6], [4, 1, 6], [3, 4, 1, 6], [6] + right: [6], [6, 2]= L[3] + R[3] - 1 = 4 + 2 - 1 = 5
	output[4] = >  max val '2' => left:[2] + right: [2] = L[4] + R[4] - 1 = 1 + 1 - 1 = 1


Solution approach 2
	We can next observe that the index of the latest element to the left of the ith element ( which is larger than it)
	determines which subarrays ending at index i are valid
	Specifically, the ones beginning to the right of that larger element.
	Letting G[i] be equal to the largest index j such that j < i and a[j] > a[i] (or equal to 0 if there’s no such j), then L[i] = i - G[i].
	We’ve now reduced the problem to computing these values G[1..N] for an array of N distinct integers.

Example:
	arr = [3, 4, 1, 6, 2]
	output = [1, 3, 1, 5, 1]
	G[0] = 0 => largest index j such that j = -1 < i = 0 and a[-1] = None > a[0] = 3, does not exist => L[0] = 0 - G[0] = 0 - 0 = 0. Should be '1'
	G[1] = 0 => largest index j = 0 < i = 1 and a[0] = 3 > a[1] = 4, does not exist => L[1] = 1 - G[1] = 1 - 0 = 1. Should be '2'
	G[2] = 1 => largest index j = 1 < i = 2 and a[1] = 4 > a[2] = 1, exist => L[2] = 2 - G[2] = 2 - 1 = 1.
	G[3] = 4 => largest index j = 1 < i = 2 and a[1] = 4 > a[3] = 6, does not exist => L[3] = 3 - G[3] = 3 - 0 = 3. Should be '4'
	G[4] = 1 => largest index j = 3 < i = 4 and a[3] = 6 > a[4] = 2, exist => L[4] = 4 - G[3] = 4 - 3 = 1.


Solution approach 3
	Computing G[i] for each i from 1 to N is a promising approach, but we’ll still need to consider how to do so as efficiently as possible.
	We can observe that it’s not possible to compute G[i] purely based on the values of G[i-1], a[i-1], and a[i];
	we may need more information about earlier a values as well, but would like to avoid simply scanning over all of them.
	Out of earlier indices j (such that j < i), we can consider which indices are worth considering as potential candidates for G[i] - for example,
	if there exists a pair of indices j and k such that j < k and a[j] < a[k], can index j ever be a candidate for G[i] for any i > k?
	If we can maintain information about the set of these possible candidate indices as we go through the array,
	it’s possible to efficiently determine the one that’s actually equal to G[i] for each i.

Example:
	arr = [3, 4, 1, 6, 2]
	output = [1, 3, 1, 5, 1]

"""

# Step - 1
# Iterate left to right
# Compare current element with peek() stack
# Everytime an element is smaller push(i) into the stack and check the next element
# If current element is bigger than peek(), then pop() from stack and calculate interval/subarray length for j = curr index
# Calculate j = curr - i and add it to the array


# Step - 2
# when array is completed
# empty the stack like you were comparing to a bigger element
# calculate j = curr - i and add it to the array

# Step - 3
# Iterate right to left
# everytime and element is smaller push(i) into the stack and check the next element
# compare current element with peek() stack
# if current element is bigger than peek(), then pop() from stack and calculate interval/subarray length for j = curr index
# calculate j = curr - i and add it to the array

# Step - 2
# when array is completed
# empty the stack like you were comparing to a bigger element
# calculate j = curr - i and add it to the array

# Step - 5
# Rest minus one considering that elements are count twice (in both directions)

# [3, 4, 1, 6, 2]
# [1, 2, 1, 2, 1] left to right
# [1, 2, 1, 4, 1] right to left
# [2, 4 ,2, 6, 2] total
# [1, 3, 1, 5, 1] total -1 , to account for double visited
def count_subarrays(arr):
	n = len(arr)
	sol = [0] * n
	onboard = []
	# Going from left to right
	for i in range(n):
		while onboard and arr[onboard[-1]] < arr[i]:  # While there are elements in the queue and curr element 'i' bigger than peek() (usually prev elements)
			mounted = onboard.pop() 	# pop() index of the element from the stack
			# mounted index is the index where element was added to the stack.
			sol[mounted] = i - mounted  # Calculate the distance or count of elements of sub-array,
			# which is de difference in between curr 'i' and index were element was mounted
		onboard.append(i)  # If the curr element 'i' is less than stack peek(), then push() to the stack and continue with next element in array

	# When finish with array, process remaining items in the stack
	while onboard:
		mounted = onboard.pop()
		sol[mounted] = len(arr) - mounted  # Calculate the distance or count of elements of sub-array,
		# but in this case, is de difference in between the index of the last element and index were element was mounted,
		# because iterating from left to right, finished the whole array and current is at the last element,
		# Therefore, the remaining elements needs to be compare with the last index n-1
	# print(sol)

	# Going from right to left
	for i in range(n-1, -1, -1):
		sol[i] -= 1  # Decrease the total count by 1 one because index will count again (twice) in the reverse direction
		while onboard and arr[i] > arr[onboard[-1]]:
			mounted = onboard.pop()
			sol[mounted] += mounted - i  # Reverse the distance count calculation formula since is in reverse direction, and add it to previous count for that index
		onboard.append(i)

	# When finish with array (in reverse), process remaining items in the stack
	while onboard:
		mounted = onboard.pop()
		sol[mounted] += mounted + 1  # Simply add one ??
	# print(sol)

	return sol


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
	print('[', n, ']', sep='', end='')


def printIntegerList(array):
	size = len(array)
	print('[', end='')
	for i in range(size):
		if i != 0:
			print(', ', end='')
		print(array[i], end='')
	print(']', end='')


test_case_number = 1


def check(expected, output):
	global test_case_number
	expected_size = len(expected)
	output_size = len(output)
	result = True
	if expected_size != output_size:
		result = False
	for i in range(min(expected_size, output_size)):
		result &= (output[i] == expected[i])
	rightTick = '\u2713'
	wrongTick = '\u2717'
	if result:
		print(rightTick, 'Test #', test_case_number, sep='')
	else:
		print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
		printIntegerList(expected)
		print(' Your output: ', end='')
		printIntegerList(output)
		print()
	test_case_number += 1


if __name__ == "__main__":
	test_1 = [3, 4, 1, 6, 2]
	expected_1 = [1, 3, 1, 5, 1]
	output_1 = count_subarrays(test_1)
	check(expected_1, output_1)

	test_2 = [2, 4, 7, 1, 5, 3]
	expected_2 = [1, 2, 6, 1, 3, 1]
	output_2 = count_subarrays(test_2)
	check(expected_2, output_2)