"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


def length_longest_substring(str):
	letter_pos = {}
	start = -1
	end = 0
	max_length = 0

	while end < len(str):
		c = str[end]
		# Scenario (1):
		# If other repeated letters cause the start idx to move ahead
		# Then, the last pos that 'c' that was spotted, is behind the current start idx
		# Therefore, start idx will keep current value, since is not relevant what is behind start idx.

		# Scenario (2):
		# If 'c' is a new occurrence of a repeated letter,
		# Then, the repeated letter position should be ahead of start idx
		# And therefore, start idx should be updated with the pos of the new repeated letter 'c'.

		# Conclusion:
		# start index will always be updated with the max (most rightest) pos value
		if c in letter_pos:
			# Update star index
			start = max(start, letter_pos[c])

		# Update max_length for each iteration, since end idx is moving (start idx may move too)
		max_length = max(max_length, end - start)

		# Update hte last pos current letter 'c' was saw, with the curr pos of pointer end
		letter_pos[c] = end

		# Update the moving pointer end
		end += 1

	return max_length


print(length_longest_substring('aabcbbeacc'))