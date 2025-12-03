"""
39. Combination Sum  - Difficulty: Medium

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40

Time Complexity: O(2^n) in the worst case, where n is the number of candidates. This is because each candidate can either be included or excluded from a combination.

Space Complexity: O(k) where k is the maximum depth of the recursion tree, which in the worst case can be O(n) if all candidates are included in a combination. 
"""
def combination_sum(candidates, target):
    result = []

    def backtrack(remaining, combination, start):
        if remaining == 0:
            result.append(list(combination))
            return
        elif remaining < 0:
            return

        for i in range(start, len(candidates)): # Allow the same element to be reused
            combination.append(candidates[i]) # Choose the candidate
            backtrack(remaining - candidates[i], combination, i) # Not i + 1 because we can reuse the same element
            combination.pop() # Backtrack

    backtrack(target, [], 0)
    return result

def combination_sum_dp(candidates, target):
    dp = [[] for _ in range(target + 1)] # dp[i] will hold all combinations that sum up to i
    dp[0] = [[]]  # Base case: one way to make target 0

    for t in range(1, target + 1):
        for candidate in candidates:
            if t - candidate >= 0:
                for combination in dp[t - candidate]:
                    dp[t].append(combination + [candidate])

    return dp[target]

def combination_sum_dp_unique(candidates, target):
    dp = [[] for _ in range(target + 1)] # dp[i] will hold all combinations that sum up to i
    dp[0] = [[]]  # Base case: one way to make target 0

    for candidate in candidates: # Iterate over candidates first to avoid duplicates
        for t in range(candidate, target + 1): # Start from candidate to target
            for combination in dp[t - candidate]: # Get combinations that sum to t - candidate
                dp[t].append(combination + [candidate]) # Append current candidate

    return dp[target]

def combination_dfs(candidates, target):
    res = []

    def dfs(i, cur, total):
        if total == target:
            res.append(cur[:]) # Create a copy of current combination
            return
        if i>= len(candidates) or total > target: # Out of bounds or exceeded target
                return

        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])  # Include the candidate
        cur.pop() # Backtrack
        dfs(i + 1, cur, total)  # Exclude the candidate

    dfs(0, [], 0)
    return res

# Example usage:
candidates = [2, 3, 6, 7]
target = 7
print(combination_sum(candidates, target))  # Output: [[2, 2, 3], [7]]
print(combination_sum_dp(candidates, target))  # Output: [[2, 2, 3], [7]]
print(combination_sum_dp_unique(candidates, target))  # Output: [[2, 2, 3], [7]]
print(combination_dfs(candidates, target))  # Output: [[2, 2, 3], [7]]
