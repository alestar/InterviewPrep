def is_in_list(n, lst):
    # Base Case
    if not lst:
        return False
    else:
        return lst[0] == n or is_in_list(n, lst[1:])


print(is_in_list(5, [1, 2, 3]))
print(is_in_list(5, [1, 2, 3, 4, 5]))
