# you can write to stdout for debugging purposes, e.g.

class Node(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def is_bst_helper(node, low_bound, upper_bound):
	if not node:
		return True

	if low_bound < node.val < upper_bound and\
			is_bst_helper(node.left, low_bound, node.val) and\
			is_bst_helper(node.right, node.val, upper_bound):
		return True
	return False


def is_bst(node):
	return is_bst_helper(node, float('-inf'), float('inf'))


#           10
#         /    \
#        6      13
#       / \    /  \
#      1   12  9  14
# False

#           10
#         /    \
#        6      13
#       / \    /  \
#      1   8  11  14
# True


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
