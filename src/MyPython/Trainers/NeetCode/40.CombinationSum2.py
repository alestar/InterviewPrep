"""
40. Combination Sum II  - Difficulty: Medium

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]

Time Complexity: O(2^n) in the worst case, where n is the number of candidates. This is because each candidate can either be included or excluded from a combination. Why? Because we have to explore all possible combinations to ensure we find all unique sets that sum to the target. How? Through backtracking, we explore each candidate and decide whether to include it in the current combination or not, while also skipping duplicates to avoid redundant combinations.

Space Complexity: O(k) where k is the maximum depth of the recursion tree, which in the worst case can be O(n) if all candidates are included in a combination. Why? Because of the space used by the recursion stack during backtracking. How? Each recursive call adds a new layer to the stack, and in the worst case, we might have to go as deep as the number of candidates if they all contribute to a valid combination.

"""
def combination_sum_2(candidates, target):
    candidates.sort()  # Sort to handle duplicates easily
    result = []

    def backtrack(remaining, combination, start):
        if remaining == 0:
            result.append(list(combination))
            return
        elif remaining < 0:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue  # Skip duplicates

            combination.append(candidates[i])  # Choose the candidate
            backtrack(remaining - candidates[i], combination, i + 1)  # Move to the next index
            combination.pop()  # Backtrack

    backtrack(target, [], 0)
    return result

def combination_sum_2_dp(candidates, target):
    candidates.sort()
    dp = [[] for _ in range(target + 1)]
    dp[0] = [[]]  # Base case

    for candidate in candidates: # Iterate through candidates
        for t in range(target, candidate - 1, -1): # Go backwards to avoid using the same element multiple times
            for combination in dp[t - candidate]: # Existing combinations that sum to (t - candidate)
                if combination and candidate < combination[-1]: # if the last element is greater than candidate
                    continue  # Ensure combinations are in non-decreasing order
                dp[t].append(combination + [candidate]) # Add candidate to the combination

    # Remove duplicates
    unique_combinations = set(tuple(sorted(comb)) for comb in dp[target])
    return [list(comb) for comb in unique_combinations]

def combination_dfs(candidates, target):
    candidates.sort()
    res = []
    n = len(candidates)

    def dfs(i, cur, total=None):
        if total == target: # Found a valid combination
            res.append(cur[:])
            return
        if total > target or i == n: # Out of bounds
            return

        # Include candidates[i]
        cur.append(candidates[i])
        dfs(i + 1, cur, total + candidates[i]) # Move to next index
        cur.pop() # Backtrack or exclude  candidates[i]
        while i + 1 < n and candidates[i] == candidates[i + 1]:  # Skip duplicates, until a different number is found
            i += 1
        dfs(i + 1, cur, total) # Move to next index with candidates[i] excluded

    dfs(0,  [], 0)
    return res

# Example1 usage:
candidates = [10,1,2,7,6,1,5]
target = 8
print(combination_sum_2(candidates, target))  # Output: [[1,1,6], [1,2,5], [1,7], [2,6]]
print(combination_sum_2_dp(candidates, target))  # Output: [[1,1,6], [1,2,5], [1,7], [2,6]]
print(combination_dfs(candidates, target))  # Output: [[1,1,6], [1,2,5], [1,7], [2,6]]