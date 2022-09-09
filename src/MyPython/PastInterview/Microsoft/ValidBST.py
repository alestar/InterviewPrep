"""
Validate binary search tree

   3
  / \
 2   4
 /   /\
 1  3.5  5

 True or False

"""

class Node:
	def __init__(self, val, left=None, right=None):
		self.val= val
		self.left = left
		self.right = right

class Solution:
	def is_valid_tree_recur(self, node, low, high):
		if not node:
			return True

		val = node.val
		if low < val < high and self.is_valid_tree_recur(node.left, low, node.val) and self.is_valid_tree_recur(node.right, node.val, high):
			return True
		return False

	def is_valid_tree(self, node):
		return self.is_valid_tree_recur(node, float('-inf'), float('inf'))

bst = Node(10)
bst.left = Node(6)
bst.right = Node(13)
bst.left.left = Node(1)
bst.left.right = Node(8)  # True
# bst.left.right = Node(12)  # False
bst.right.left = Node(11)  # True
# bst.right.left = Node(9)  # False
bst.right.right = Node(14)

print(is_bst(bst))
