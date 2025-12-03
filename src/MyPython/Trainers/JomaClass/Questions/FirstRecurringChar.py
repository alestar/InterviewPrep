"""
First Recurring Char

Giving a string, return the first recurring letter that appears. If there is no recurring letters (duplicates), return None.

"""


def first_recurring_character(str):
	seen = set()

	for c in str:
		if c in seen:
			return c
		seen.add(c)

	return None


print(first_recurring_character('qwertty'))  # t
print(first_recurring_character('qwerty'))  # None
