"""
Implement a method to create list [1,2,4] from input [1,2,3] that is turn into num,ber '123',
and add '1' given new number '124',
and turn that into list.
"""
def increment_list(digits):
    # Step 1: Convert list of digits to a number
    num = int("".join(map(str, digits)))

    # Step 2: Add 1
    num += 1

    # Step 3: Convert back to list of digits
    return [int(d) for d in str(num)]

# Example usage
input_list = [1,2,3]
print("input: " + str(input_list))  # [1, 2, 3]
output_list = increment_list(input_list)
print("output: " + str(output_list))  # [1, 2, 4]
