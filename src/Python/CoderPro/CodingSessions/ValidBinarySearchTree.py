"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
  5
 / \
4   7

Input: root = [2,1,3]
Output: true

Example 2:

  5
 / \
1   4
   / \
  3   6

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

"""


class Node(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution(object):
	def _isValidBSTHelper(self, n, low, high):
		if not n:
			return True

		val = n.val
		if low < val < high and\
			self._isValidBSTHelper(n.left, low, n.val) and\
			self._isValidBSTHelper(n.right, n.val, high):
			return True
		return False

	def isValidBST(self, n):
		# Start by calling the method recur from the root
		# use  - inf for lower bound and if as upper bound since anything is permissible
		return self._isValidBSTHelper(n, float('-inf'), float('inf'))


#   5
#  / \
# 4   7
node = Node(5)
node.left = Node(4)
node.right = Node(7)
print(Solution().isValidBST(node))

#   5
#  / \
# 4   7
#    /
#   2
node = Node(5)
node.left = Node(4)
node.right = Node(7)
node.right.left = Node(2)
print(Solution().isValidBST(node))
# False
