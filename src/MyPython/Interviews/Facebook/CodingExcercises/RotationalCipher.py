
"""
Rotational Cipher
One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount.
Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?".
Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A),
and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.

Given a string and a rotation factor, return an encrypted string.
Signature
	string rotationalCipher(string input, int rotationFactor)
Input
	1 <= |input| <= 1,000,000
	0 <= rotationFactor <= 1,000,000
Output
	Return the result of rotating input a number of times equal to rotationFactor.
Example 1
	input = Zebra-493?
	rotationFactor = 3
	output = Cheud-726?
Example 2
	input = abcdefghijklmNOPQRSTUVWXYZ0123456789
	rotationFactor = 39
	output = nopqrstuvwxyzABCDEFGHIJKLM9012345678
"""


def rotationalCipher(input, rotation_factor):
	sol = ""
	for c in input:
		if c.isupper():  # Check if it's an uppercase character

			# subtract the unicode of 'A' to get index in [0-25) range => 26 letter in the alphabet
			c_index = ord(c) - ord('A')  # ord('A') => 65, upper case letter star at '65' unicode

			# shift the current character by key positions
			c_shifted = (c_index + rotation_factor) % 26 + ord('A')  # Mod the rotated pos with '26',
			# to determine were it is in the alphabet,
			# and add ord('A') => 65 to calculate new unicode

			c_new = chr(c_shifted)  # convert unicode to char
			sol += c_new
		elif c.islower():  # Check if its a lowercase character

			# subtract the unicode of 'a' to get index in [0-25) range => 26 letter in the alphabet
			c_index = ord(c) - ord('a')  # ord('a') => 97, lowercase letter star at '97' unicode

			c_shifted = (c_index + rotation_factor) % 26 + ord('a')  # Mod the rotated pos with '26',
			# to determine were it is in the alphabet,
			# and add ord('a') => 97 to calculate new unicode

			c_new = chr(c_shifted) # convert unicode to char
			sol += c_new
		elif c.isdigit():

			# if it's a number,shift its actual value
			c_new = (int(c) + rotation_factor) % 10
			sol += str(c_new)

		else:
			# if its neither alphabetical nor a number, just leave it like that
			sol += c
	return sol

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
	print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
	global test_case_number
	result = False
	if expected == output:
		result = True
	rightTick = '\u2713'
	wrongTick = '\u2717'
	if result:
		print(rightTick, 'Test #', test_case_number, sep='')
	else:
		print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
		printString(expected)
		print(' Your output: ', end='')
		printString(output)
		print()
	test_case_number += 1

if __name__ == "__main__":
	input_0 = "Zebra-493?"
	rotation_factor_0 = 3
	expected_0 = "Cheud-726?"
	output_0 = rotationalCipher(input_0, rotation_factor_0)
	check(expected_0, output_0)


	input_1 = "All-convoYs-9-be:Alert1."
	rotation_factor_1 = 4
	expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
	output_1 = rotationalCipher(input_1, rotation_factor_1)
	check(expected_1, output_1)

	input_2 = "abcdZXYzxy-999.@"
	rotation_factor_2 = 200
	expected_2 = "stuvRPQrpq-999.@"
	output_2 = rotationalCipher(input_2, rotation_factor_2)
	check(expected_2, output_2)

	# Add your own test cases here
