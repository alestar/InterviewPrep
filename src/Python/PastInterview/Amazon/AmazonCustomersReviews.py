"""
1. Amazon Customer Reviews (example question)
Amazon is building a way to help customers search reviews quicker by providing real-time suggestions to search terms when the customer starts typing. When given a minimum of two characters into the search field the system will suggest at most three keywords from the review word repository. As the customer continues to type in the reviews search bar the relevant keyword suggestions will update automatically.

Write an algorithm that will output a maximum of three keyword suggestions after each character is typed by the customer in the search field.

If there are more than three acceptable keywords, return the keywords that are first in alphabetical order.
Only return keyword suggestions after the customer has entered two characters.
Keyword suggestions must start with the characters already typed

Both the repository and the customerQuery should be compared in a case-insensitive way.

Input:
The input to the method/function consists of two arguments:
repository, a list of unique strings representing the various keywords from the Amazon review comment section;
customerQuery, a string representing the full search query of the customer.

Output:
Return a list of a list of strings in lower case, where each list represents the keyword suggestions made by the system as the customer types each character of the customerQuery. Assume the customer types characters in order without deleting or removing any characters. If an output is not possible, return an empty array ([]).

Example
Input:
repository = [ "mobile", "mouse", "moneypot", "monitor", "mousepad" ]
customerQuery = "mouse"

Output:
["mobile", "moneypot", "monitor"]
["mouse", "mousepad"]
["mouse", "mousepad"]
["mouse", "mousepad"]

Explanation:
The chain of words that will generate in the search box will be
mo, mou, mous, mouse
and each line from output shows the suggestion of "mo", "mou", "mous", "mouse", respectively in each line.
For the keyword suggestions made by the system that are generated for 'mo', the matches that will be generated are:["mobile", "mouse", "moneypot", "monitor", "mousepad"]
Alphabetically, they will be reordered to [ "mobile", "moneypot", "monitor", "mouse", "mousepad" ].
Thus the keyword suggestions made by the system are [ "mobile", "moneypot", "monitor"].

Other ed Cases:
	ab abc abcd
	abc abcd abcde
	abcd abcde abcdef
	abcde abcdef abcdefg
	abcdef abcdefg abcdefgh

"""


# # !/bin/python3
#
# import math
# import os
# import random
# import re
# import sys


#
# Complete the 'searchSuggestions' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY repository
#  2. STRING customerQuery
#

class Node:
	def __init__(self, is_word, children):
		self.is_word = is_word
		self.children = children


def build_trie(words):
	trie = Node(False, {})
	for word in words:
		curr = trie
		for c in word:
			if c not in curr.children:
				curr.children[c] = Node(False, {})
			curr = curr.children[c]
		curr.is_word = True
	return trie


def autocomplete(trie, word):
	curr = trie
	for c in word:
		if c not in curr.children:
			return []
		curr = curr.children[c]

	words = []
	dfs(curr, word, words)
	return words


def dfs(node, prefix, words):
	if node.is_word:
		words.append(prefix)
	for c in node.children:
		dfs(node.children[c], prefix + c, words)


def searchSuggestions(repository, customer_query):
	if not repository:
		return []
	if not customer_query:
		return []

	# Lower case for customer query
	customer_query_low = customer_query.lower()

	# Lower case for all words in repo
	repo_low = []
	for r in repository:
		low_repo = r.lower()
		repo_low.append(low_repo)

	# Build trie out of repo words
	trie = build_trie(repo_low)

	sol = []
	prefix = ""
	for i in range(0, len(customer_query_low)):  # Iterate every char of query word
		prefix += customer_query_low[i]  # update the prefix by adding each char
		if i > 0:  # When at least 2 char of the query word, start auto completion
			print(prefix)
			autocompletion = autocomplete(trie, prefix)  # Auto-complete words for Prefix so far
			sort_list = sorted(autocompletion)  # Sort alphabetically the list of autocompleted words
			lst = sort_list[:3]  # Slice the list to only the  first 3 words
			sol.append(lst)  # Add words list to the solution list
	return sol


def print_list(lst):
	for item in lst:
		print(item)


repo = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
customer_query1 = "mouse"
customer_query2 = "all"
print_list(searchSuggestions(repo, customer_query1))
print_list(searchSuggestions(repo, customer_query2))
