"""
We can render an ASCII art pyramid with N levels by printing N rows of asterisks, where the top row has a single asterisk in the center and each successive row has two additional asterisks on either side.

Here's what that looks like when N is equal to 3.

  *
 ***
*****
And here's what it looks like when N is equal to 5.

    *
   ***
  *****
 *******
*********
Can you write a program that generates this pyramid with a N value of 10?

[execution time limit] 4 seconds (py3)

[memory limit] 2g

"""
def print_asterisks_pyramid(N):
    for i in range(N):
        # Calculate the number of spaces and asterisks for the current row
        spaces = ' ' * (N - i - 1)
        asterisks = '*' * (2 * i + 1)
        # Print the row
        print(spaces + asterisks + spaces)

def print_asterisks_pyramid1(N):
    for row in range(1, N + 1):
        num_asterisks = 2 * row - 1
        num_spaces = N - row
        line = ' ' * num_spaces + '*' * num_asterisks + ' ' * num_spaces
        print(line)


# Example usage:
N = 10
print_asterisks_pyramid(N)
print_asterisks_pyramid1(N)