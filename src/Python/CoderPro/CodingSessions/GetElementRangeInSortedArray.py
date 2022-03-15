"""
Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""


class Solution:
    def getRange(self, arr, target):
        first = self.binary_search_iter(arr, 0, len(arr) - 1, target, True)
        last = self.binary_search_iter(arr, 0, len(arr) - 1, target, False)
        # Little optimization to find second element from the first one
        # Using it as the lower bound for binary search
        # last = self.binary_search_iter(arr, first, len(arr) - 1, target, False)
        return [first, last]

    def binary_search_recur(self, arr, low, high, target, find_first):
        if high < low:
            return -1
        mid = low + (high - low) // 2
        if find_first:
            if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                return mid
            if target > arr[mid]:
                return self.binary_search_recur(arr, mid + 1, high, target, find_first)
            else:
                return self.binary_search_recur(arr, low, mid - 1, target, find_first)
        else:
            if (mid == len(arr)-1 or target < arr[mid + 1]) and arr[mid] == target:
                return mid
            elif target < arr[mid]:
                return self.binary_search_recur(arr, low, mid - 1, target, find_first)
            else:
                return self.binary_search_recur(arr, mid + 1, high, target, find_first)

    def binary_search_iter(self, arr, low, high, target, find_first):
        while True:
            if high < low:
                return -1
            mid = low + (high - low) // 2
            if find_first:
                if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                    return mid
                if target > arr[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if (mid == len(arr)-1 or target < arr[mid + 1]) and arr[mid] == target:
                    return mid
                elif target < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1


a = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
t = 9
print("Looking range for target : '" + str(t) + "' in array: " + str(a))
print("Range is : " + str(Solution().getRange(a, t)))  # [6, 8]
