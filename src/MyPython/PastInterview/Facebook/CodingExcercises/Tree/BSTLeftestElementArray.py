"""
Number of Visible Nodes
There is a binary tree with N nodes. You are viewing the tree from its left side and can see only the leftmost nodes at each level. Return the number of visible nodes.
Note: You can see only the leftmost nodes, but that doesn't mean they have to be left nodes. The leftmost node at a level could be a right node.
Signature
int visibleNodes(Node root) {
Input
The root node of a tree, where the number of nodes is between 1 and 1000, and the value of each node is between 0 and 1,000,000,000
Output
An int representing the number of visible nodes.

Example 1:
   8 <----  8  <------ root
           / \
   3 <-- 3    10
        / \     \
  1 <- 1   6     14
          / \    /
  4 <--- 4  7  13

Output: 4
Explanation: [8,3,1,4]

Example 2:
     1 <---- 1
            / \
     3 <-- 3  9
          /\   \
    4 <- 4 5  10
        /      /  \
  7 <- 7     11  12
      /
8 <- 8

Output: 5
Explanation: [1,3,4,7,8]
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
def leftest_elems(node):
	if not node:
		return

	# Use a Queue for node that has not been visited yet and are pending to explore
	queue = deque()
	queue.append((0, node))
	leftest = {0: node.value}

	while queue:
		depth, curr_node = queue.popleft()
		leftest[depth] = curr_node.value

		if curr_node.right:
			queue.append((depth + 1, curr_node.right))
		if curr_node.left:
			queue.append((depth + 1, curr_node.left))
	print("Leftest dic: " + str(leftest))
	return leftest.values()


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
print(leftest_elems(bst))
