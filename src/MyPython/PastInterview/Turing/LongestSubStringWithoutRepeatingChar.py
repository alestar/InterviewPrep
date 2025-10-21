"""
Given a string s, find the length of the longest substring without duplicate characters.

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


def longest_substr_without_repeat_char_set(s):
    longest_value=0
    l_index=0
    r_index=0
    result=[]
    observed = set()

    while r_index < len(s):
        c=s[r_index]
        if c in observed:
            observed.remove(c)
            l_index +=1
        else:
            observed.add(c)
            longest_value = max(longest_value, r_index-l_index + 1)
            result=s[l_index:r_index]
        r_index +=1
    return  result,longest_value

def longest_substr_without_repeat_char_array(s):
    longest_value=0
    l_index=0
    r_index=0
    result=[]
    observed = [0]*128  # Assuming ASCII

    while r_index < len(s):
        c=s[r_index]
        l_index = max(observed[ord(c)], l_index)
        longest_value = max(longest_value, r_index-l_index + 1)
        observed[ord(c)] = r_index + 1
        r_index+=1
        result=s[l_index:r_index]
    return  result,longest_value


    # if observed[ord(c)] == 1:
    #         observed[ord(s[l_index])] = 0
    #         l_index +=1
    #     else:
    #         observed[ord(c)] = 1
    #         longest_value = max(longest_value, r_index-l_index + 1)
    #         result=s[l_index:r_index+1]
    #     r_index +=1
    # return  result,longest_value


def run_tests():
    # print(longest_substr_without_repeat_char_set("abcabcbb"))  # Expected: ('abc', 3) or similar
    # print(longest_substr_without_repeat_char_set("bbbbb"))  # Expected: ('b', 1) or similar
    # print(longest_substr_without_repeat_char_set("pwwkew"))  # Expected: ('wke', 3) or similar
    # print(longest_substr_without_repeat_char_set(""))  # Expected: ('', 0)
    # print(longest_substr_without_repeat_char_set("a"))  # Expected: ('a', 1)
    # print(longest_substr_without_repeat_char_set("abcdef"))  # Expected: ('abcdef', 6)

    print(longest_substr_without_repeat_char_array("abcabcbb"))  # Expected: ('abc', 3) or similar
    print(longest_substr_without_repeat_char_array("bbbbb"))  # Expected: ('b', 1) or similar
    print(longest_substr_without_repeat_char_array("pwwkew"))  # Expected: ('wke', 3) or similar
    print(longest_substr_without_repeat_char_array(""))  # Expected: ('', 0)
    print(longest_substr_without_repeat_char_array("a"))  # Expected: ('a', 1)
    print(longest_substr_without_repeat_char_array("abcdef"))  # Expected: ('abcdef', 6)

if __name__ == "__main__":
    run_tests()