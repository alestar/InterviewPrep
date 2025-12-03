"""
5. Longest Palindromic Substring  - Difficulty: Medium

Given a string s, return the longest palindromic substring in s (Hint: 'longest palindromic substring' is equal to the 'longest common subsequence' substring for both original and reverse of original string).

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

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

def longest_palindromic_substring_reversing(s):
    rev_s = s[::-1]
    return longest_common_subsequence(s, rev_s)



def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

def longest_palindromic_substring(s):
    if len(s) == 0:
        return ""

    start = 0
    end = 0

    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)   # Odd length palindromes
        len2 = expand_around_center(s, i, i + 1) # Even length palindromes
        max_len = max(len1, len2)

        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]

"""
Dynamic Programming approach to find the length of the longest palindromic subsequence.
Time Complexity: O(n^2)
Why? Because we are filling a 2D table of size n x n.
Space Complexity: O(n^2) for the DP table
Why? Because we are using a 2D table to store results of subproblems.
"""
def lps_length(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for cl in range(2, n + 1): # 'cl' is the length of substring, from 2 to n
        for i in range(n - cl + 1): # 'i' is the starting index
            j = i + cl - 1 #  j is the ending index
            if s[i] == s[j] and cl == 2: # two characters match
                dp[i][j] = 2 # count both characters
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2 # characters match, increment count and move inward
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j]) # characters do not match, take max from left or right

    return dp[0][n - 1]

"""
Recursive approach with memoization to find the length of the longest palindromic subsequence.
Time Complexity: O(n^2) 
Why? Because we are filling a 2D table of size n x n.
Space Complexity: O(n^2) for memoization table
Why? Because we are using a 2D table to store results of subproblems.

"""
def lps_recursive(s):

    n =len(s)
    memo=[[0] * n for _ in range(n)]

    def helper(i, j):
        if i > j:
            return 0
        if i == j:
            return 1

        if memo[i][j] != 0: # already computed
            return memo[i][j]

        if s[i] == s[j]: # characters match
            memo[i][j] = 2 + helper(i + 1, j - 1) # increment count and move inward
        else: # characters do not match
            memo[i][j] = max(helper(i + 1, j), helper(i, j - 1)) # take max from left or right
        return memo[i][j]
    return helper(0, len(s) - 1)

def longestPalindromicSubseq(s: str) -> int:
   cache ={}

   def dfs(l,r):
       if (l,r) in cache: # already computed
           return cache[(l,r)]
       if l>r: # invalid case,Why? because left index crossed right index
           return 0
       if l==r: # single character is always palindrome. Why? because same character
           return 1
       if s[l]==s[r]: # characters match. Why? because same character
           cache[(l,r)] = 2 + dfs(l+1,r-1) # increment count and move inward, How much? 2 for both characters, plus whatever is inside
       else:
           cache[(l,r)] = max(dfs(l+1,r),dfs(l,r-1)) # characters do not match, take max from left or right
       return cache[(l,r)]
   return dfs(0,len(s)-1)



s1 = "babad"
s2 = "cbbd"
print(longest_palindromic_substring(s1))  # Output: "bab" or "aba"
print(longest_palindromic_substring(s2))  # Output: "bb"
print(longest_palindromic_substring_reversing(s1)) # Output: 3
print(longest_palindromic_substring_reversing(s2)) # Output: 2

s3 = "a"
s4 = "ac"
print(longest_palindromic_substring(s3))  # Output: "a"
print(longest_palindromic_substring(s4))  # Output: "a"
s5 = "forgeeksskeegfor"
print(longest_palindromic_substring(s5))  # Output: "geeksskeeg"
s6 = "abccba"
print(longest_palindromic_substring(s6))  # Output: "abccba"
print(longest_palindromic_substring_reversing(s6))  # Output: "abccba"
s7 = "bbbab"
print(longest_palindromic_substring(s7))  # Output: "bbbb"
s8 = "aabxycbaa"
print(s8)
print(longest_palindromic_substring(s8))  # Output: "aabbaa"
print(longest_palindromic_substring_reversing(s8))
print(lps_length(s8))
print(lps_recursive(s8))
print(longestPalindromicSubseq(s8))
