"""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
#      4              4
#    /   \          /   \
#   2     7  ->    7     2
#  / \   / \      / \   / \
# 1   3 6  9     9   6 3   1

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]


Example 2:
#      2            2
#    /   \   ->   /  \
#   1     3      3    1

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

"""


class Node(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __repr__(self):
		result = self.val
		result += f"{self.left}" if self.left else ''
		result += f"{self.right}" if self.right else ''
		return result


class Solution(object):
	def invert(self, node):
		if not node:
			return None
		left = self.invert(node.left)
		right = self.invert(node.right)
		node.right = left
		node.left = right
		return node


n = Node('a')
n.left = Node('b')
n.right = Node('c')
n.left.left = Node('d')
n.left.right = Node('e')
n.right.left = Node('f')

#       a
#     /  \
#    b    c
#   / \  /
#  d  e  f

print(n)
# 'abdecf'

#       a
#     /  \
#    c    b
#     \  / \
#     f e   d
print(Solution().invert(n))
# 'acfbed'
