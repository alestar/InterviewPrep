"""
Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.
For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".
Provide an implementation for shortenPath method below based on the above requirements.

Tips:
1 - Empty subdirectory is the same as "/./". Therefore "/usr//" -> "/usr/"
2 - Backtracking ('..') when the current directory is root keeps you at root. Hence, "/usr/../.." returns "/"
3 - “..” implies go up one level of enclosing folder from the current directory
4 - “.” implies stay at the current directory

Test Cases:
- EtcPath: Shortened path for "/etc/../../apache2/original/./extra/.." should be "/apache2/original/"
- PathWithSpaces: Shortened path for "/ User Data  /" should be "/User Data/"
- EmptyPaths: Shortened path for "", "/", "//", " "  should be "/"
- EmptyDirectory: Shortened path for "/etc/../../apache2/original//extra/.." should be "/apache2/original/"
- QuestionSample: Shortened path for "/usr/bin/../bin/./scripts/../" should be "/usr/bin/"
- BackToRoot: Shortened path for "/usr/bin/../../" should be "/"
- BackTrackBeyondRoot: Shortened path for "/usr/bin/../../../" should be "/"
- BackTrackFromRoot: Shortened path for "/../../" should be "/"

"""


def simplify_path(abs_path):
	stack = ['/']
	dirs = abs_path.strip().split("/")
	for curr_dir in dirs:
		if curr_dir == '..':
			if len(stack) > 1:
				stack.pop()
			else:
				continue
		elif curr_dir == '.':
			continue
		elif curr_dir != '':
			stack.append("/" + str(curr_dir.strip()))
	if len(stack) == 1:
		return "/"
	return "".join(stack[1:]) + "/"


def simplify_path_test(test_name, test_input, test_expected):
	test_output = simplify_path(test_input)
	print(" Test: '" + test_name + "', Expected: '" + test_expected + "' Actual: '" + test_output + "'")


if __name__ == "__main__":
	simplify_path_test("EtcPath", "/etc/../../apache2/original/./extra/..", "/apache2/original/")
	simplify_path_test("PathWithSpaces", "/ User Data  /", "/User Data/")
	simplify_path_test("EmptyPaths1", "", "/")
	simplify_path_test("EmptyPaths2", "/", "/")
	simplify_path_test("EmptyPaths3", "//", "/")
	simplify_path_test("EmptyPaths4", " ", "/")
	simplify_path_test("EmptyDirectory", "/etc/../../apache2/original//extra/..", "/apache2/original/")
	simplify_path_test("QuestionSample", "/usr/bin/../bin/./scripts/../", "/usr/bin/")
	simplify_path_test("BackToRoot", "/usr/bin/../../", "/")
	simplify_path_test("BackTrackBeyondRoot", "/usr/bin/../../../", "/")
	simplify_path_test("BackTrackFromRoot", "/../../", "/")
