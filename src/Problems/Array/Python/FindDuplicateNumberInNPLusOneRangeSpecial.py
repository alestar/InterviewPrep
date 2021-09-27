class Solution:
    def find_duplicate(self, int_list):
        n = len(int_list) - 1

        # STEP 1: GET INSIDE A CYCLE
        # Start at position n+1 and walk n steps to
        # find a position guaranteed to be in a cycle
        position_in_cycle = n + 1
        for _ in range(n):
            position_in_cycle = int_list[position_in_cycle - 1]
            # we subtract 1 from the current position to step ahead:
            # the 2nd *position* in a list is *index* 1

        # STEP 2: FIND THE LENGTH OF THE CYCLE
        # Find the length of the cycle by remembering a position in the cycle
        # and counting the steps it takes to get back to that position
        remembered_position_in_cycle = position_in_cycle
        current_position_in_cycle = int_list[position_in_cycle - 1]  # 1 step ahead
        cycle_step_count = 1

        while current_position_in_cycle != remembered_position_in_cycle:
            current_position_in_cycle = int_list[current_position_in_cycle - 1]
            cycle_step_count += 1

        # STEP 3: FIND THE FIRST NODE OF THE CYCLE
        # Start two pointers
        #   (1) at position n+1
        #   (2) ahead of position n+1 as many steps as the cycle's length
        pointer_start = n + 1
        pointer_ahead = n + 1
        for _ in range(cycle_step_count):
            pointer_ahead = int_list[pointer_ahead - 1]

        # Advance until the pointers are in the same position
        # which is the first node in the cycle
        while pointer_start != pointer_ahead:
            pointer_start = int_list[pointer_start - 1]
            pointer_ahead = int_list[pointer_ahead - 1]

        # Since there are multiple values pointing to the first node
        # in the cycle, its position is a duplicate in our list
        return pointer_start

arr = [6,6,7,8,9,10,1,2,3,4,5]
arr1 = [6,5,1,3,2,2,2]
arr2 = [6,4,1,1,2,2,1]

print(Solution().find_repeat(arr))
# 6
print(Solution().find_repeat(arr1))
# 2
print(Solution().find_repeat(arr2))
# 1
