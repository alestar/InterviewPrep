"""
String to Integer

Given a String, convert to an integer without using the built in function str.

You are allowed to use ord to convert a character to ASCII code.

Consider all possible cases of am integer. IN the case where the string is not a valid integer, return NOne.

"""


def convert_to_int(str):
	is_negative = False
	start_index = 0
	if str[0] == '-':
		is_negative = True
		start_index = 1

	result = 0
	for c in str[start_index:]:
		if not c.isdigit():
			return None
		result = result * 10 + ord(c) - ord('0')

	if is_negative:
		result *= -1
	return result


print(convert_to_int('-105') + 1)  # -104
print(convert_to_int('103453455') + 1)  # 103453456

