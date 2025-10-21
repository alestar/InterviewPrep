"""
In the shadowy circuits of the hacker underworld, data isn’t just stored, it’s encoded with secrets.
Among the lines of encrypted entries lies an array of codes (represented by positive integers), each one a digital fingerprint.
Within this set, certain code-pairs appear nearly identical, save for a subtle corruption in a single digit.
You’ve intercepted this array, and your mission is to uncover how many unique index-pairs (i, j) exist such that 0 ≤ i < j < codes.length,
where the codes are exactly the same length, but differ in precisely one digit. Example For codes = [404, 12, 504, 7, 414, 604, 700, 1],
the output should be solution(codes) = 5.
    codes[0] = 404 differs from codes[2] = 504 in the first digit.
    codes[0] = 404 differs from codes[4] = 414 in the second digit.
    codes[0] = 404 differs from codes[5] = 604 in the first digit.
    codes[2] = 504 differs from codes[5] = 604 in the first digit.
    codes[3] = 7 differs from codes[7] = 1 in their only digit.
Only pairs with the same number of digits are considered.
For example: codes[0] = 404 and codes[1] = 12 are ignored, since they have different lengths (3 vs 2).
Input/Output [execution time limit] 4 seconds (py3) [memory limit] 1 GB [input] array.integer codes
The array holds positive integers, each one a shard of hidden knowledge.
Guaranteed constraints: 1 ≤ codes.length ≤ 104, 1 ≤ codes[i] ≤ 109.
[output] integer The number of pairs of equal-length codes that differ in precisely one digit.
"""
from collections import defaultdict

def solution(codes):
    def generate_patterns(code_str):
        patterns = []
        for i in range(len(code_str)):
            pattern = code_str[:i] + '_' + code_str[i+1:]
            patterns.append(pattern)
        return patterns

    pattern_count = defaultdict(list)  # store all previous codes
    total_pairs = 0

    for code in codes:
        code_str = str(code)
        patterns = generate_patterns(code_str)

        for pattern in patterns:
            for prev_code in pattern_count[pattern]:
                if prev_code != code:  # only count if exactly one digit differs
                    total_pairs += 1
            pattern_count[pattern].append(code)  # add current code to mask

    return total_pairs



def solution1(codes):
    length_groups = defaultdict(list)
    for code in codes:
        s = str(code)
        length_groups[len(s)].append(s)

    total_pairs = 0

    for group in length_groups.values():
        masks = defaultdict(list)  # store all previous codes (with duplicates) key:mask, value:list of codes
        for code in group:
            for i in range(len(code)):
                masked = code[:i] + "_" + code[i+1:]
                for prev in masks[masked]:
                    if prev != code:  # differ in exactly one digit
                        total_pairs += 1
                masks[masked].append(code)  # append to list, not set

    return total_pairs




codes = [5, 5, 5, 5, 5, 5, 8]
print(solution(codes))  # Output: 6
print(solution1(codes))  # Output: 6
codes = [404, 504, 414, 604, 700]
print(solution(codes))  # Output: 4
print(solution1(codes))  # Output: 4
codes = [404, 12, 504, 7, 414, 604, 700, 1]
print(solution(codes))  # Output: 5
print(solution1(codes))  # Output: 5
codes = [123, 223, 133, 124, 125, 126]
print(solution(codes))  # Output: 8
print(solution1(codes))  # Output: 8
codes = [1, 2, 3, 4, 5]
print(solution(codes))  # Output: 10
print(solution1(codes))  # Output: 10
codes = [10, 20, 30, 40, 50]
print(solution(codes))  # Output: 10
print(solution1(codes))  # Output: 10
codes = [111, 121, 131, 141, 151]
print(solution(codes))  # Output: 10
print(solution1(codes))  # Output:10
codes = [999, 998, 997, 996, 995]
print(solution(codes))  # Output: 10
print(solution1(codes))  # Output:10
codes = [1234, 2234, 3234, 4234, 5234]
print(solution(codes))  # Output: 10
print(solution1(codes))  # Output:10
codes = [1001, 2001, 3001, 4001, 5001]
print(solution(codes))  # Output: 10
print(solution1(codes))  # Output:10