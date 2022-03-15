"""
Swap Every Two nodes in a Linked List

Given a linked list, swap the position of every 2 nodes ( i.e: the 1st and 2nd node, then swap the position of 3rd and 4th etc.)

***  Hint on restriction ***:
	Values can be swapped in the nodes instead of the nodes itself

"""


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def __repr__(self):
		return f"{self.value} -> {self.next.__repr__()}"


def swap_every_two(linked_list):
	head = linked_list
	curr = head

	while curr is not None and curr.next is not None:
		curr.value, curr.next.value = curr.next.value, curr.value  # Swap values
		curr = curr.next.next  # jump 2 positions from initial to check the next pair (if available)

	return head


linked_list_1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
linked_list_2 = Node(2, Node(1, Node(4, Node(3, Node(5)))))
linked_list_3 = Node(1, Node(1, Node(2, Node(2, Node(3)))))

print("Input:  " + str(linked_list_1))
print("Output: " + str(swap_every_two(linked_list_1)))
print("Input:  " + str(linked_list_2))
print("Output: " + str(swap_every_two(linked_list_2)))
print("Input:  " + str(linked_list_3))
print("Output: " + str(swap_every_two(linked_list_3)))
