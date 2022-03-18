"""

Inorder Successor

Given a node in a BST (may not be the root), find the in-order successor (also know as the next larger node).
The nodes in this BST will also have a parent field to traverse upwards the tree.

In a BST Inorder successor of a node is the next node in Inorder traversal of the Binary Tree. In order traverse as follow: Left-> Node -> Right.
Inorder Successor of an input node can also be defined as the node with the smallest key greater than the key of the input node.
Inorder Successor is NULL for the last node in Inorder traversal.

Example:

#     20
#    / \
#   8   22
#  / \
# 4   12
#    / \
#   10  14

In the above diagram:
 - Inorder successor of '8' is '10', because '10' is the smallest key that is greater than '8'
 - Inorder successor of '10' is '12', because '10' is the smallest key that is greater than '12'
 - Inorder successor of '14' is '20', because '20' is the smallest key that is greater than '14'

***
Note:
 (1) - If the node has a right child, then inorder successor will be the leftest descendent of the the right child if there are left descendent,
       because inorder visit the left child recursively to the end before visiting the node itself.
       Otherwise, if there is in fact a right child , then the successor will be the right child.
 (2) - If the node has non right child, then inorder successor will be:
       the parent of the ancestor that has as the left child the ancestor of the node in question (parent of the node 'to the right of the BST'),
       because inorder visit the left->node->right, so a node that does has a right child must be the end of the right subtree recursion,
       in which case the successor will be the parent that call that recursion on the left subtree.
***
"""


class Node:
	def __init__(self, value, left=None, right=None, parent=None):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent

	def __repr__(self):
		return f"(node: {self.value}, l: {self.left}, r: {self.right})"


def in_order_successor(node):
	if node.right:
		curr = node.right
		while curr.left:
			curr = curr.left
		return curr

	curr = node
	parent = curr.parent
	while parent and parent.left is not curr:
		curr = parent
		parent = parent.parent
	return parent


#     4
#    / \
#   2   8
#  /   / \
# 1   5   9
#      \
#       7


tree = Node(4)
tree.left = Node(2)
tree.right = Node(8)
tree.left.parent = tree
tree.right.parent = tree
tree.left.left = Node(1)
tree.left.left.parent = tree.left
tree.right.right = Node(7)
tree.right.right.parent = tree.right
tree.right.left = Node(5)
tree.right.left.parent = tree.right
tree.right.left.right = Node(7)
tree.right.left.right.parent = tree.right.left
tree.right.right = Node(9)
tree.right.right.parent = tree.right

print(in_order_successor(tree.right))  # 8 -> 9
print(in_order_successor(tree.left))  # 2 -> 4
print(in_order_successor(tree.right.left.right))  # 7 -> 8
print(in_order_successor(tree.right.right))  # 9 -> None (Last node does not have inorder successor)

