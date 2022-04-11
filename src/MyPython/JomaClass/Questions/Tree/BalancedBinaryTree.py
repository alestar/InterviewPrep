"""
Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:

#     3
#    / \
#   9  20
#  /  / \
# 4  15  7

Input: root = [3,9,20,null,null,15,7]
Output: True

Example 2:
#       1
#      / \
#     2  2
#    / \
#   3   3
#  / \
# 4   4

Input: root = [1,2,2,3,3,null,null,4,4]
Output: False


Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

"""


class Node(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution(object):
	# return value (isBalanced, height)
	def _is_balanced_helper(self, node):
		if not node:
			return True, 0

		l_balanced, l_height = self._is_balanced_helper(node.left)
		r_balanced, r_height = self._is_balanced_helper(node.right)
		return (l_balanced and r_balanced and abs(l_height - r_height) <= 1,
				max(l_height, r_height) + 1)

	def is_balanced(self, n):
		return self._is_balanced_helper(n)[0]


n = Node(1)
n.left = Node(2)
n.left.left = Node(4)
n.right = Node(3)
#     1
#    / \
#   2   3
#  /
# 4
print((Solution().is_balanced(n)))

n.right = None
#    1
#   /
#  2
# /
# 4
print(Solution().is_balanced(n))
# False
