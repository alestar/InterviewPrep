class Solution:
    def find_repeat(self, numbers):
        floor = 1
        ceiling = len(numbers) - 1

        while floor < ceiling:
            # Divide our range 1..n into an upper range and lower range
            # (such that they don't overlap)
            # Lower range is floor..midpoint
            # Upper range is midpoint+1..ceiling
            midpoint = floor + ((ceiling - floor) // 2)
            lower_range_floor, lower_range_ceiling = floor, midpoint
            upper_range_floor, upper_range_ceiling = midpoint+1, ceiling

            # Count number of items in lower range
            items_in_lower_range = 0
            for item in numbers:
                # Is it in the lower range?
                if item >= lower_range_floor and item <= lower_range_ceiling:
                    items_in_lower_range += 1

            distinct_possible_integers_in_lower_range = (
                    lower_range_ceiling
                    - lower_range_floor
                    + 1
            )
            if items_in_lower_range > distinct_possible_integers_in_lower_range:
                # There must be a duplicate in the lower range
                # so use the same approach iteratively on that range
                floor, ceiling = lower_range_floor, lower_range_ceiling
            else:
                # There must be a duplicate in the upper range
                # so use the same approach iteratively on that range
                floor, ceiling = upper_range_floor, upper_range_ceiling

        # Floor and ceiling have converged
        # We found a number that repeats!
        return floor


arr0 = [6, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
arr1 = [6, 5, 1, 3, 2, 2, 2]
arr2 = [6, 4, 1, 1, 2, 2, 1]

print(Solution().find_repeat(arr0))
# 6
print(Solution().find_repeat(arr1))
# 2
print(Solution().find_repeat(arr2))
# 1
