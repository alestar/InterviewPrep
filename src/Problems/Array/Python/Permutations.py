class Solution(object):
    def _permuteHelper(self, nums, start=0):
        if start == len(nums) - 1:
            return [nums[:]]

        result = []
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start] # swap to create a different permutation with a different 'start'
            result += self._permuteHelper(nums, start + 1)# store the results of recursive call with 'start' pointing to the next position and with prev position swaped
            nums[start], nums[i] = nums[i], nums[start] #swap back so in the next iter, other permutation can be created by swaping the original value
        return result

    def permute(self, nums):
        return self._permuteHelper(nums)

    def permute2(self, nums, values=[]):
        if not nums:
            return [values]
        result = []
        for i in range(len(nums)):
            result += self.permute2(nums[:i] + nums[i+1:], values + [nums[i]]) # Pass the rest of the number but excluding the current number in use, also insert the current ith number to the to values that we are constructing
        return result

    def permute2Iterative(self, nums):
        results = []
        stack = [(nums, [])]
        while len(stack):
            nums, values = stack.pop()
            if not nums:
                results += [values]
            for i in range(len(nums)):
                stack.append((nums[:i]+nums[i+1:], values+[nums[i]]))
        return results


print(Solution().permute([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

print(Solution().permute2([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

print(Solution().permute2Iterative([1, 2, 3]))
# [[3, 2, 1], [3, 1, 2], [2, 3, 1], [2, 1, 3], [1, 3, 2], [1, 2, 3]]