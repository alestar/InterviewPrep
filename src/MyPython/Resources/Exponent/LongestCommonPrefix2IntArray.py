"""
Find the longest common prefix given two integer arrays.

Example1:
Input: arr1 = [1,2,3,4], arr2 = [1,2,5,6]
Output: [1,2]

Example2:
Input: arr1 = [7,8,9], arr2 = [1,2,3]
Output: []

Constraints:
1 <= len(arr1), len(arr2) <= 1000
-10^9 <= arr1[i], arr2[i] <= 10^9
arr1 and arr2 consist of integers.
arr1 and arr2 may have different lengths.
arr1 and arr2 may be empty.
arr1 and arr2 may not have any common prefix.
arr1 and arr2 may be identical.
arr1 and arr2 may contain negative integers.
arr1 and arr2 may contain duplicate integers.
arr1 and arr2 may contain zero.
arr1 and arr2 may contain large integers.
arr1 and arr2 doesn't have to be sorted.

"""
def longest_common_prefix(arr1, arr2):
    min_length = min(len(arr1), len(arr2))
    common_prefix = []

    for i in range(min_length):
        if arr1[i] == arr2[i]:
            common_prefix.append(arr1[i])
        else:
            break

    return common_prefix

# Example usage:
arr1 = [1, 2, 3, 4]
arr2 = [1, 2, 5, 6]
print(longest_common_prefix(arr1, arr2))  # Output: [1, 2]

#Example 2:
arr1 = [7, 8, 9]
arr2 = [1, 2, 3]
print(longest_common_prefix(arr1, arr2))  # Output: []

#Example 3:
arr1 = [5, 6, 7, 8]
arr2 = [5, 6, 7, 9, 10]
print(longest_common_prefix(arr1, arr2))  # Output: [5, 6, 7]

#Example 4:
arr1 = [10, 20, 30]
arr2 = [10, 20, 30, 40, 50]
print(longest_common_prefix(arr1, arr2))  # Output: [10, 20, 30]
#Example 5:
arr1 = [1, 3, 2]
arr2 = [1, 3, 4]
print(longest_common_prefix(arr1, arr2))  # Output: [1, 3]
