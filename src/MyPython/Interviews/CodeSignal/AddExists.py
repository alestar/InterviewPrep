"""
Welcome to the practice task! This task is designed to be a playground that allows you to get acquainted to the testing environment and practice the functionalities of the platform.

Solving this task consists of several steps, and each next step is opened whenever the current step is solved correctly.
You always have access to the current and all previous steps data.

Your task is to implement a simple container of integer numbers. As a first step, consider implementing the following two operations:

ADD <value> should add the specified integer value to the container. Returns an empty string.
EXISTS <value> should check whether the specific integer value exists in the container. Returns "true" if the value exists, "false" otherwise.
The container is supposed to be empty at the beginning of execution.

Given a list of queries, return the list of answers for these queries. To pass to the next level you have to pass all tests at this level.

Environment
To customize the editor settings and see the editor hotkeys, check out the IDE Settings tabin the lower left corner of the page.

For debugging purposes, you can:
Run just a single test case by clicking the "Run single" button to the right of each test case
Setting up and executing a set of custom tests at "Custom Tests" tab
For more information, check out the Readme tabon the left.
Partial credit will be granted for each test passed, so press Submit often to run tests and receive partial credits for passed tests. Please check tests for requirements and argument types.

Example

For
queries = [
    ["ADD", "1"],
    ["ADD", "2"],
    ["ADD", "5"],
    ["ADD", "2"],
    ["EXISTS", "2"],
    ["EXISTS", "5"],
    ["EXISTS", "1"],
    ["EXISTS", "4"],
    ["EXISTS", "3"],
    ["EXISTS", "0"]
]
the output should be solution(queries) = ["", "", "", "", "true", "true", "true", "false", "false", "false"].

Explanation:

Add 1, 2, 5, 2 -> [1, 2, 5, 2]
Numbers 2, 5, 1 exist in the container
Numbers 4, 3, 0 don't exist in the container

"""
def solution(queries):
    container = set()  # our container of integers
    answers = []

    for query in queries:
        op = query[0]
        value = int(query[1])

        if op == "ADD":
            container.add(value)
            answers.append("")  # ADD returns empty string
        elif op == "EXISTS":
            answers.append("true" if value in container else "false")
        else:
            raise ValueError(f"Unknown operation: {op}")

    return answers
# Example usage:
queries = [
    ["ADD", "1"],
    ["ADD", "2"],
    ["ADD", "5"],
    ["ADD", "2"],
    ["EXISTS", "2"],
    ["EXISTS", "5"],
    ["EXISTS", "1"],
    ["EXISTS", "4"],
    ["EXISTS", "3"],
    ["EXISTS", "0"]
]
print(solution(queries))  # Output: ["", "", "", "", "true", "true", "true", "false", "false", "false"]
