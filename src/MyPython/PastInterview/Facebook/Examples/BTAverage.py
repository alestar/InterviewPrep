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
 - Level 0: 4 , because is only 4
 - Level 1: 7 + 9  = 16 / 2 = 8
 - Level 2: 10 + 2 + 6  = 18 / 3 = 6
 - Level 3: 6 , because is only 6
 - Level 4: 2 , because is only 4

"""


class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __repr__(self):
		return f"(node: {self.value}, l: {self.left}, r: {self.right})"


def _collect1(node, data, depth=0):
	if not node:
		return None

	if depth not in data:
		data[depth] = []
	data[depth].append(node.value)

	_collect1(node.left, data, depth + 1)
	_collect1(node.right, data, depth + 1)


def avg_by_depth1(node):
	data = {}
	_collect1(node, data)

	result = []
	i = 0
	while i in data:
		nums = data[i]
		avg = sum(nums) / len(nums)
		result.append(avg)
		i += 1
	return result


def _collect2(node, data, depth=0):
	if not node:
		return None

	if depth not in data:
		data[depth] = (node.val, 1)

	val, count = data[depth]
	val += node.val
	count += 1
	data[depth] = (val, count)

	_collect2(node.left, data, depth + 1)
	_collect2(node.right, data, depth + 1)


def avg_by_depth2(node):
	data = {}
	_collect1(node, data)

	result = []
	i = 0
	while i in data:
		val, count = data[i]
		result.append(val / count)
		i += 1
	return result


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
