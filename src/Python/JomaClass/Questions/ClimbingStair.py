"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45

* This problem is Fibonacci sequence in disguise:
The total numbers of ways/steps to climb n stairs with 1 and 2 jumps is:
- the total numbers of ways of climbing n -1 stairs (with 1 jump)
	+
- the total numbers of ways of climbing n -2 stairs (with 2 jumps)
*
"""


# Traditional recur sol
def stair_case_recur(n):
	if n <= 1:
		return 1
	return stair_case_recur(n - 1) + stair_case_recur(n - 2)  # O(2^n) -> really bad Time Complex


# Using memo dic to optimize prev computations
def stair_case_recur_memo(n):
	memo = {0: 1, 1: 1}
	return stair_case_recur_memo_aux(n, memo)


# Aux that actually recur
def stair_case_recur_memo_aux(n, memo):
	if n in memo:
		return memo[n]
	memo[n] = stair_case_recur_memo_aux(n - 1, memo) + stair_case_recur_memo_aux(n - 2, memo)
	return memo[n]


def stair_case_iter(n):
	if n <= 1:
		return 1

	prev = 1
	prev_prev = 1
	curr = 0

	for i in range(2, n + 1):
		curr = prev + prev_prev

		prev_prev = prev
		prev = curr
	return curr


print(stair_case_recur(0))
print(stair_case_recur_memo(0))
print(stair_case_iter(0))
print(stair_case_recur(1))
print(stair_case_recur_memo(1))
print(stair_case_iter(1))
print(stair_case_recur(5))
print(stair_case_recur_memo(5))
print(stair_case_iter(5))
print(stair_case_recur(10))
print(stair_case_recur_memo(10))
print(stair_case_iter(10))
