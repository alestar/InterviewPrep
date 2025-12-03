"""
Question 2 of 4
1:00:18
Imagine you're part of a team analyzing fictional alien technology logs. You have a string alienCode, which represents activity codes from their devices. Your task is to examine this string and count how many substrings of this code represent numbers evenly divisible by 3. It's important to note that none of these substrings should start with zero unless the substring is the character "0" itself.

Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(alienCode.length3) will fit within the execution time limit.

Example

For alienCode = "456", the output should be solution(alienCode) = 3.

Consider all substrings of the given string:

alienCode[0..0] = 4 isn't divisible by 3.
alienCode[1..1] = 5 isn't divisible by 3.
alienCode[2..2] = 6 is divisible by 3.
alienCode[0..1] = 45 is divisible by 3.
alienCode[1..2] = 56 isn't divisible by 3.
alienCode[0..2] = 456 is divisible by 3.
There are 3 substrings that meet the conditions, so the answer is 3.

For alienCode = "6666", the output should be solution(alienCode) = 10.

All substrings are divisible by 3 and have no leading zeros, so the answer is equal to the number of possible substrings, which is 10.

For alienCode = "303", the output should be solution(alienCode) = 5.

alienCode[0..0] = 3 is divisible by 3.
alienCode[1..1] = 0 is divisible by 3.
alienCode[2..2] = 3 is divisible by 3.
alienCode[0..1] = 30 is divisible by 3.
alienCode[1..2] = 03 is divisible by 3, but it has leading zeroes, so we don't count it.
alienCode[0..2] = 303 is divisible by 3.
There are 5 substrings that meet the conditions, so the answer is 5.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string alienCode

A string of digits representing alien device activity codes.

Guaranteed constraints:
2 ≤ alienCode.length ≤ 10,
10 ≤ (int)alienCode ≤ 109.

[output] integer

Return the number of substrings that form an integer divisible by 3.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name

123
def solution(alienCode):


Tests
Custom Tests
0/300
object, ``` ``` , ``` ``` , hint


"""
def solution(alienCode):
    n = len(alienCode)
    count = 0

    # Iterate over all possible substrings
    for i in range(n):
        for j in range(i, n):
            sub = alienCode[i:j+1]

            # Skip substrings with leading zeros, except "0"
            if len(sub) > 1 and sub[0] == '0':
                continue

            # Convert substring to int
            num = int(sub)

            # Check divisibility by 3
            if num % 3 == 0:
                count += 1

    return count

def solution1(alienCode):
    count = 0
    n = len(alienCode)

    for i in range(n):
        for j in range(i, n):
            substring = alienCode[i:j + 1]
            if (substring[0] != '0' or substring == '0') and int(substring) % 3 == 0:
                count += 1

    return count
# Example usage:
alienCode1 = "456"
print(solution(alienCode1))  # Output: 3
alienCode2 = "6666"
print(solution(alienCode2))  # Output: 10
alienCode3 = "303"
print(solution(alienCode3))  # Output: 5
alienCode4 = "1203"
print(solution(alienCode4))  # Output: 5
alienCode5 = "000"
print(solution(alienCode5))  # Output: 3
alenCode6 ="0213"
print(solution(alenCode6))  # Output: 4
print(solution1(alenCode6))  # Output: 4