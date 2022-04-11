"""
Find Subtree

Given 2 binary trees t and s, find if s has an equal subtree in t, where the structure and the values are the same.
Return True if it exist, otherwise return False.

"""

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def pre_order_serialize(n):
	if not n:
		return 'null'
	return '-' + str(n.value) + '-' + pre_order_serialize(n.left) + '-' + pre_order_serialize(n.right)


def find_subtree(a, b):
	return pre_order_serialize(b) in pre_order_serialize(a)


def find_subtree2(a, b):
	if not a:
		return False

	is_match = a.value == b.value
	if is_match:
		is_match_left = (not a.left and not b.left) or find_subtree2(a.left, b.left)
		if is_match_left:
			is_match_right = (not a.right and not b.right) or find_subtree2(a.right, b.right)
			if is_match_right:
				return True

	return find_subtree2(a.left, b) or find_subtree2(a.right, b)


#      a			b

#      1			4
#    /   \		   / \
#   4     5       3   2
#  / \   / \
# 3   2 4   1

a = Node(1)
a.left = Node(4)
a.right = Node(5)
a.left.left = Node(3)
a.left.right = Node(2)
a.right.left = Node(4)
a.right.right = Node(1)

b = Node(4)
b.left = Node(3)
b.right = Node(2)

print(find_subtree(a, b))
# True

print(find_subtree2(a, b))
# True
