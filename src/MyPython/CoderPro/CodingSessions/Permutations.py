"""
Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]


Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
Accepted
1,095,122
Submissions
1,528,739

"""
class Solution(object):
    def _permuteHelper(self, nums, start=0):
        print('***************************')
        print('Enter recur call: ')
        # When there are more numbers to iterate
        # Return the current arrays of nums (curr permutation)
        # as a list of list
        if start == len(nums) - 1:
            print(" Since start: '" + str(start) + "' == " + "len(nums) - 1 : '" + str(len(nums) - 1) + "'")
            print('Exit recur call')
            print('***************************')
            return [nums[:]]

        result = []
        for i in range(start, len(nums)):
            print(' ++++++++++++++++++++++++++')
            print(' Start iteration: ')
            print('   i: ' + str(i))
            print('   start: ' + str(start))
            print("   nums (before swap): " + str(nums))

            # Step 1: Swap to create a different permutation with a different 'start'
            nums[start], nums[i] = nums[i], nums[start]
            print("   nums (after swap): " + str(nums))

            # Step 2: Store the results of recursive call,
            # with 'start' pointing to the next position
            # and with prev position swapped
            result += self._permuteHelper(nums, start + 1)
            print('    Came back from recur call')

            # swap back so in the next iter, other permutation can be created by swapping the original value
            nums[start], nums[i] = nums[i], nums[start]
            print("   nums (after swap back): " + str(nums))
            print(' Finish iteration')
            print(' ++++++++++++++++++++++++++')
        print('Exist Loop')
        print('_________________________')
        print("Final result (for this recur): " + str(result))
        return result

    def permute_recur(self, nums):
        return self._permuteHelper(nums)

    def permute_recur2(self, nums, values=[]):
        if not nums:
            return [values]
        result = []
        for i in range(len(nums)):
            # Continue recur with the rest of the number but excluding the current number in use,
            # Also insert the current ith number to the to permuted values that we are constructing
            result += self.permute_recur2(nums[:i] + nums[i + 1:], values + [nums[i]])
        return result

    def permute_iter(self, nums):
        results = []
        stack = [(nums, [])]
        while len(stack):
            nums, values = stack.pop()
            if not nums:
                results += [values]
            for i in range(len(nums)):
                stack.append((nums[:i]+nums[i+1:], values+[nums[i]]))
        return results


Solution().permute_recur([1, 2, 3])
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

print(Solution().permute_recur2([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
# i = 0
# nums [1, 2, 3]
# (i = 0)                     0   1 (i = 1)
# values[1] ,  nums [2,3] -> [2] [3] ,
# values[1,2], nums [3]   -> values[1, 3], nums[2]
# values[1, 2, 3], nums[] -> values [1, 3, 2],

# i = 1
# nums [1, 2, 3]
# (i = 0)                     0   1 (i = 1)
# values[2] ,  nums [1,3] -> [1] [3] ,
# values[2,1], nums [3]   -> values[2, 3], nums[1]
# values[2, 1, 3], nums[] -> values [2, 3, 1],

# i = 2
# nums [1, 2, 3]
# (i = 0)                     0   1 (i = 1)
# values[3] ,  nums [1,2] -> [1] [2] ,
# values[3,1], nums [2]   -> values[3, 2], nums[1]
# values[3, 1, 2], nums[] -> values [3, 2, 1],


print(Solution().permute_iter([1, 2, 3]))
# [[3, 2, 1], [3, 1, 2], [2, 3, 1], [2, 1, 3], [1, 3, 2], [1, 2, 3]]
