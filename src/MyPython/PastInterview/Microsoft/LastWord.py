"""
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.


Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.

"""


def last_word_from_start(str):
	new_word = False
	word_size = 0
	curr_word_size = 0

	for i in range(len(str)):
		c = str[i]
		if c == " ":
			new_word = False
			if curr_word_size > 0:
				word_size = curr_word_size
				curr_word_size = 0
			continue
		else:
			if not new_word:
				new_word = True
			curr_word_size += 1

	if curr_word_size > 0:
		word_size = curr_word_size
	return word_size


def last_word_from_end(str):
	s = str.strip()
	print(s)
	c = s[-1]
	i = len(s) - 1
	last_w = ""
	while c != " " and i >= 0:
		c = s[i]
		if c == " ":
			print(last_w)
			print(last_w[::-1])  # Print reversed
			return len(last_w)
		last_w += c
		i -= 1


# print(last_word_from_start("Hello World"))
# print(last_word_from_start("fly me   to   the moon  "))
# print(last_word_from_start("luffy is still joyboy"))
print(last_word_from_end("Hello World"))
print(last_word_from_end("fly me   to   the moon  "))
print(last_word_from_end("luffy is still joyboy"))
