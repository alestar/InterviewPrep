"""

Validate parenthesis correct expression

Explame 1:
Input: "(()(()))" -> Correct Expression
Output: "(()(()))" - > Return same string

Example 2:
Input: "(()(())))))" -> Incorrect Expression
Output: "(()(()))" - > Return string with extra parenthesis removed

"())))))))))))))))))))))" -> ()
"((((((((((((((((((((()" -> ()

"""


def validate_parenthesis(s):
	open_stack = []
	open_set = set('({[')
	close_set = set(')}]')
	res = ''
	# Traverse the entire string to check each character
	for i in range(len(s)):
		elem = s[i]

		# If the current char is an open elem
		# Then push it to the stack
		if elem in open_set:
			open_stack.append((i, elem))
			res += elem

		# If the current char is a close elem
		# Then proceed to inspect the stack of open elems
		# To determine if there is an open elem match for it
		elif elem in close_set:

			# If there is an open elem in the stack
			# Then, there is a match
			# Therefore, pop from the stack
			# and include the close elem in the res
			if open_stack:
				res += elem
				open_stack.pop()

		# If is neither open or closing element continue to the next
		else:
			continue

	# When the loop is completed
	# If the open elem stack is not empty
	# Then pop the remaining elems and removed them from the res
	while open_stack:
		# print(open_stack)
		pos, open_symbol = open_stack.pop()
		res = res[:pos] + res[pos + 1:]

	if len(res) == 1:
		res = ''

	if res == '':
		return None
	else:
		return res


print(validate_parenthesis("(()(()))"))  # (()(())))
print(validate_parenthesis("(()(())))))"))  # (()(())))
print(validate_parenthesis("())))))))))))))))))))))"))  # ()
print(validate_parenthesis("((((((((((((((((((((()"))  # ()
print(validate_parenthesis("))))"))  # None
print(validate_parenthesis("((((("))  # None
print(validate_parenthesis(")((((("))  # None
print(validate_parenthesis("))))("))  # None
