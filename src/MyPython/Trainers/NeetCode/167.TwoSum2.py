"""
167. Two Sum II - Input Array Is Sorted - Difficulty: Medium

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

"""

def two_sum_2_pointers(num, target):

    left,right =0,len(num)-1
    while left < right:

        curr_sum= num[left] + num[right]

        if curr_sum == target:
            return [left + 1, right + 1]
        elif curr_sum < target :
            left+=1
        else:
            right-=1
    return []

def two_sum_binary_search(numbers, target):
    def binary_search(left, right, target):
        while left <= right:
            mid = left + (right - left) // 2
            if numbers[mid] == target:
                return mid
            elif numbers[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    n = len(numbers)
    for i in range(n):
        complement = target - numbers[i]
        j = binary_search(i + 1, n - 1, complement)
        if j != -1:
            return [i + 1, j + 1]  # Return 1-indexed positions
    return []

# Example usage:
numbers = [2, 7, 11, 15]
target = 9
print(two_sum_2_pointers(numbers, target))  # Output: [1, 2]
print(two_sum_binary_search(numbers, target))  # Output: [1,  2]

# Example 2:
numbers = [2, 3, 4]
target = 6
print(two_sum_2_pointers(numbers, target))  # Output: [1, 3]
print(two_sum_binary_search(numbers, target))  # Output: [1, 3]





