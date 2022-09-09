"""
Remove Zero Sum Consecutive Nodes from Linked List

Share
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no s
uch sequences.
After doing so, return the head of the final linked list.  You may return any such answer.

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.

Example 2:
Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]

Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.

"""

import collections


class Node(object):
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

	def __repr__(self):
		return f"{self.val} -> {self.next.__repr__()}"

	# def __repr__(self):
	# 	n = self
	# 	ret = ''
	# 	while n:
	# 		ret += str(n.val) + '->'
	# 		n = n.next
	# 	return ret


class Solution(object):
	def remove_zero_sum_sublists(self, node):
		prefix_sums = collections.OrderedDict()
		accumulated_sum = 0

		# Use a dummy node to avoid deleting the list in case the head node gets removed
		# This guarantees the consistency of the list
		curr = dummy = Node(0)
		dummy.next = node

		# Traverse all the nodes of the Linked List
		while curr:
			accumulated_sum += curr.val

			# If is a new sum not seen so far
			# Then, added it to the dictionary
			if accumulated_sum not in prefix_sums:
				prefix_sums[accumulated_sum] = curr

			# Otherwise, if the accumulated sum reach repeated or the same val of previous state
			# Then, that means that the elems in between that cancel each other (add up to 0)
			# Hence, the accumulated sum went back to the initial prev state
			else:
				prev = prefix_sums[accumulated_sum]

				# Update the pointers to skip the in between elems that add to zero sum
				prev.next = curr.next

				# Proceed to removed all the previous in between elems that add to zero sum
				# Until accumulated ir reach the previous accumulated sum state item
				while list(prefix_sums.keys())[-1] != accumulated_sum:
					prefix_sums.popitem()

			# Move to the next Linked Node
			curr = curr.next

		# Finally, return the next of the dummy node
		return dummy.next


# 3, 1, 2, -1, -2, 4, 1
n = Node(3)
n.next = Node(1)
n.next.next = Node(2)
n.next.next.next = Node(-1)
n.next.next.next.next = Node(-2)
n.next.next.next.next.next = Node(4)
n.next.next.next.next.next.next = Node(1)
print(Solution().remove_zero_sum_sublists(n))
# 3, 4, 1
