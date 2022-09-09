"""
Example 1:

Input:
I.like.eating.ice.cream

Output:
cream.ice.eating.like.I


"""
def reverse_string(str):

	if not str:
		return None

	word_list = str.split(".")
	word_list.reverse()
	size = len(word_list)
	count = 0
	res = ""
	for word in word_list:
		if count < size - 1:
			res += word + "."
		else:
			res += word
		count += 1

	return res


print(reverse_string("I.like.eating.ice.cream"))
