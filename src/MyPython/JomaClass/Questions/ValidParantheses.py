"""
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
	def is_valid_paranthesis(self, s):
		p_stack = []
		for c in s:
			if c == '(':
				p_stack.append('(')
			elif c == ')':
				if not p_stack:
					return False
				elif p_stack[-1] != '(':
					return False
				else:
					p_stack.pop()
			elif c == '{':
				p_stack.append('{')
			elif c == '}':
				if not p_stack:
					return False
				elif p_stack[-1] != '{':
					return False
				else:
					p_stack.pop()
			elif c == '[':
				p_stack.append('[')
			elif c == ']':
				if not p_stack:
					return False
				elif p_stack[-1] != '[':
					return False
				else:
					p_stack.pop()
		if not p_stack:
			return True
		else:
			return False


s = Solution()
print(s.is_valid_paranthesis("()"))  # True
print(s.is_valid_paranthesis("()[]{}"))  # True
print(s.is_valid_paranthesis("(]"))  # False
print(s.is_valid_paranthesis("{[({})]()}"))  # True
