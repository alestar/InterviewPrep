"""

Given N kids and M ice cream sellers on a 1D line, find the smallest distance E such that every kid is within E of a seller.
"""


def find_smallest_distance_optimal(kids, sellers):
    # Sort the positions
    kids.sort()
    sellers.sort()

    max_e = 0
    j = 0  # pointer for sellers
    left_seller = float('-inf')

    for kid in kids:
        # move the seller pointer to the first seller >= kid
        while j < len(sellers) and sellers[j] < kid:
            left_seller = sellers[j]
            j += 1

        # nearest distance to left seller
        dist_left = kid - left_seller if left_seller != float('-inf') else float('inf')
        # nearest distance to right seller
        dist_right = sellers[j] - kid if j < len(sellers) else float('inf')

        # minimal distance to nearest seller
        min_dist = min(dist_left, dist_right)

        # update max distance across all kids
        max_e = max(max_e, min_dist)

    return max_e


"""
bidirectional traverse - the nearest seller is either on the left or right of each child 
1 - Traverse from left to right，always record the latest seller s_i, and record the left nearest distance k_i - s_i of current kid into left_array 
2 - Traverse from right to left，always record the latest seller s_i, and record the left nearest distance s_i - k_i of current kid into right_array
3 - Find the maximum of the min(left_array[i], right_array[i]) of each kid

Time complexity: O(N+M) 3 passes of traverse of the input Space complexity: O(N) record the left nearest and right nearest distance

Anyone can propose a solution that is O(N+M) or O((N+M)log(N+M)) in time and O(1) in space?

"""

def find_smallest_distance_bi_directional(kids, sellers):
    #kids.sort()
    #sellers.sort()
    n, m = len(kids), len(sellers)

    left_array = [float('inf')] * n
    right_array = [float('inf')] * n

    # Left to right
    seller_idx = 0
    for i in range(n):
        while seller_idx < m and sellers[seller_idx] <= kids[i]:
            seller_idx += 1
        if seller_idx > 0:
            left_array[i] = kids[i] - sellers[seller_idx - 1]

    # Right to left
    seller_idx = m - 1
    for i in range(n - 1, -1, -1):
        while seller_idx >= 0 and sellers[seller_idx] >= kids[i]:
            seller_idx -= 1
        if seller_idx < m - 1:
            right_array[i] = sellers[seller_idx + 1] - kids[i]

    # Find the minimum of the maximum distances
    min_distance = 0
    for i in range(n):
        min_distance = max(min_distance, min(left_array[i], right_array[i]))

    return min_distance


def find_smallest_distance_binary_search(kids, sellers):
    """
    Finds the smallest distance E such that every kid is within E of a seller.

    Args:
        kids (list): A list of integer positions for the kids.
        sellers (list): A list of integer positions for the ice cream sellers.

    Returns:
        float: The smallest distance E.
    """
    # Sort the positions for efficient searching
    kids.sort()
    sellers.sort()

    def check(e):
        """
        Checks if every kid can be covered with a maximum distance of e.
        Uses a two-pointer approach for efficiency.
        """
        seller_idx = 0
        for kid_pos in kids:
            # Find the nearest seller to the current kid
            while seller_idx < len(sellers) - 1 and sellers[seller_idx] < kid_pos - e:
                seller_idx += 1

            # Check if the nearest seller can cover the kid
            if abs(sellers[seller_idx] - kid_pos) > e:
                return False
        return True

    # Binary search for the optimal distance E
    left, right = 0, max(max(kids) - min(kids), max(sellers) - min(sellers))
    ans = right

    # Perform binary search on the range of possible distances
    while abs(right - left) > 1e-7:  # Use a small epsilon for float comparison
        mid = (left + right) / 2
        if check(mid):
            ans = mid
            right = mid
        else:
            left = mid

    return ans

# Example usage
N = 3
M = 2

kids = [1, 5, 9]
sellers = [2, 8]

kid_positions_1 = [10, 20, 30]
seller_positions_1 = [15, 25]

# Expected result should be 5, since:
# - Kid at 10 is covered by seller at 15 (distance 5).
# - Kid at 20 is covered by seller at 15 or 25 (distance 5).
# - Kid at 30 is covered by seller at 25 (distance 5).
result = find_smallest_distance_binary_search(kid_positions_1, seller_positions_1)
result_bi = find_smallest_distance_bi_directional(kid_positions_1, seller_positions_1)
result_optimal = find_smallest_distance_optimal(kid_positions_1, seller_positions_1)
print(f"The smallest distance E is: {result}")
print(f"The smallest distance E (bi-directional) is: {result_bi}")
print(f"The smallest distance E (optimal) is: {result_optimal}")

