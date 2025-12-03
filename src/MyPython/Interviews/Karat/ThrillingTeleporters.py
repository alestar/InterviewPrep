"""
We're building the game engine for Thrilling Teleporters, a board game with N tiles, starting from tile 0.

Certain tiles contain teleporters that instantly move the player to a specific tile, either forward or backward. For example, here are three teleporters:

teleporters1 = [
  "3,1", -- From tile 3 to tile  1
  "4,2", -- From tile 4 to tile  2
  "5,10" -- From tile 5 to tile 10
]

Or as seen on the board:

       "3,1"
     ┌─<───<─┐                                    N = 12
     v       │
 0 → 1 → 2 → 3 . 4 . 5 . 6 → 7 → 8 → 9 → 10 → 11 → 12
         ^       │   │                    ^
         └─<───<─┘   └──>───>───>───>───>──┘
           "4,2"             "5,10"

After rolling the die:
- The player moves forward by the number rolled.
- If the player lands on a tile with a teleporter, they are immediately sent to its destination.
- The player can’t move past the final tile N, and only one teleporter is used per die roll.
To add variety, the die can have any number of sides (minimum 2).

Write a function that returns all unique tiles the player can reach in a single die roll, given:

- A list of teleporter strings
- The number of sides on the die
- The player's starting tile
- The total number of tiles N

Example:
The player starts at tile 0 on a board of size N = 12, using a standard 6-sided die and the teleporters defined earlier.

They can roll values from 1 to 6, leading to the following tile outcomes: [_, _, _, _, _, _].
- Rolling 1, 2, or 6 lands the player on tiles with no teleporters, so they stay on those tiles → [1, 2, _, _, _, 6].
- Rolling 3 activates a teleporter from tile 3 to tile 1 → updated list: [1, 2, 1, _, _, 6].
- Rolling 4 teleports the player from tile 4 to tile 2 → updated list: [1, 2, 1, 2, _, 6].
- Rolling 5 teleports the player from tile 5 to tile 10 → final list: [1, 2, 1, 2, 10, 6].
Removing duplicates, the final possible tiles are: [1, 2, 10, 6].

Additional Inputs:
teleporters2 = ["5,10", "6,22", "39,40", "40,49", "47,29"]
teleporters3 = ["6,18", "36,26", "41,21", "49,55", "54,52",
                "71,58", "74,77", "78,76", "80,73", "92,85"]
teleporters4 = ["97,93", "99,81", "36,33", "92,59", "17,3",
                "82,75", "4,1", "84,79", "54,4", "88,53",
                "91,37", "60,57", "61,7", "62,51", "31,19"]
teleporters5 = ["3,8", "8,9", "9,3"]

All Test Cases:
(output can be in any order)
                           die  start
                          sides,tile  N
destinations(teleporters1,  6,    0,  12) => [1, 2, 10, 6]
destinations(teleporters2,  6,   46, 100) => [48, 49, 50, 51, 52, 29]
destinations(teleporters2, 10,    0,  50) => [1, 2, 3, 4, 7, 8, 9, 10, 22]
destinations(teleporters3, 10,   95, 100) => [96, 97, 98, 99, 100]
destinations(teleporters3, 10,   70, 100) => [72, 73, 75, 76, 77, 79, 58]
destinations(teleporters4,  6,    0, 100) => [1, 2, 3, 5, 6]
destinations(teleporters5,  7,    2,  20) => [3, 4, 5, 6, 7, 8, 9]

Complexity Variable:
N = number of tiles
Note: The number of teleporters, T, and the size of the die, D, are bounded by N.
"""
def destinations(teleporters, die_sides, start_tile, N):
    teleporter_map = {}
    for teleporter in teleporters:
        src, dest = map(int, teleporter.split(','))
        teleporter_map[src] = dest

    reachable_tiles = set()

    for roll in range(1, die_sides + 1):
        next_tile = start_tile + roll
        if next_tile > N:
            continue
        if next_tile in teleporter_map:
            next_tile = teleporter_map[next_tile]
        reachable_tiles.add(next_tile)

    return list(reachable_tiles)

def destinations2(teleporters, die_sides, start, board):

    res = set()
    curr= start

    for roll in range(1, die_sides + 1):
        curr = curr + roll
        tile = curr

        for tp in teleporters:
            tp_list = tp.split(',')

            if curr == int(tp_list[0]):
                tile = int(tp_list[1])
        curr= start
        if tile <= board:
            res.add(tile)
    return res
# Example usage:
teleporters1 = ["3,1", "4,2", "5,10"]
print(destinations(teleporters1, 6, 0, 12))  # Output: [1, 2, 10, 6]
teleporters2 = ["5,10", "6,22", "39,40", "40,49", "47,29"]
print(destinations(teleporters2, 6, 46, 100))  # Output: [48, 49, 50, 51, 52, 29]
print(destinations(teleporters2, 10, 0, 50))  # Output: [1, 2, 3, 4, 7, 8, 9, 10, 22]
teleporters3 = ["6,18", "36,26", "41,21", "49,55", "54,52",
                "71,58", "74,77", "78,76", "80,73", "92,85"]
print(destinations(teleporters3, 10, 95, 100))  # Output: [96, 97, 98, 99, 100]
print(destinations(teleporters3, 10, 70, 100))  # Output: [72, 73, 75, 76, 77, 79, 58]
teleporters4 = ["97,93", "99,81", "36,33", "92,59", "17,3",
                "82,75", "4,1", "84,79", "54,4", "88,53",
                "91,37", "60,57", "61,7", "62,51", "31,19"]
print(destinations(teleporters4, 6, 0, 100))  # Output: [1, 2, 3, 5, 6]
teleporters5 = ["3,8", "8,9", "9,3"]
print(destinations(teleporters5, 7, 2, 20))  # Output: [3, 4, 5, 6, 7, 8, 9]