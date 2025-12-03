"""
Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
(This make it easy to sum from the back to the front or from the lower digits to higher digits)
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

      2->4->3
    + 5->6->4
    = 7->0->8

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, lst1, lst2):
        return self.addTwoNumbersRecursive(lst1, lst2, 0)
        # return self.addTwoNumbersIterative(l1, l2)

    def addTwoNumbersRecursive(self, lst1, lst2, carry_over):
        # Calculate Value
        val = lst1.val + lst2.val + carry_over

        # Floor division to obtain carry over
        carry_over = val // 10

        # Mod the value to obtain the single digit
        ret = Node(val % 10)

        # If at least of the lists has another node
        # Continue the recursion
        if lst1.next is not None or lst2.next is not None:
            if not lst1.next:
                lst1.next = Node(0)
            if not lst2.next:
                lst2.next = Node(0)
            ret.next = self.addTwoNumbersRecursive(lst1.next, lst2.next, carry_over)

        # Otherwise, check if there is any carry_over from the last operation that needs to be included
        # If so, add the carry_over as a new node
        elif carry_over:
            ret.next = Node(carry_over)
        return ret

    def addTwoNumbersIterative(self, lst1, lst2):
        a = lst1
        b = lst2
        c = 0
        ret = current = None

        while a or b:
            val = a.val + b.val + c
            c = val // 10
            if not current:
                ret = current = Node(val % 10)
            else:
                current.next = Node(val % 10)
                current = current.next

            if a.next or b.next:
                if not a.next:
                    a.next = Node(0)
                if not b.next:
                    b.next = Node(0)
            elif c:
                current.next = Node(c)
            a = a.next
            b = b.next
        return ret


l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

answer = Solution().addTwoNumbers(l1, l2)
line = ""
while answer:
    link = ''
    if answer.next:
        link = '->'
    else:
        link = ''
    line += str(answer.val) + link
    answer = answer.next
print(line)
# 7 0 8