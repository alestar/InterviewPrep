"""
Passing Yearbook


There are n students, numbered from 1 to n, each with their own yearbook. They would like to pass their yearbooks around and get them signed by other students.
You're given a list of n integers arr[1..n], which is guaranteed to be a permutation of 1..n (in other words, it includes the integers from 1 to n exactly once each, in some order). The meaning of this list is described below.
Initially, each student is holding their own yearbook. The students will then repeat the following two steps each minute: Each student i will first sign the yearbook that they're currently holding (which may either belong to themselves or to another student), and then they'll pass it to student arr[i]. It's possible that arr[i] = i for any given i, in which case student i will pass their yearbook back to themselves. Once a student has received their own yearbook back, they will hold on to it and no longer participate in the passing process.
It's guaranteed that, for any possible valid input, each student will eventually receive their own yearbook back and will never end up holding more than one yearbook at a time.
You must compute a list of n integers output, whose ith element is equal to the number of signatures that will be present in student i's yearbook once they receive it back.*

Signature
int[] findSignatureCounts(int[] arr)
Input
n is in the range [1, 100,000].
Each value arr[i] is in the range [1, n], and all values in arr[i] are distinct.
Output
Return a list of n integers output, as described above.

Example 1
n = 2
arr = [2, 1]
output = [2, 2]
The first student will sign their own yearbook and pass it to the second, who will also sign it and pass it back to the first student, resulting in 2 signatures. Meanwhile, the second student's yearbook will similarly be signed both by themselves and then by the first student.

Example 2
n = 2
arr = [1, 2]
output = [1, 1]
Each student will simply pass their yearbook back to themselves, resulting in 1 signature each.
facebook
"""


def find_signature_counts(arr):
	passes = [None] * len(arr)
	for i in range(len(arr)):
		count = 1
		j = arr[i] - 1
		# print(arr[j])
		while j >= 0 and arr[j] != arr[i]:
			count += 1
			j = arr[j] - 1
			# print(arr[j])
		passes[i] = count

	return passes


print(find_signature_counts([1, 2]))  # [1, 1] => 1->1 (1); 2->2 (1)
print(find_signature_counts([2, 1]))  # [2, 2] => 2->1, 1->2 (2); 1->2, 2->1 (2)
print(find_signature_counts([1, 2, 3]))  # [1, 1, 1] => 1->1 (1); 2->2 (1); 3->3 (1)
print(find_signature_counts([1, 3, 2]))  # [1, 2, 2] => 1->1 (1); 3->2, 2->3 (2); 2->3, 3->2 (2)
print(find_signature_counts([2, 1, 3]))  # [2, 2, 1] => 2->1, 1->2 (2); 1->2, 2->1 (2); 3->3 (1)
print(find_signature_counts([2, 3, 1]))  # [3, 3, 3] => 2->3, 3->1, 1->2(3); 3->1, 1->2, 2->3 (3); 1->2, 2->3, 3->1 (3)
print(find_signature_counts([3, 1, 2]))  # [3, 3, 3] => 3->2, 2->1, 1->3 (3); 1->3, 3->2, 2->1 (3); 2->1, 1->3, 3->2 (3)
print(find_signature_counts([3, 2, 1]))  # [2, 1, 2] => 3->1, 1->3 (2); 2->2 (1); 1->3, 3->1 (2)
print(find_signature_counts([1, 2, 3, 4]))  # [1, 1, 1, 1]
print(find_signature_counts([4, 3, 2, 1]))  # [2, 2, 2, 2]
