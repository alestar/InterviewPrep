def filter_gt_n(lst, n):
    # Base Case
    if not lst:
        return lst
    # Recursive Case
    elif lst[0] > n:  # Filter num bigger than 'n'
        return lst[0:1] + filter_gt_n(lst[1:], n)  # keep number
    else:
        return filter_gt_n(lst[1:], n)  # remove number


print(filter_gt_n([1, 2, 3, 4], 2))
print(filter_gt_n([1, 2, 3, 4], 4))
print(filter_gt_n([2, 2, 3, 3], 4))
print(filter_gt_n([2, 2, 3, 3], 1))
