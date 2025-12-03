"""
Two strings are anagrams if they contain the same characters with the same frequencies. For example "bat" and "tab" are anagrams, while "bat" and "tabb" are not.

Given a list of strings, group the anagrams together and return the number of such groups.

Example:
Suppose there are n=5 words: words = ["cat","listen,"silent","kitten","salient"]
Output: 4

Explanation:
Only silent and listen are anagrams. The last word 'salient' contains an extra 'a' compared to 'silent' and 'listen'.

Therefore, there are 4 groups of anagrams:
1. ["cat"]
2. ["listen", "silent"]
3. ["kitten"]
4. ["salient"]

"""

def group_anagrams(words):
    anagram_set = set()

    for w in words:
        sorted_word = ''.join(sorted(w)) # Sort the word to create a key for anagram grouping
        if sorted_word not in anagram_set:
            anagram_set.add(sorted_word)

    # The number of unique keys in the set is the number of anagram groups
    return len(anagram_set)

# Example usage:
words = ["cat","listen","silent","kitten","salient"]
print(group_anagrams(words))  # Output: 4 Explanation: The anagram groups are ["cat"], ["listen","silent"], ["kitten"], and ["salient"]

#Example 2:
words = ["bat","tab","eat","tea","tan","nat","bat"]
print(group_anagrams(words))  # Output: 3 Explanation: The anagram groups are ["bat","tab"], ["eat","tea"], and ["tan","nat"]