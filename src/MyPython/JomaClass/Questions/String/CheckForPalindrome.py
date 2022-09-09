from collections import defaultdict


def find_palindrome(str):
	char_counts = defaultdict(int)

	for c in str:
		char_counts[c] += 1

	pal = ''
	odd_char = ''
	for c, cnt in char_counts.items():
		# Construct the first half of the palindrome
		# by adding the even counts letters to the palindrome half
		if cnt % 2 == 0:
			pal += c * (cnt // 2)

		# If the count is not even
		# then, it must be the odd letter
		# which is safe
		# and the rest of the count is added to the palindrome half
		elif odd_char == '':
			odd_char = c
			pal += c * (cnt // 2)
		else:
			return False
	return pal + odd_char + pal[::-1]


print(find_palindrome('foxfo'))
# foxof

print(find_palindrome('mommo'))
# momom

print(find_palindrome('qqaaao'))
# False
