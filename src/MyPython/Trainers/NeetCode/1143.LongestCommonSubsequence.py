"""
1143. Longest Common Subsequence - Difficulty: Medium

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""
def longest_common_subsequence(text1, text2):
    m = len(text1)
    n = len(text2)

    # Create a 2D array to store lengths of longest common subsequence.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the dp array from bottom up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1 # Characters match , increment the count
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # Characters do not match , take max from left or top

    return dp[m][n]
# Example usage:
text1 = "abcde"
text2 = "ace"
print(longest_common_subsequence(text1, text2))  # Output: 3
text1 = "abc"
text2 = "abc"
print(longest_common_subsequence(text1, text2))  # Output: 3
text1 = "abc"
text2 = "def"
print(longest_common_subsequence(text1, text2))  # Output: 0
text1 = "AGGTAB"
text2 = "GXTXAYB"
print(longest_common_subsequence(text1, text2))  # Output: 4 ("GTAB")
