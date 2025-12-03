"""
2492. Minimum Score of a Path Between Two Cities Difficulty: -Medium
Hint
You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

A path is a sequence of roads between two cities.
It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
The test cases are generated such that there is at least one path between 1 and n.

Example 1:
Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
Output: 5
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.

Example 2:
Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
Output: 2
…
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.

"""
def min_score_bfs(n, roads):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for a, b, distance in roads:
        graph[a].append((b, distance))
        graph[b].append((a, distance))

    min_score = float('inf')
    visited = set()
    queue = deque([1]) # Start BFS from city 1
    visited.add(1)

    while queue:
        city = queue.popleft()
        for neighbor, distance in graph[city]:
            min_score = min(min_score, distance)
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return min_score

def min_score_dfs(n, roads):
    from collections import defaultdict

    graph = defaultdict(list)
    for a, b, distance in roads:
        graph[a].append((b, distance)) # Build the graph directionally
        graph[b].append((a, distance)) # Build the graph bidirectionally

    min_score = float('inf')
    visited = set()

    def dfs(city):
        nonlocal min_score # To modify the outer scope variable, that is modified inside dfs
        visited.add(city)
        for neighbor, distance in graph[city]:
            min_score = min(min_score, distance) # Update min_score
            if neighbor not in visited: # Continue DFS if not visited
                dfs(neighbor)

    dfs(1) # Start DFS from city 1
    return min_score

def min_score_union_find(n, roads):
    parent = list(range(n + 1))
    rank = [1] * (n + 1)

    def find(city):
        if parent[city] != city:
            parent[city] = find(parent[city]) # Path compression
        return parent[city]

    def union(city1, city2):
        root1 = find(city1)
        root2 = find(city2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    for a, b, _ in roads:
        union(a, b)

    min_score = float('inf')
    for a, b, distance in roads:
        if find(1) == find(a): # Check if city 1 is connected to city a
            min_score = min(min_score, distance)

    return min_score

# Example usage:
n1 = 4
roads1 = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
print(min_score_bfs(n1, roads1))  # Output: 5
print(min_score_dfs(n1, roads1))  # Output: 5
print(min_score_union_find(n1, roads1))  # Output: 5

n2 = 4
roads2 = [[1,2,2],[1,3,4],[3,4,7]]
print(min_score_bfs(n2, roads2))  # Output: 2
print(min_score_dfs(n2, roads2))  # Output: 2
print(min_score_union_find(n2, roads2))  # Output: 2