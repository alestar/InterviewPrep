def is_increasing(lst):

    if not lst:
        return False
    # Base Case
    if len(lst) == 1:
        return True
    # Recursive Case
    else:
        return lst[0] <= lst[1] and is_increasing(lst[1:])


print(is_increasing([1, 2, 3, 4]))
print(is_increasing([1, 3, 2, 4]))
print(is_increasing([1]))
print(is_increasing([]))
