"""
2405. Optimal Partition of String
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.


Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
Example 2:

Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").
"""
def optimal_partition_string(s: str) -> int:
    substrings_count = 0
    seen_chars = set()

    for char in s:
        if char in seen_chars:
            substrings_count += 1
            seen_chars.clear()
        seen_chars.add(char)

    if seen_chars:
        substrings_count += 1

    return substrings_count

def optimal_partition_string_array(s: str) -> int:
    substrings_count = 0
    seen_chars = [0] * 128  # Assuming ASCII

    for char in s:
        if seen_chars[ord(char)]:
            substrings_count += 1
            seen_chars = [0] * 128  # Reset for new substring
        seen_chars[ord(char)] = 1

    if any(seen_chars):
        substrings_count += 1

    return substrings_count

def optimal_partition_string_bitmask(s: str) -> int: # Using bitmasking for lowercase letters 'a' to 'z' to optimize space
    substrings_count = 0
    bitmask = 0

    for char in s:
        char_bit = 1 << (ord(char) - ord('a')) # Assuming only lowercase letters 'a' to 'z',
        if bitmask & char_bit: # Character already seen in current substring
            substrings_count += 1
            bitmask = 0
        bitmask |= char_bit # Mark character as seen

    if bitmask:
        substrings_count += 1

    return substrings_count

# Example 1:
print(optimal_partition_string("abacaba"))  # Output: 4
# Example 2:
print(optimal_partition_string("ssssss"))  # Output: 6
# Example 3:
print(optimal_partition_string("abcde"))  # Output: 1
# Example 4:
print(optimal_partition_string("aabbcc"))  # Output: 4
# Example 5:
print(optimal_partition_string("abcdabc"))  # Output: 2