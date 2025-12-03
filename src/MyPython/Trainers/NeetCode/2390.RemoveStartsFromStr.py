"""
2390. Removing Stars From a String - Difficulty: Medium

Hint
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.


Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
Example 2:

Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters and stars *.
The operation above can be performed on s.

"""
def remove_stars(s: str) -> str:
    stack = []

    for c in s:
        if c == '*':
            if stack:
                stack.pop()  # Remove the closest non-star character to the left
        else:
            stack.append(c)  # Add non-star characters to the stack

    return ''.join(stack)  # Join the remaining characters to form the final string

def remove_stars_two_pointer(s: str) -> str:
    s_list = list(s) # Convert string to list for in-place modification
    write_index = 0

    for read_index in range(len(s_list)):
        if s_list[read_index] == '*':
            write_index -= 1  # Move back to remove the closest non-star character
        else:
            s_list[write_index] = s_list[read_index] # Overwrite the character at write_index with the current non-star character
            write_index += 1  # Move forward to add the non-star character

    return ''.join(s_list[:write_index])  # Join the valid part of the list to form the final string. How? by slicing the list up to write_index and joining the characters from that slice. Example

# Example usage:
s1 = "leet**cod*e"
print(remove_stars(s1))  # Output: "lecoe"
print(remove_stars_two_pointer(s1))  # Output: "lecoe"
s2 = "erase*****"
print(remove_stars(s2))  # Output: ""
print(remove_stars_two_pointer(s2))  # Output: ""
s3 = "ab*c*d*e*"
print(remove_stars(s3))  # Output: "a"
print(remove_stars_two_pointer(s3))  # Output: "a"
s4 = "a*b*c*"
print(remove_stars(s4))  # Output: ""
print(remove_stars_two_pointer(s4))  # Output: ""
s5 = "abcde"
print(remove_stars(s5))  # Output: "abcde"
print(remove_stars_two_pointer(s5))  # Output: "abcde"
s6 = "****"
print(remove_stars(s6))  # Output: ""
print(remove_stars_two_pointer(s6))  # Output: ""
s7 = "a**b**c**"
print(remove_stars(s7))  # Output: ""
print(remove_stars_two_pointer(s7))  # Output: ""
s8 = "a*b**c***d"
print(remove_stars(s8))  # Output: "d"
print(remove_stars_two_pointer(s8))  # Output: "d"
s9 = "ab**cd*e**f"
print(remove_stars(s9))  # Output: "f"
print(remove_stars_two_pointer(s9))  # Output: "f"
s10 = "*abc*"
print(remove_stars(s10))  # Output: "bc"
print(remove_stars_two_pointer(s10))  # Output: "bc"