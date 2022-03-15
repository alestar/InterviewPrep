"""
You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order).
Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.
Reconstruct and return the queue that is represented by the input array people.
The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

Example 1:
Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.

Example 2:
Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

Constraints:
1 <= people.length <= 2000
0 <= hi <= 106
0 <= ki < people.length
It is guaranteed that the queue can be reconstructed.
"""


class Solution:
	def reconstruct_queue_sorted(self, people):
		print(people)
		# Sort input list by two order criteria:
		#  (1) - height of the person <descending> (tallest to shortest)
		#  (2) - If height is equal, then sort by how many people k, they see in front <ascending> (lesser to grater)
		# Used negative number to reverse the ascending order into descending, when sorting by heights.
		people.sort(key=lambda x: (-x[0], x[1]))
		res = []
		print(people)

		# Iterate through the now sorted by height descending people list
		# and insert each person in the kth index that represents the amount of people/element they see at most in front of them.

		# (1) By continuously inserting the next tallest people first, guarantees that:
		# 	Inserting smaller people afterwards does not affect the order of the taller people previously inserted,
		#   neither affects the amount of people those next tallest people see 'at most', in front of them.
		#   Hence, that is why is ordered by height first.

		# (2) By continuously inserting in k order (ascending), at the kth index, guarantees that:
		# 	Inserting the person with lesser value k first, will have 'at most' k people (it could be less, but not more)
		# 	equal or taller from prev insertions in front of them,
		#
		# (3) By performing insertion sort and shifting of all elements one position to the right from the element inserted guarantees:
		# 	Both previous conditions are meet and does not affect the order of the people behind them. prev inserted.
		for p in people:
			res.insert(p[1], p)
		return res


people_list1 = [[7, 0], [4, 4], [4, 1], [7, 1], [5, 0], [6, 4], [5, 2], [5, 3], [6, 2]]
print(Solution().reconstruct_queue_sorted(people_list1))
print("---------------------------------------------------")
# Output:
# [[7, 0], [4, 4], [4, 1], [7, 1], [5, 0], [6, 1], [5, 2], [5, 3], [6, 2]]
# [[7, 0], [7, 1], [6, 1], [6, 2], [5, 0], [5, 2], [5, 3], [4, 1], [4, 4]]
# [[5, 0], [4, 1], [7, 0], [5, 2], [4, 4], [5, 3], [6, 1], [6, 2], [7, 1]]

people_list2 = [[7, 0], [4, 4], [4, 1], [7, 1], [4, 3], [5, 0], [6, 1], [5, 2], [5, 3], [6, 2], [7, 3], [7, 100]]
print(Solution().reconstruct_queue_sorted(people_list2))
print("---------------------------------------------------")
# Output:
# [[7, 0], [4, 4], [4, 1], [7, 1], [4, 3], [5, 0], [6, 1], [5, 2], [5, 3], [6, 2], [7, 3], [7, 100]]
# [[7, 0], [7, 1], [7, 3], [7, 100], [6, 1], [6, 2], [5, 0], [5, 2], [5, 3], [4, 1], [4, 3], [4, 4]]
# [[5, 0], [4, 1], [7, 0], [4, 3], [4, 4], [5, 2], [5, 3], [6, 1], [6, 2], [7, 1], [7, 3], [7, 100]]

people_list1 = [[7, 0], [4, 4], [4, 1]]
print(Solution().reconstruct_queue_sorted(people_list1))
print("---------------------------------------------------")
# Output:
# [[7, 0], [4, 4], [4, 1]]
# [[7, 0], [4, 1], [4, 4]]
# [[7, 0], [4, 1], [4, 4]]
