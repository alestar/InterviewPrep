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
	def max_depth_recur(self, node):
		if not node:
			return 0
		return max(self.max_depth_recur(node.left) + 1,
				self.max_depth_recur(node.right) + 1)

	def max_depth_recur2(self, node):
		if not node:
			return 0
		return max(self.max_depth_recur(node.left), self.max_depth_recur(node.right)) + 1

	def max_depth_iter(self, node):
		stack = [(1, node)]

		max_depth = 0
		while stack:
			curr_depth, curr_node = stack.pop()
			if curr_node:
				max_depth = max(max_depth, curr_depth)
				stack.append((curr_depth + 1, curr_node.left))
				stack.append((curr_depth + 1, curr_node.right))
		return max_depth


n = Node(1)
n.left = Node(2)
n.right = Node(3)
n.left.left = Node(4)

print(Solution().max_depth_iter(n))  # 3
print(Solution().max_depth_recur(n))  # 3
print(Solution().max_depth_recur2(n))  # 3

