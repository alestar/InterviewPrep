"""

Square Root of Natural Number

As the title says, we need to find the square root of a number. Let say the number is x, then Sqrt(x) is a number such that Sqrt(x) * Sqrt(x) = x.
If the square root of a number is some decimal value, then we have to return the floor value of the square root.


Approach(Binary Search)
Here, we can apply binary search on a range of numbers starting from 1 going up to x / 2where x = given number.
Here, we implement the binary search on a chosen sorted sequence instead of an array.
Right limit is set as x / 2 because for every number x, greater than 2, the floor of their square root will be less than x / 2.
Depending on the result of the binary search, we can jump to the left or right halves of the original sample space.

Create a binarySearch() function returning floor of sqrt(x)
Initialize variable ans to store the result
If the number is less than 2, return itself
Initialise left and right values as 1 and x / 2 respectively
Until left <= right:
Find middle of this range, mid = left + right / 2
In case square of mid is equal to x,  return it as it is the square root
If square of mid is less than x, jump to the right half by setting left = mid + 1
Otherwise, jump to the left half by setting right = mid – 1 and save this value in ans
Print the result
"""


def sqr_binary_search(x):
	left = 1
	right = x // 2
	mid = -1
	while left <= right:
		mid = left + (right - left) // 2
		sqr = mid * mid
		if sqr == x:
			return mid
		elif sqr < x:
			left = mid + 1
		else:
			right = mid - 1
	if mid * mid != x:
		mid = -1
	return mid


def my_sqrt(x):
	if x <= 1:
		return x
	return sqr_binary_search(x)


print(my_sqrt(9))
print(my_sqrt(16))
print(my_sqrt(25))
print(my_sqrt(36))
print(my_sqrt(0))
print(my_sqrt(1))
print(my_sqrt(2))
print(my_sqrt(3))
print(my_sqrt(5))
print(my_sqrt(10))


