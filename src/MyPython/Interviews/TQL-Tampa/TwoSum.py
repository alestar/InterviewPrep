"""
Two Sum
Easy
Topics
premium lock icon
Companies
Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

"""
def two_sum_brute_force(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # In case there is no solution, though the problem guarantees one exists

def two_sum_set(nums, target):
    seen = set()
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [nums.index(complement), index]
        seen.add(num)
    return []  # In case there is no solution, though the problem guarantees one exists

def two_sum_dict(nums, target):
    num_to_index = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index

    return []  # In case there is no solution, though the problem guarantees one exists

def two_sum_two_pointer(nums, target):
    nums_with_indices = [(num, index) for index, num in enumerate(nums)]
    nums_with_indices.sort()  # Sort based on the numbers

    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums_with_indices[left][0] + nums_with_indices[right][0] #

        if current_sum == target:
            return [nums_with_indices[left][1], nums_with_indices[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []  # In case there is no solution, though the problem guarantees one exists



# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(two_sum_brute_force(nums, target))  # Output: [0, 1]
print(two_sum_set(nums, target))          # Output: [0, 1]
print(two_sum_dict(nums, target))              # Output: [0, 1]
print(two_sum_two_pointer(nums, target))  # Output: [0, 1]

# Example 2:
nums = [3, 2, 4]
target = 6
print(two_sum_brute_force(nums, target))  # Output: [1, 2]
print(two_sum_set(nums, target))          # Output: [1, 2]
print(two_sum_dict(nums, target))              # Output: [1, 2]
print(two_sum_two_pointer(nums, target))  # Output: [1, 2]

# Example 3:
nums = [3, 3]
target = 6
print(two_sum_brute_force(nums, target))  # Output: [0, 1]
print(two_sum_set(nums, target))          # Output: [0, 1]
print(two_sum_dict(nums, target))              # Output: [0, 1]
print(two_sum_two_pointer(nums, target))  # Output: [0, 1]

# Example 4:
nums = [1, 2, 3, 4, 5]
target = 8
print(two_sum_brute_force(nums, target))  # Output: [2, 4]
print(two_sum_set(nums, target))          # Output: [2, 4]
print(two_sum_dict(nums, target))              # Output: [2, 4]
print(two_sum_two_pointer(nums, target))  # Output: [2, 4]

# Example 5:
nums = [-1, 0, 1, 2]
target = 1
print(two_sum_brute_force(nums, target))  # Output: [0, 3]
print(two_sum_set(nums, target))          # Output: [1, 2]
print(two_sum_dict(nums, target))              # Output: [1, 2]
print(two_sum_two_pointer(nums, target))  # Output: [0, 3]

#Example 6:
nums = [0, 4, 3, 0]
target = 0
print(two_sum_brute_force(nums, target))  # Output: [0, 3]
print(two_sum_set(nums, target))          # Output: [0, 3]
print(two_sum_dict(nums, target))              # Output: [0, 3]
print(two_sum_two_pointer(nums, target))  # Output: [0, 3]

#Example 7:
nums = [5, 75, 25]
target = 100
print(two_sum_brute_force(nums, target))  # Output: [1, 2]
print(two_sum_set(nums, target))          # Output: [1, 2]
print(two_sum_dict(nums, target))              # Output: [1, 2]
print(two_sum_two_pointer(nums, target))  # Output: [1, 2]

#Example 8:
nums = [3, 3, 4, 4]
target = 7
print(two_sum_brute_force(nums, target))  # Output: [0, 2]
print(two_sum_set(nums, target))          # Output: [0, 2]
print(two_sum_dict(nums, target))              # Output: [1, 2]
print(two_sum_two_pointer(nums, target))  # Output: [0, 3]

#Example 9:
nums = [2,7,11,15]
target = 9
print(two_sum_brute_force(nums, target))  # Output: [0, 1]
print(two_sum_set(nums, target))          # Output: [0, 1]
print(two_sum_dict(nums, target))              # Output: [0, 1]
print(two_sum_two_pointer(nums, target))  # Output: [0, 1]

