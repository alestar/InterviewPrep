"""
Arithmetic Expression Tree

You are given a binary tree representation of an arithmetic expression. In this tree, each leaf is an interger value,
and a non-leaf node is one of the four operation: '+', '-',  '*',  '/'

Write a function that takes this tree and evaluates the expression.

Example:
      *
    /   \
   +     +
  / \   / \
 3  2  4  5

This is a representation of the expression (3 + 2) * (4 + 5) =  45

"""


class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def evaluate(node):
	operators = {
		'+': lambda a, b: a + b,
		'-': lambda a, b: a - b,
		'/': lambda a, b: a / b,
		'*': lambda a, b: a * b,
	}

	if not node:
		return 0

	if node.value in operators:
		fn = operators[node.value]
		return fn(evaluate(node.left), evaluate(node.right))
	else:
		return node.value



node = Node('*')
node.left = Node('+')
node.right = Node('+')
node.left.left = Node(3)
node.left.right = Node(2)
node.right.left = Node(4)
node.right.right = Node(5)

print(evaluate(node))  # 45
