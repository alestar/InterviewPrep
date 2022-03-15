"""
Distribute Bonuses

You are the manager of a a number of employees who all sit in a row.
The CEO would like to give bonuses to all of your employees, but since the company did not perform so well this year, the CEO would like to keep the bonus to a minimum.

The rules of giving bonuses is that:
	- Each employee begins with a bonus factor 1x.
	- For each employee, of they perform better than the person sitting next to them, the employee is given +1 higher bonus,
	and up to +2 if they perform better than both people to their sides.

Given a lis t of employee's performance, find the bonus each employee should get.

Example 1:
	Input: [1,2,3,2,3,5,1]
	Output: [1,2,3,1,2,3,1]

Example 2:
	Input: [1,2,3,4,3,1]
	Output: [1,2,3,4,2,1]

Example 3:
	Input: [4,3,2,1]
	Output: [1,2,3,4,2,1]

"""


def dist_bonuses(performances):
	n = len(performances)
	bonuses = [1] * n

	for i in range(1, n):  # traverse and looking at the left neighbor
		if performances[i-1] < performances[i]:  # Compare with left neighbor
			bonuses[i] = bonuses[i-1] + 1  # Assign the current bonus of left neighbor plus one.

	for i in range(n - 2, -1, -1):  # traverse and looking at the right neighbor
		if performances[i + 1] < performances[i]:  # Compare with right neighbor
			bonuses[i] = max(bonuses[i], bonuses[i+1] + 1)  # Assign the MAX bonus between the current and new on if it beats the right neighbor

	return bonuses


print(dist_bonuses([1, 2, 3, 2, 3, 4, 1]))  # [1, 2, 3, 1, 2, 3, 1]
print(dist_bonuses([1, 2, 3, 4, 3, 1]))  # [1, 2, 3, 4, 2, 1]
print(dist_bonuses([4, 3, 2, 1]))  # [4, 3, 2, 1]
