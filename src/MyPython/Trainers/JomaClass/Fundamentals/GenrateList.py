def generate_list(start, end, step):
    i = start
    result_list = []

    if(start > end):
        while i > end:
            result_list.append(i)
            i += step
    else:
        while i < end:
            result_list.append(i)
            i += step
    return result_list

# print(generate_list(0, 5, 1))
# print(generate_list(0, 0, 1))
# print(generate_list(5, 10, 2))
# print(generate_list(10, 5, -2))


def reverse_list(list_orig):
    reversed_list = []
    i = 1
    while i <= len(list_orig):
        reversed_list.append(list_orig[-i])
        i += 1
    return reversed_list


print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
