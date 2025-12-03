"""
The storage drive isn't being used efficiently because the data is scattered across many partitions.
Each partition has some space already used and a maximum capacity. The goal is to consolidate these partitions to minimize the number of partitions used while ensuring that no partition exceeds its maximum capacity.
Rearrange the data so that it takes up the fewest possible partitions. Find the minimum number of partitions needed.

Example:
Input: n=5, used=[3,2,1,3,1], max_capacity=[3,5,3,5,5]
Output: 2
Explanation:
- Combine partitions with used space 3 and 2 into one partition with max capacity 5
- Combine partitions with used space 1, 3, and 1 into another partition with max capacity 5
- Total partitions used = 2

Example 2:
Input: n=3, used=[1,2,3], max_capacity=[3,3,3]
Output: 2
Explanation:
- Combine partitions with used space 1 and 2 into one partition with max capacity 3
- The partition with used space 3 remains as is
"""
def consolidate_partitions(used, max_capacity):
    n= len(used)
    partitions = sorted(zip(used, max_capacity), key=lambda x: x[1])
    count = 0
    i = 0

    while i < n:
        current_used, current_max = partitions[i]
        j = i + 1

        while j < n and current_used + partitions[j][0] <= current_max: # Try to fit as many partitions as possible into the current one
            current_used += partitions[j][0]
            j += 1

        count += 1
        i = j

    return count

def consolidate_partitions_two_pointer(used, max_capacity):
    n= len(used)
    partitions = sorted(zip(used, max_capacity), key=lambda x: x[1])
    count = 0
    left, right = 0, n - 1

    while left <= right:
        if left == right:
            count += 1
            break

        if partitions[left][0] + partitions[right][0] <= partitions[right][1]: #
            left += 1

        count += 1
        right -= 1

    return count

def consolidate_partitions_substr(used, max_capacity):
        n= len(used)
        total_used = 0

        # sum all elements of used
        for u in used:
            total_used += u

        sorted(max_capacity)
        count = 0

        i= n-1
        while total_used > 0 and i >= 0:
            total_used -= max_capacity[i]
            count += 1
            i -= 1
        return count

# Example 1:
n1 = 5
used1 = [3, 2, 1, 3, 1]
max_capacity1 = [3, 5, 3, 5, 5]
#print(consolidate_partitions(used1, max_capacity1))  # Output: 2
#print(consolidate_partitions_two_pointer(used1, max_capacity1))  # Output: 2
print(consolidate_partitions_substr( used1, max_capacity1))  # Output: 2

# Example 2:
n2 = 3
used2 = [1, 2, 3]
max_capacity2 = [3, 3, 3]
#print(consolidate_partitions(used2, max_capacity2))  # Output: 2
#print(consolidate_partitions_two_pointer(used2, max_capacity2))  # Output: 2
print(consolidate_partitions_substr( used2, max_capacity2))  # Output: 2