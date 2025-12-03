def binary_search_recur(lis, low, high, key):

	if high >= low:
		mid = low + (high - low) // 2

		if lis[mid] == key:
			return mid
		elif lis[mid] < key:
			return binary_search_recur(lis, mid + 1, high, key)
		elif lis[mid] > key:
			return binary_search_recur(lis, low, mid - 1, key)
	else:
		return -1


def binary_search_iter(lis, low, high, key):
	if high >= low:
		while low <= high:
			mid = low + (high - low) // 2
			if lis[mid] == key:
				return mid
			elif lis[mid] < key:
				low = mid + 1
			else:
				high = mid - 1
	return -1


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

val_1 = 4
val_2 = 20

print("binary_search_iter for val_1: " + str(val_1) + ", gave index: " + str(
	binary_search_iter(list_1, 0, len(list_1) - 1, val_1)))
print("binary_search_iter for val_2: " + str(val_2) + ", gave index: " + str(
	binary_search_iter(list_1, 0, len(list_1) - 1, val_2)))
print("binary_search_recur for val_1: " + str(val_1) + ", gave index: " + str(
	binary_search_recur(list_1, 0, len(list_1) - 1, val_1)))
print("binary_search_recur for val_2: " + str(val_2) + ", gave index: " + str(
	binary_search_recur(list_1, 0, len(list_1) - 1, val_2)))
