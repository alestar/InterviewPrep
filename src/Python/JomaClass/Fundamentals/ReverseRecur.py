def reverse_str_rec(my_str):
    # Base Case
    if len(my_str) < 2:
        return my_str
    # Recursive Case
    else:
        return reverse_str_rec(my_str[1:]) + my_str[0]


print(reverse_str_rec("Jonathan is a teacher"))
