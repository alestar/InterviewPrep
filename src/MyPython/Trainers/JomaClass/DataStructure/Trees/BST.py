class BSTNode:
	def __init__(self, value=None):
		self.value = value
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.value)


class BST:
	def __init__(self, root_node=None):
		self.root = root_node

	def insert_node_recur_helper(self, curr, value):
		if curr is None:
			return BSTNode(value)
		else:
			if curr.value == value:
				return None
			if curr.value > value:
				curr.left = self.insert_node_recur_helper(curr.left, value)
			elif curr.value < value:
				curr.right = self.insert_node_recur_helper(curr.right, value)
		return curr

	def insert_node_recur(self, value):
		return self.insert_node_recur_helper(self.root, value)

	# Iterative function to insert a key into a BST
	def insert_node_iter(self, val):
		# start from the node
		curr = self.root

		# pointer to store the parent of the current node
		parent = None

		# if the tree is empty, create a new node and set it as root
		if node is None:
			return BSTNode(val)

		# traverse the tree and find the parent node of the given key
		while curr:
			# update the parent to the current node
			parent = curr

			# if the given key is less than the current node,
			# go to the left subtree; otherwise, go to the right subtree.
			if val < curr.value:
				curr = curr.left
			else:
				curr = curr.right

		# construct a node and assign it to the appropriate parent pointer
		if val < parent.value:
			parent.left = BSTNode(val)
		else:
			parent.right = BSTNode(val)

		return node

	def delete(self, node, val):
		# if node doesn't exist, just return it
		if node is None:
			return node
		# Find the node in the left subtree	if key value is less than node value
		if val < node.value:
			if node.left:
				node.left = self.delete(node.left, val)
			return node
		# Find the node in right subtree if key value is greater than root value
		elif val > node.value:
			if node.right:
				node.right = self.delete(node.right, val)
			return node
		# Case 3: Delete the node if root.value == key
		else:
			# If there is no right children delete the node and new node would be node.left
			if node.right is None:
				return node.left
			# If there is no left children delete the node and new node would be node.right
			elif node.left is None:
				return node.right

			# If both left and right children exist in the node replace its value with
			# the minimum value in the right subtree. Now delete that minimum node
			# in the right subtree
			min_larger_node = node.right
			while min_larger_node.left:
				min_larger_node = min_larger_node.left
			node.value = min_larger_node.value  # Replace
			node.right = self.delete(node.right, min_larger_node.value)  # Delete
		return node

	def inorder(self, node):
		if node:
			self.inorder(node.left)
			print(node.value)
			self.inorder(node.right)

	def inorder_traverse_using_stack(self):
		curr = self.root
		stack = [curr]
		curr = curr.left

		while len(stack) >= 0:
			if curr:
				stack.append(curr)
				curr = curr.left
			else:
				curr = stack.pop(0)
				print(curr.value)
				curr = curr.right

	def traverse_pre_order(self, node, lst):
		lst.append(node.value)
		if node.left:
			self.traverse_pre_order(node.left, lst)
		if node.right:
			self.traverse_pre_order(node.right, lst)
		return lst


def traverse_bts(curr):
	current_level = [curr]
	while current_level:
		print(' '.join(str(n) for n in current_level))
		next_level = list()
		for n in current_level:
			if n.left:
				next_level.append(n.left)
			if n.right:
				next_level.append(n.right)
		current_level = next_level


# Driver Code
if __name__ == "__main__":
	node = BSTNode(50)
	bst = BST(node)
	r = bst.insert_node_recur(30)
	r = bst.insert_node_recur_helper(r, 20)
	r = bst.insert_node_recur_helper(r, 40)
	r = bst.insert_node_recur_helper(r, 70)
	traverse_bts(bst.root)
	r = bst.insert_node_recur(60)
	r = bst.insert_node_recur_helper(r, 80)

	bst.insert_node_iter(100)
	bst.insert_node_iter(10)

	# print(bst.traverse_pre_order(bst.root, []))
	traverse_bts(bst.root)
	bst.delete(bst.root, 20)
	traverse_bts(bst.root)
	bst.delete(bst.root, 50)
	traverse_bts(bst.root)
	# bst.inorder_traverse_using_stack()
