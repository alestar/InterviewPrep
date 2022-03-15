def is_in_list(n, lst):
    found = False
    for i in lst:
        if i == n:
            found = True
            break
    return found


# print(is_in_list(5, [1, 2, 3, 4]))
# print(is_in_list(5, [1, 5, 6]))


def intersection(lst1, lst2):
    inter_lst =[]
    for i in lst1:
        for j in lst2:
            if i == j:
                if is_in_list(i, inter_lst):
                    continue
                else:
                    inter_lst.append(i)
            else:
                continue
    return inter_lst


print(intersection([1, 2, 3], [2, 4, 6]))
print(intersection([1, 2, 3], [4, 5, 6]))
print(intersection([2, 3, 2, 4], [2, 2, 4]))
