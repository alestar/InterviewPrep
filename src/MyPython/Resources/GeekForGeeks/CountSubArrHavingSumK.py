"""
Given an array arr[] of positive and negative integers, the objective is to find the number of  <<continuous>> subarrays having a sum exactly equal to a given number k.

Examples:

Input : arr[] = [10, 2, -2, -20, 10], k = -10
Output : 3
Explanation: Subarrays: arr[0...3], arr[1...4], arr[3...4] have sum equal to -10.

Input : arr[] = [9, 4, 20, 3, 10, 5], k = 33
Output : 2
Explanation: Subarrays: arr[0...2], arr[2...4] have sum equal to 33.

Input : arr[] = [1, 3, 5], k = 2
Output : 0
Explanation: No subarrays with 0 sum.
"""
def count_subarrays_with_sum_k(arr, k):
    count = 0
    current_sum = 0
    prefix_sum = {0: 1}  # To handle the case when subarray starts from index 0

    for num in arr:
        current_sum += num
        if (current_sum - k) in prefix_sum:# Check if there is a prefix subarray with sum equal to current_sum - k
            count += prefix_sum[current_sum - k]# If current_sum - k exists in prefix_sum, it means there are prefix_sum[current_sum - k] subarrays ending at the current index that sum up to k
        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1 # Update the frequency of the current sum

    return count
# Example usage:
arr = [10, 2, -2, -20, 10]
k = -10
print(count_subarrays_with_sum_k(arr, k))  # Output: 3

# Example 2:
arr = [9, 4, 20, 3, 10, 5]
k = 33
print(count_subarrays_with_sum_k(arr, k))  # Output: 2