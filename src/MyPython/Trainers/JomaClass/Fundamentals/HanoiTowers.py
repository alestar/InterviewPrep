def print_move(n, fr, to):
    print("Move Disc \"" + str(n) + "\" from " + str(fr) + ' --> ' + str(to))


def TowersHanoiHandler(n, fr, to, spare):
    if n == 1:
        print_move(n, fr, to)
    else:
        TowersHanoiHandler(n-1, fr, spare, to)
        TowersHanoiHandler(1, fr, to, spare)
        TowersHanoiHandler(n-1, spare, to, fr)


def TowersHanoiHandler2(n, start, intermediate, goal):
    if n == 0:
        return
    else:
        TowersHanoiHandler2(n - 1, start, goal, intermediate)  # Move all disc - 1 from the start to the intermediate
        print_move(n, start, goal)  # Move the remaining Disc to the goal or end
        TowersHanoiHandler2(n - 1, intermediate, start, goal)  # Move all disc - 1 from the intermediate to the goal


def TowersHanoi():
    # Classic Solution Implementation
    # Start : 'Pole1'
    # End or Goal: 'Pole3'
    # Spare or Intermediate: 'Pole2'
    # TowersHanoiHandler(5, 'Pole1', 'Pole3', 'Pole2')

    # The goal is to move all the Discs from 'Pole1' to 'Pole3'
    # Start : 'Pole1'
    # Spare or Intermediate: 'Pole2'
    # End or Goal: 'Pole3'
    TowersHanoiHandler2(3, 'Pole1', 'Pole2', 'Pole3')


TowersHanoi()
