"""
Given a binary tree, get the average value at each level of the tree

Input:
		 4
		/ \
	   7   9
	  / \   \
	 10  2   6
		 \
		  6
		 /
		2

Output: [4, 8 ,6 ,6 ,2]

Explanation:
- Level 0: 4, because is only 4
- Level 1: 7 + 9  = 16 / 2 = 8
- Level 2: 10 + 2 + 6  = 18 / 3 = 6
- Level 3: 6 , because is only 6
- Level 4: 2 , because is only 4

"""
from collections import deque


class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __repr__(self):
		return f"(node: {self.value}, l: {self.left}, r: {self.right})"


# Collect all the elements at a certain depth,  by traversing DFS
def _collect_elems_dfs(node, data, depth=0):
	if not node:
		return None

	if depth not in data:
		data[depth] = []
	data[depth].append(node.value)

	_collect_elems_dfs(node.left, data, depth + 1)
	_collect_elems_dfs(node.right, data, depth + 1)


# Collect the sums and counts of elements at a certain depth, by traversing DFS
def _collect_sum_counts_dfs(node, data, depth=0):
	if not node:
		return None
	calc_sum_counts_at_depth(data, depth, node)
	_collect_sum_counts_dfs(node.left, data, depth + 1)
	_collect_sum_counts_dfs(node.right, data, depth + 1)


# Collect the sums and counts of elements at a certain depth,
def _collect_sums_counts_bfs(node, data):
	if not node:
		return

	# Use a Queue for node that has not been visited yet and are pending to explore
	queue = deque()
	queue.append((0, node))

	while queue:
		depth, curr_node = queue.popleft()
		calc_sum_counts_at_depth(data, depth, curr_node)
		if curr_node.left:
			queue.append((depth + 1, curr_node.left))
		if curr_node.right:
			queue.append((depth + 1, curr_node.right))
	return data


# Use the collected elements to added them and calculate the avg (not space efficient)
def calc_avg_by_depth_elems(node):
	data = {}
	_collect_elems_dfs(node, data)

	result = []
	i = 0
	while i in data:
		nums = data[i]
		avg = sum(nums) / len(nums)
		result.append(avg)
		i += 1
	return result


# Calculate the avg directly using sum and counts
def calc_avg_by_depth_sum(node):
	data = {}
	_collect_sum_counts_dfs(node, data)
	return calc_avg(data)


# Use Sum to calculate average them to calculate the avg (more space efficient)
def calc_avg_by_depth_sum_bfs(node):
	data = {}
	_collect_sums_counts_bfs(node, data)
	return calc_avg(data)


# Calculate sums and counts of elements in the tree at a certain depth
def calc_sum_counts_at_depth(data, depth, node):
	if depth not in data:
		data[depth] = (node.value, 1)
	else:
		val, count = data[depth]
		val += node.value
		count += 1
		data[depth] = (val, count)


# Calculate average after traversing the tree and collect date
def calc_avg(data):
	res = []
	for key in data:
		val, count = data[key]
		res.append(val / count)
	return res


def bt_avg(node):
	res = []
	dic = {}
	bt_avg_calc_recur(node, dic, 0)

	for val in dic.values():
		res.append(val[0] / val[1])
	return res


def bt_avg_calc_recur(node, dic, lvl):
	if not node:
		return None

	if lvl in dic:
		val = dic[lvl]
		val[0] += node.value
		val[1] += 1
	else:
		val = [0] * 2
		val[0] = node.value
		val[1] += 1
		dic[lvl] = val

	bt_avg_calc_recur(node.left, dic, lvl + 1)
	bt_avg_calc_recur(node.right, dic, lvl + 1)


bt = Node(4)
bt.left = Node(7)
bt.left.left = Node(10)
bt.left.right = Node(2)
bt.left.right.right = Node(6)
bt.left.right.right.left = Node(2)
bt.right = Node(9)
bt.right.right = Node(6)

print(bt_avg(bt))
print(calc_avg_by_depth_elems(bt))
print(calc_avg_by_depth_sum(bt))
print(calc_avg_by_depth_sum_bfs(bt))
