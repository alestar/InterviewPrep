"""
2300. Successful Pairs of Spells and Potions - Difficulty: Medium

You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.



Example 1:

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.
Example 2:

Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
- 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful.
- 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful.
Thus, [2,0,2] is returned.


"""

def successful_pairs(spells, potions, success):
    from bisect import bisect_left # Importing bisect_left for binary search

    potions.sort()
    n = len(potions)
    result = []

    for spell in spells:
        required_potion_strength = (success + spell - 1) // spell  # Ceiling division
        index = bisect_left(potions, required_potion_strength) # Find the first index where potion strength >= required using bisect_left, which is more efficient
         # Calculate the number of successful pairs
        successful_count = n - index
        result.append(successful_count)

    return result

def successful_pairs_two_pointer(spells, potions, success):
    potions.sort()
    n = len(potions)
    result = []

    for spell in spells:
        left, right = 0, n - 1
        index = n  # Default to n if no potion is found. Index is used to track the first successful potion

        while left <= right:
            mid = left + (right - left) // 2
            if spell * potions[mid] >= success:
                index = mid # Update index with the leftmost successful potion, if there is more than one. If there is only one, it will be mid.
                right = mid - 1
            else:
                left = mid + 1

        successful_count = n - index
        result.append(successful_count)

    return result

# Example usage:
spells1 = [5, 1, 3]
potions1 = [1, 2, 3, 4, 5]
success1 = 7
print(successful_pairs(spells1, potions1, success1))  # Output: [4, 0, 3]
print(successful_pairs_two_pointer(spells1, potions1, success1))  # Output: [4, 0, 3]

# Example 2:
spells2 = [3, 1, 2]
potions2 = [8, 5, 8]
success2 = 16
print(successful_pairs(spells2, potions2, success2))  # Output: [2, 0, 2]
print(successful_pairs_two_pointer(spells2, potions2, success2))  # Output: [2, 0, 2]