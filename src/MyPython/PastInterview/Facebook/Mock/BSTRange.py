"""
You are given a binary search tree. Goal is to find sum of all elements in the tree which are in range [low, high],
inclusive.

#        6
#      /   \
#     4     8
#    / \   / \
#   3   5 7   9
#  /
# 2

Input: [3, 10] => 42
Input: [2, 5] => 14
Input: [8, 9] => 17
Input: [4, 6] => 15
Input: [20, 50] => 0
Input: [1, 4] => 9

My own edge cases
Input: [6, 9] => 30
Input: [4, 9] => 39
Input: [4, 7] => 22
Input: [5, 7] => 18

"""

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __repr__(self):
		return f"(node: {self.value}, l: {self.left}, r: {self.right})"


def sum_val_in_range(curr, low, high):
	addition = 0

	# If the curr node is None return addition = 0, since there is nothing to add
	if curr is None:
		return addition

	# Verify current node is in range
	# If so, add its value to the addition
	if low <= curr.value <= high:
		addition += curr.value
	# If the node value is not in the range entirely, verify each bound

	# If current value in range with lower bound
	if curr.value > low:
		
		# Continue exploring from the left sub tree, and add the result
		addition += sum_val_in_range(curr.left, low, high)
	# Otherwise, if is smaller than lower bound, the left subtree is guarantee to be smaller and therefore out of low bound of the range.
	# Hence, dont search on the left subtree

	# If current value in range with upper bound
	if curr.value < high:

		# Continue exploring from the right sub tree, and add the result
		addition += sum_val_in_range(curr.right, low, high)
	# Otherwise, if is bigger than higher bound, the right subtree is guarantee to be bigger and therefore out of high bound of the range.
	# Hence, dont search on the right subtree

	return addition


def sum_val_in_range2(curr, low, high):
	addition = 0
	if curr is None:  # If the root is None return sol = 0
		return addition
	if low <= curr.value <= high:  # Verify current node is in range
		addition += curr.value  # if so, added to the sum

	left = curr.left
	if left is not None:
		if left.value >= low:  # If there is a left node and is bigger/equal than lower bound of the range
			addition += sum_val_in_range2(left, low, high)  # Continue exploring from the left sub tree, and add the result
		else:  # However, if the left node is smaller than lower bound
			addition += sum_val_in_range2(left.right, low, high)  # Attempt to explore from the right subtree of the left node
		# Since, it is only in the right subtree that could be elements (if they exist) in the range at this point
		# Because the left of the left (if exist) is guarantee, to be smaller that lower bound of the range.

	right = curr.right
	if right is not None:
		if right.value <= high:  # If there is a right node and is smaller/equal than upper bound of the range
			addition += sum_val_in_range2(right, low, high)  # Continue continue exploring from the right sub tree, and add it
		else:  # However, if the right node is bigger than upper bound
			addition += sum_val_in_range2(right.left, low, high)  # Attempt to explore the left subtree of the right node
			# Since, it is only in the left subtree that could be elements (if they exist) in the range at this point
			# Because the right of the right (if exist) is guarantee, to be bigger than upper bound of the range.
	return addition


# Driver Code
if __name__ == "__main__":
	# Build BST tree
	#        6
	#      /   \
	#     4     8
	#    / \   / \
	#   3   5 7   9
	#  /
	# 2

	# Creating the root node
	bst = Node(6)

	# Building left sub-tree
	bst.left = Node(4)
	bst.left.left = Node(3)
	bst.left.left.left = Node(2)
	bst.left.right = Node(5)

	# Building right sub-tree
	bst.right = Node(8)
	bst.right.left = Node(7)
	bst.right.right = Node(9)

	# Testing
	sum_range = sum_val_in_range(bst, 3, 10)
	print("# Input: [3, 10] - Expected: 42  - Actual: " + str(sum_range))
	sum_range = sum_val_in_range(bst, 2, 5)
	print("# Input: [2, 5] - Expected: 14  - Actual: " + str(sum_range))
	sum_range = sum_val_in_range(bst, 8, 9)
	print("# Input: [8, 9] - Expected: 17  - Actual: " + str(sum_range))
	sum_range = sum_val_in_range(bst, 4, 6)
	print("# Input: [4, 6] - Expected: 15  - Actual: " + str(sum_range))
	sum_range = sum_val_in_range(bst, 20, 50)
	print("# Input: [20, 50] - Expected: 0  - Actual: " + str(sum_range))
	sum_range = sum_val_in_range(bst, 1, 4)
	print("# Input: [1, 4] - Expected: 9  - Actual: " + str(sum_range))
	sum_range = sum_val_in_range(bst, 4, 9)
	print("# Input: [4, 9] - Expected: 39  - Actual: " + str(sum_range))
	sum_range = sum_val_in_range(bst, 6, 9)
	print("# Input: [6, 9] - Expected: 30  - Actual: " + str(sum_range))
	sum_range = sum_val_in_range(bst, 4, 7)
	print("# Input: [4, 7] - Expected: 22  - Actual: " + str(sum_range))
	sum_range = sum_val_in_range(bst, 5, 7)
	print("# Input: [5, 7] - Expected: 18  - Actual: " + str(sum_range))