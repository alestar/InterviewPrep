"""
Matching Pairs

Given two strings s and t of length N, find the maximum number of possible matching pairs in strings s and t after swapping exactly two characters within s.
A swap is switching s[i] and s[j], where s[i] and s[j] denotes the character that is present at the ith and jth index of s, respectively.
The matching pairs of the two strings are defined as the number of indices for which s[i] and t[i] are equal.
Note: This means you must swap two characters at different indices.

Signature
int matchingPairs(String s, String t)
Input:
-s and t are strings of length N
-N is between 2 and 1,000,000
Output:
Return an integer denoting the maximum number of matching pairs

Example 1
s = "abcd"
t = "adcb"
output = 4
Explanation:
Using 0-based indexing, and with i = 1 and j = 3, s[1] and s[3] can be swapped, making it  "adcb".
Therefore, the number of matching pairs of s and t will be 4.

Example 2
s = "mno"
t = "mno"
output = 1
Explanation:
Two indices have to be swapped, regardless of which two it is, only one letter will remain the same.
If i = 0 and j=1, s[0] and s[1] are swapped, making s = "nmo", which shares only "o" with t.
"""

def matching_pairs(s, t):
	# CHECK FOR VALID INPUT
	if len(s) != len(t):
		raise ValueError(f"Strings have different lengths.")
	if len(s) < 2:
		raise ValueError(f"Length of strings {len(s)} precludes a swap being possible.")

	# CHECK FOR MATCHING STRINGS
	if s == t:
		if contains_repeat_char(s):
			# any repeated characters can be swapped with impunity
			return len(s)
		else:
			# must impose a swap, which reduces matches
			return len(s) - 2

	# TRAVERSE THE STRINGS
	# Count the matching pairs while saving data about the pairs for a potential swap later
	misses = set()  # non-matching pairs
	pairs = set()  # the swap pool
	base = 0  # pre-swap count of matching pairs

	for si, ti in zip(s, t):
		pairs.add((si, ti))
		if si == ti:
			base += 1
			pairs.add((si, True))  # matched pair swap candidate
		else:
			misses.add((si, ti))
			pairs.add((si, False))  # unmatched pair swap candidate

	# CHECK FOR SPECIFIC MISSES THAT CAN BE SWAPPED
	# CHECK THEM IN SERIAL ORDER BECAUSE EACH SWAP TYPES IMPACT THE MATCH COUNT DIFFERENTLY

	# Check for a swap that creates two new matches: eg. pre-swap s='ab', t='ba'; after swap s='ba'
	for m in misses:
		if (m[1], m[0]) in pairs:
			return base + 2
	# Check for a swap that creates one new match: eg. pre-swap s='at', t='xa'; after swap s='ta'
	for m in misses:
		if (m[1], False) in pairs:
			return base + 1
	# Check for a swap that breaks an existing match while creating a new one: eg. pre-swap s='ab', t='aa'; after swap s='ba'
	for m in misses:
		if (m[1], True) in pairs:
			return base

	# CHECK FOR REPEATED CHARACTERS IN 's', which can be swapped with impunity
	if contains_repeat_char(s):
		return base

	# IMPOSE A SWAP
	# 2 indices that both contain misses can be swapped with impunity
	if len(misses) >= 2:
		return base

	# swapping an index that has a miss with an index that has a match removes a match
	if len(misses) == 1 and base >= 1:
		return base - 1

	# else, swap indexes of two matching pairs, which removes both matches
	return base - 2


def contains_repeat_char(str):
	used = set()
	for c in str:
		if c in used:
			return True
		else:
			used.add(c)
	return False


assert matching_pairs('abcd', 'abcd') == 2
assert matching_pairs('abcde', 'adcbe') == 5

assert matching_pairs('aa', 'aa') == 2
assert matching_pairs('aa', 'bb') == 0

assert matching_pairs('at', 'at') == 0
assert matching_pairs('at', 'ta') == 2
assert matching_pairs('ax', 'ya') == 1

assert matching_pairs('ax', 'aa') == 1
assert matching_pairs('aa', 'ax') == 1

assert matching_pairs('abx', 'abb') == 2
assert matching_pairs('abb', 'axb') == 2

assert matching_pairs('ax', 'ay') == 0
assert matching_pairs('axb', 'ayb') == 1

assert matching_pairs('ABC', 'ADB') == 2
assert matching_pairs('abcde', 'axcbe') == 4
assert matching_pairs('docomo', 'docomo') == 6

assert matching_pairs('abcdc', 'baccd') == 3
assert matching_pairs('abcdx', 'abxcc') == 4

assert matching_pairs('abcd', 'adcb') == 4
assert matching_pairs('mno', 'mno') == 1
assert matching_pairs('abcde', 'adcbe') == 5

assert matching_pairs('abcd', 'abcd') == 2
assert matching_pairs('abcd', 'efgh') == 0
assert matching_pairs('abcd', 'abce') == 2
assert matching_pairs('abczz', 'abcee') == 3
assert matching_pairs('abc', 'abd') == 1
assert matching_pairs('mnode', 'mnoef') == 4

assert matching_pairs('abxce', 'abcdx') == 3
assert matching_pairs('dd', 'dd') == 2

print("All tests passed!")
