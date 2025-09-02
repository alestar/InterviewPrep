"""
Given string s, return the most frquent char (an alphabete letter) in the string ss.

Examples:

Input: s = 'abcddefda11113333'
Output: 'd'
Explanation: 'd' occurs 3 times in the string

Input: s = 'AA0AB0BB00CCC0AA0AW00WS0BBBW123123'
Output: 'B'
Explanation: 'B' occurs 6 times in the string
"""

def most_repeated_char_dict(s):
    char_count ={}
    max_count = 0
    most_repeated = ''

    for c in s:
        if c.isalpha():
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1
            if char_count[c] > max_count:
                max_count = char_count[c]
                most_repeated = c
       # raise Exception("Error: No alphabetic characters in the string")
    return most_repeated

def most_repeated_char_iterative(s):
    max_count = 0
    most_repeated = ''
    for i in range(len(s)):
        if s[i].isalpha():
            occurrence = 0
            for j in range(i,len(s)):
                if s[i] == s[j]:
                    occurrence+=1
            if occurrence > max_count:
                max_count=occurrence
                most_repeated= s[i]
    return most_repeated


print(most_repeated_char_dict('abcddefda11113333'))  # Output: 'd'
print(most_repeated_char_dict('AA0AB0BB00CCC0aa0aW00WS0BBBW123123'))  # Output: 'B'
print(most_repeated_char_dict('aAaaBBbbCcC'))  # Output: 'a' or 'A' or 'b' or 'B' or 'c' or 'C' (all occur 3 times)
print(most_repeated_char_dict('1234567890!@#$%^&*()'))  # Output: '' (no alphabetic characters)

print(most_repeated_char_iterative('abcddefda11113333'))  # Output: 'd'
print(most_repeated_char_iterative('AA0AB0BB00CCC0aa0aW00WS0BBBW123123'))  # Output: 'B'
print(most_repeated_char_iterative('aAaaBBbbCcC'))  # Output: 'a' or 'A' or 'b' or 'B' or 'c' or 'C' (all occur 3 times)
print(most_repeated_char_iterative('1234567890!@#$%^&*()'))  # Output: '' (no alphabetic characters)