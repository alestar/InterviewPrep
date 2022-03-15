def is_in_list(n, lst):
    # Base Case
    if not lst:
        return False
    # Recursive Case
    else:
        return lst[0] == n or is_in_list(n, lst[1:])


def intersection1(lst1, lst2):
    if not lst1:
        return []
    #  Note: Check if numb  is later in 'lst1' to prevent double addition (prematurely)
    if not is_in_list(lst1[0], lst2) or is_in_list(lst1[0], lst1[1:]):  # not in 'lst2' or is repeated in 'lst1' (later)
        return intersection1(lst1[1:], lst2)  # disregard num and continue to the rest of the 'lst1'
    else:
        return lst1[:1] + intersection1(lst1[1:], lst2)  # keep number for the result list
        # + the rest of the intersection computation


print(intersection1([1, 2, 3], [2, 4, 6]))
print(intersection1([1, 2, 3], [4, 5, 6]))
print(intersection1([2, 3, 2, 4], [2, 2, 4]))
