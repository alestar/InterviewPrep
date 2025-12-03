"""
Imagine you are developing a sophisticated text processing tool editors use to format lists of words for publication quickly. You are given an array of strings wordsList. Your tool needs to automatically adjust the format of each word based on its length: if the length of a string is even, the word should be reversed; if the length of a string is odd, the word should be converted to uppercase.

Your task is to write a function that processes the input array wordsList according to these rules and returns a new array where each string has been formatted correctly.

Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(wordsList.length * max(wordsList[i].length)2) will fit within the execution time limit.

Example

For wordsList = ["HeLLo", "Data", "science"], the output should be solution(wordsList) = ["HELLO", "ataD", "SCIENCE"].

Explanation:

"HeLLo" has an odd length, so it is converted to uppercase: "HELLO".
"Data" has an even length, so it is reversed: "ataD".
"science" has an odd length, so it is converted to uppercase: "SCIENCE".
For wordsList = [], the output should be solution(wordsList) = [].

Explanation:
The input list is empty, so the output is also an empty list.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.string wordsList

An array of strings containing words.

Guaranteed constraints:
0 ≤ wordsList.length ≤ 100,
1 ≤ wordsList[i].length ≤ 50.

[output] array.string

An array of strings where each word is formatted according to the specified rules.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name

"""
def solution(wordsList):
    result = []

    for word in wordsList:
        if len(word) % 2 == 0:
            result.append(word[::-1])  # Reverse the word for even length
        else:
            result.append(word.upper())  # Convert to uppercase for odd length

    return result
# Example usage:
wordsList1 = ["HeLLo", "Data", "science"]
print(solution(wordsList1))  # Output: ["HELLO", "ataD", "SCIENCE"]
wordsList2 = []
print(solution(wordsList2))  # Output: []
wordsList3 = ["Python", "is", "fun"]
print(solution(wordsList3))  # Output: ["nohtyP", "SI",