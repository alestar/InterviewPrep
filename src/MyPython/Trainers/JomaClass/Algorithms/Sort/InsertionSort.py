# Insertion sort in Python

def insertionSort(array):

	# Start from the second element to compare with first one
	for step in range(1, len(array)):
		key = array[step]
		# Star comparing left elements loop from the prev element
		j = step - 1

		# Compare 'key' with each element on the left of it, until an element smaller is found
		# (for descending order, change array[j] > key to array[j] < key)
		while j >= 0 and array[j] > key:

			# Replace element to the right of curr, with curr (move curr element to the right before insertion)
			array[j + 1] = array[j]

			# Move to the left for next comparison
			j = j - 1

		# When an element that is smaller than the key is found
		# Insert key element right after the smaller element
		array[j + 1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)
