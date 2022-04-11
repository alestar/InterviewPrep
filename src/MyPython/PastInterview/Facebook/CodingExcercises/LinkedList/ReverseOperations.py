"""
Reverse Operations

You are given a singly-linked list that contains N integers. A subpart of the list is a contiguous set of even elements, bordered either by either end of the list or an odd element. For example, if the list is [1, 2, 8, 9, 12, 16], the subparts of the list are [2, 8] and [12, 16].
Then, for each subpart, the order of the elements is reversed. In the example, this would result in the new list, [1, 8, 2, 9, 16, 12].
The goal of this question is: given a resulting list, determine the original order of the elements.

Implementation detail:
You must use the following definition for elements in the linked list:
class Node {
	int data;
	Node next;
}
Signature
Node reverse(Node head)
Constraints
1 <= N <= 1000, where N is the size of the list
1 <= Li <= 10^9, where Li is the ith element of the list
Example
Input:
N = 6
list = [1, 2, 8, 9, 12, 16]
Output:
[1, 8, 2, 9, 16, 12]

"""

class Node:
	def __init__(self, x):
		self.data = x
		self.next = None


def reverse(head):
	# Write your code here
	node = head

	evens = []

	while node is not None:
		is_even = node.data % 2 == 0
		if is_even:  # even, start pushing
			# Add to the stack of even number subpart
			evens.append(node)

		if not is_even or node.next is None:  # not even, start popping
			while len(evens) > 1:

				# Swap the values instead of the pointers itself
				evens[0].data, evens[-1].data = evens[-1].data, evens[0].data

				# pop two even elements at a time to swap their values
				evens.pop(0)
				evens.pop(-1)
			# Clear the stack when done with a subpart
			evens.clear()
		node = node.next
	return head

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.


def printLinkedList(head):
	print('[', end='')
	while head is not None:
		print(head.data, end='')
		head = head.next
		if head is not None:
			print(' ', end='')
	print(']', end='')


test_case_number = 1


def check(expected_head, output_head):
	global test_case_number
	temp_expected_head = expected_head
	temp_output_head = output_head
	result = True
	while expected_head is not None and output_head is not None:
		result &= (expected_head.data == output_head.data)
		expected_head = expected_head.next
		output_head = output_head.next

	if not (output_head is None and expected_head is None):
		result = False

	right_tick = '\u2713'
	wrong_tick = '\u2717'
	if result:
		print(right_tick, ' Test #', test_case_number, sep='')
	else:
		print(wrong_tick, ' Test #', test_case_number, ': Expected ', sep='', end='')
		printLinkedList(temp_expected_head)
		print(' Your output: ', end='')
		printLinkedList(temp_output_head)
		print()
	test_case_number += 1


def create_linked_list(arr):
	head = None
	temp_head = head
	for v in arr:
		if head is None:
			head = Node(v)
			temp_head = head
		else:
			head.next = Node(v)
			head = head.next
	return temp_head


if __name__ == "__main__":
	head_1 = create_linked_list([1, 2, 8, 9, 12, 16])
	expected_1 = create_linked_list([1, 8, 2, 9, 16, 12])
	output_1 = reverse(head_1)
	check(expected_1, output_1)

	head_2 = create_linked_list([2, 18, 24, 3, 5, 7, 9, 6, 12])
	expected_2 = create_linked_list([24, 18, 2, 3, 5, 7, 9, 12, 6])
	output_2 = reverse(head_2)
	check(expected_2, output_2)
