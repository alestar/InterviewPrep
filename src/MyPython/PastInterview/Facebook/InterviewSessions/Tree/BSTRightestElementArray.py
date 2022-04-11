"""
FB Python.Interview with (agrichuk )
Given a tree:
             1 -----> 1
            / \
           3  9  ------> 9
          /\   \
         4  5  10 -----> 10
        /     / \
       7     11  12 -----> 12
      /
     8 ---------------->8

Output: Return arr[1,9,10,12,8]
"""
from collections import deque


class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __repr__(self):
		return f"(node: {self.value}, l: {self.left}, r: {self.right})"


# Collect all the rightest elements
def rightest_elems(node):
	if not node:
		return

	# Use a Queue for node that has not been visited yet and are pending to explore
	queue = deque()
	queue.append((0, node))
	rightest = {0: node.value}

	while queue:
		depth, curr_node = queue.popleft()
		rightest[depth] = curr_node.value

		if curr_node.left:
			queue.append((depth + 1, curr_node.left))
		if curr_node.right:
			queue.append((depth + 1, curr_node.right))
	return rightest.values()


# Creating the root node
bst = Node(1)

# Building left sub-tree
bst.left = Node(3)
bst.left.left = Node(4)
bst.left.left.left = Node(7)
bst.left.left.left.left = Node(8)
bst.left.right = Node(5)
bst.right = Node(9)
bst.right.right = Node(10)
bst.right.right.left = Node(11)
bst.right.right.right = Node(12)
print(rightest_elems(bst))
