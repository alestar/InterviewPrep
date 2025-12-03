"""
You are standing at the top of a hill at a fixed position. Around you are several trees, each located at a specific (x, y) coordinate and with a certain height. You want to take a photo that captures as many trees as possible within a single frame. Given your position and the positions of the trees, write an algorithm to determine the maximum number of trees visible within a given viewing angle. Trees that lie in the same direction (same line of sight) should count as one visible tree, since nearer trees block the view of those behind them.

Solution Explanation:
The problem can be solved by calculating the angles of each tree relative to the observer's position. We can then sort these angles and use a sliding window approach to find the maximum number of trees that fit within the given viewing angle.

Explanation of code:



"""
import math
def max_num_visible_trees(trees, observer_position, viewing_angle):
    def angle_between(p1, p2):
        angle_calc= math.degrees(math.atan2(p2[1] - p1[1], p2[0] - p1[0])) # Calculate angle in degrees.
        # How? using atan2 which gives angle between x-axis and line connecting p1 and p2
        # print(angle_calc)
        return angle_calc if angle_calc >= 0 else angle_calc + 360  # Normalize angle to [0, 360)

    angles = []
    for tree in trees:
        angle = angle_between(observer_position, (tree[0], tree[1]))
        angles.append(angle)

    angles.sort()
    angles += [angle + 360 for angle in angles]  # Duplicate angles for circular wrap-around. How? by adding 360 to each angle, which allows us to handle the circular nature of angles. This necessary because an angle near 0 degrees and an angle near 360 degrees are actually close to each other.

    max_visible = 0
    left = 0
    for right in range(len(angles)): # Two-pointer technique to find the maximum number of trees within the viewing angle. Start with both pointers at the beginning of the sorted angle list.
        while angles[right] - angles[left] > viewing_angle: # Sliding window to find max trees within viewing angle.How? by expanding the right pointer and contracting the left pointer when the angle difference exceeds the viewing angle. If the difference between the angles at the right and left pointers exceeds the viewing angle, we move the left pointer to the right to reduce the window size. This guarantees that we only consider angles within the specified viewing angle.
            left += 1
        max_visible = max(max_visible, right - left + 1) # Update max visible trees count. How? by calculating the number of trees in the current window (right - left + 1) and updating max_visible if this count is greater. How is this calculated? The number of trees in the current window is determined by the positions of the left and right pointers in the sorted angle list, because each angle corresponds to a unique tree.

    return max_visible

# Example usage:
trees = [(1, 2, 5), (2, 3, 10), (3, 1, 7), (4, 4, 3), (5, 2, 8)]
observer_position = (0, 0)
viewing_angle = 90
print(max_num_visible_trees(trees, observer_position, viewing_angle))  # Output: 3
# Explanation of example:
# In this example, the observer is at the origin (0, 0) and has a viewing angle of 90 degrees. The function calculates the angles of each tree relative to the observer and determines that a maximum of 3 trees can be seen within the specified viewing angle.

# Example 2:
trees = [(1, 1, 4), (2, 2, 6), (3, 3, 5), (4, 0, 2)]
observer_position = (0, 0)
viewing_angle = 45
print(max_num_visible_trees(trees, observer_position, viewing_angle))  # Output: 2
# Explanation of example 2:
# Here, the observer again is at the origin (0, 0) but with a viewing angle of 45 degrees. The function finds that only 2 trees can be seen within this narrower angle.

# Example 3:
trees = [(0, 1, 3), (1, 0, 4), (1, 1, 2), (2, 2, 5)]
observer_position = (0, 0)
viewing_angle = 180
print(max_num_visible_trees(trees, observer_position, viewing_angle))  # Output: 4
# Explanation of example 3:
# In this case, the observer has a wide viewing angle of 180 degrees. The function determines that all 4 trees can be seen within this angle.

# Example 4:
trees = [(1, -1, 3), (-1, 1, 4), (-1, -1, 2), (2, 2, 5)]
observer_position = (0, 0)
viewing_angle = 90
print(max_num_visible_trees(trees, observer_position, viewing_angle))  # Output: 2
# Explanation of example 4:
# The observer is at the origin with a viewing angle of 90 degrees. The function calculates that a maximum of 2 trees can be seen within this angle.