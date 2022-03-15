"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
1<=ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

from collections import defaultdict


class Solution(object):
    def can_spell(self, magazine, ransom_note):
        letters = defaultdict(int)
        for c in magazine:
            letters[c] += 1

        for c in ransom_note:
            if letters[c] <= 0:
                return False
            letters[c] -= 1

        return True


print(Solution().can_spell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
# True

print(Solution().can_spell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
# False
