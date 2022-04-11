"""
Minimum Length Substrings
You are given two strings s and t. You can select any substring of string s and rearrange the characters of the selected substring.
Determine the minimum length of the substring of s such that string t is a substring of the selected substring.
Signature
int minLengthSubstring(String s, String t)

Input
s and t are non-empty strings that contain less than 1,000,000 characters each
Output
Return the minimum length of the substring of s. If it is not possible, return -1

Example
s = "dcbefebce"
t = "fd"
output = 5
Explanation:
Substring "dcbef" can be rearranged to "cfdeb", "cefdb", and so on. String t is a substring of "cfdeb". Thus, the minimum length required is 5.

"""


def min_length_substring(s, t):
	# O(s+t)
	t_len = len(t)
	dic = {}
	for c in t:  # O(t)
		dic[c] = dic.get(c, 0) + 1
	total_len = 0
	index = 0
	for c in s:  # O(s)
		if (c in dic) and (dic[c] > 0):
			dic[c] -= 1
			t_len -= 1
			# there is
			total_len = index
		index += 1
	# Every char is founded
	if t_len > 0:
		return -1
	return total_len + 1


assert min_length_substring("dcbefebce", "fd") == 5
assert min_length_substring("bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf", "cbccfafebccdccebdd") == -1
