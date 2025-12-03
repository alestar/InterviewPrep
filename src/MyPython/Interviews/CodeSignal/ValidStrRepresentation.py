"""
Practice Recovery Question
0:46:31
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Consider two following representations of a non-negative integer:

A simple decimal integer, constructed of a non-empty sequence of digits from 0 to 9;
An integer with at least one digit in a base from 2 to 16 (inclusive), enclosed between # characters, and preceded by the base,
 which can only be a number between 2 and 16 in the first representation.For digits from 10 to 15 characters a, b, ..., f and A, B, ..., F are used.
Additionally, both representations may contain underscore (_) characters; they are used only as separators for improving legibility of numbers and can be ignored while processing a number.

Your task is to determine whether the given string is a valid integer representation.

Note: this is how integer numbers are represented in the programming language Ada.

Example

For line = "123_456_789", the output should be solution(line) = true;
For line = "16#123abc#", the output should be solution(line) = true;
For line = "10#123abc#", the output should be solution(line) = false;
For line = "10#10#123ABC#", the output should be solution(line) = false;
For line = "10#0#", the output should be solution(line) = true;
For line = "10##", the output should be solution(line) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string line

A non-empty string.

Guaranteed constraints:
2 ≤ line.length ≤ 30.

[output] boolean

true if line is a valid integer representation, false otherwise.


def solution(line):
    atLeastOneDigit = False
    if line[len(line) - 1] == '#':
        i = 0
        base = 0
        ...
        if base < 2 or base > 16:
            return False
        i += 1
        while i < len(line) - 1:
            if line[i] != '_':
                digit = -1
                if 'a' <= line[i] and line[i] <= 'f':
                    digit = ord(line[i]) - ord('a') + 10
                if 'A' <= line[i] and line[i] <= 'F':
                    digit = ord(line[i]) - ord('A') + 10
                if '0' <= line[i] and line[i] <= '9':
                    digit = ord(line[i]) - ord('0')
                if 0 <= digit and digit < base:
                    atLeastOneDigit = True
                else:
                    return False
            i += 1
    else:
        for i in range(len(line)):
            if line[i] != '_':
                if '0' <= line[i] and line[i] <= '9':
                    atLeastOneDigit = True
                else:
                    return False
    return atLeastOneDigit

"""

def solution(line):
    atLeastOneDigit = False
    if line[len(line) - 1] == '#':
        i = 0
        base = 0

        # Parse the base (digits before the first '#')
        while i < len(line) and line[i] != '#':
            if line[i] == '_':  # skip underscores
                i += 1
                continue
            if '0' <= line[i] <= '9':
                base = base * 10 + int(line[i])
            else:
                return False  # invalid character in base
            i += 1

        # Base must be between 2 and 16
        if base < 2 or base > 16:
            return False

        # Skip the '#' separator
        i += 1

        # Parse the number in the given base
        while i < len(line) - 1:
            if line[i] != '_':
                digit = -1
                if '0' <= line[i] <= '9':
                    digit = ord(line[i]) - ord('0')
                elif 'a' <= line[i] <= 'f':
                    digit = ord(line[i]) - ord('a') + 10
                elif 'A' <= line[i] <= 'F':
                    digit = ord(line[i]) - ord('A') + 10
                else:
                    return False  # invalid character

                if 0 <= digit < base:
                    atLeastOneDigit = True
                else:
                    return False  # digit not valid for base
            i += 1

    else:
        # Simple decimal number
        for i in range(len(line)):
            if line[i] != '_':
                if '0' <= line[i] <= '9':
                    atLeastOneDigit = True
                else:
                    return False

    return atLeastOneDigit

# Example test cases
print(solution("123_456_789"))  # True
print(solution("16#123abc#"))    # True
print(solution("10#123abc#"))    # False
print(solution("10#10#123ABC#")) # False
print(solution("10#0#"))         # True
print(solution("10##"))          # False