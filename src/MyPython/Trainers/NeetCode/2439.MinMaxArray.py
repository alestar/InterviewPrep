"""
2439. Minimize Maximum of Array - Difficulty: Medium

Hint
You are given a 0-indexed array nums comprising n non-negative integers.

In one operation, you must:

Choose an integer i such that 1 <= i < n and nums[i] > 0.
Decrease nums[i] by 1.
Increase nums[i - 1] by 1.
Return the minimum possible value of the maximum integer of nums after performing any number of operations.



Example 1:

Input: nums = [3,7,1,6]
Output: 5
Explanation:
One set of optimal operations is as follows:
1. Choose i = 1, and nums becomes [4,6,1,6].
2. Choose i = 3, and nums becomes [4,6,2,5].
3. Choose i = 1, and nums becomes [5,5,2,5].
The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
Therefore, we return 5.
Example 2:

Input: nums = [10,1]
Output: 10
Explanation:
It is optimal to leave nums as is, and since 10 is the maximum value, we return 10.

Complexity Analysis
Time Complexity: O(n), where n is the length of the input array nums. We traverse the array once to compute the maximum possible value.
Space Complexity: O(1). We use a constant amount of extra space.

"""
def minimize_array_value(nums):
    max_value = 0
    total = 0

    for i in range(len(nums)):
        total += nums[i]
        average = (total + i) // (i + 1)  # Ceiling of the average
        max_value = max(max_value, average)

    return max_value

# Example1:
print(minimize_array_value([3,7,1,6]))  # Output: 5
# Example2:
print(minimize_array_value([10,1]))  # Output: 10
# Example3:
print(minimize_array_value([0,0,0,0]))  # Output: 0
# Example4:
print(minimize_array_value([1,2,3,4,5]))  # Output: 3
# Example5:
print(minimize_array_value([5,4,3,2,1]))  # Output: 5