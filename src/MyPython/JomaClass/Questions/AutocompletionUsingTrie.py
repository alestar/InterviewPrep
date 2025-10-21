class Node:
	def __init__(self, is_word, children):
		self.is_word = is_word
		# {'a': Node, 'b': Node, ...}
		self.children = children

class Solution:
	def build(self, words):
		trie = Node(False, {}) # Star constructing the Trie with an empty node
		for word in words:
			current = trie
			for c in word:
				if c not in current.children:
					current.children[c] = Node(False, {})  # if is a new letter, create a new node for it
				current = current.children[c]  # if is an existing letter point the curr node to it and continue iterating
			current.is_word = True  # When all the letter has been inserted into the Trie a word has been added and it will be marked in curr
		self.trie = trie # update the trie

	def autocomplete(self, word):
		curr = self.trie  # Start with the root node (usually empty node in a Trie)

		# Iterate though all the letters and verify that each exist in the Trie, until the last one
		for c in word:
			if c not in curr.children:  # if the one of the letter does not exit in the Trie
				return []  # then, the sequence of letters that correspond to the word can be form with the current Trie (return empty)
			# For the autocomplete to work, all the letters af the word must exist on the Trie, in the corresponding sequence
			curr = curr.children[c]  # else, update current to the node that contains the curren letter 'c'
		# * After the last iteration is done, curr will be pointing to the latest letter of the word that exist in the Trie,
		#  and at that point is ready to attempt autocompletion with potential words, that my exist in the Trie  *

		words = []  # List of possible words found on the Trie
		self.dfs_recur(curr, word, words)  # Explore all possible words that can be form from the curr node
		return words

	def dfs_recur(self, node, prefix, words):
		if node.is_word:  # if the current node is a word
			words.append(prefix)  # Then, append the prefix (as a word) to the list of possible words autocompleted
		for c in node.children:  # If not, continue to explore the children of the node (following letters) until there are no more children
			self.dfs_recur(node.children[c], prefix + c, words)  # update the prefix by adding the current level letter and continue the search
		# * The DFS will finished when there no more node to explore *

	def dfs_iter(self, node, prefix, words):
		stack = [(node, prefix)]
		while len(stack):
			(node, prefix) = stack.pop()
			if node.is_word: # if the current node is a word
				words.append(prefix)  # Then, append the prefix (as a word) to the list of possible words autocompleted
			for c in node.children:  # If not, continue to explore the children of the node (following letters) until there are no more children
				stack.append((node.children[c], prefix + c))  # update the prefix by adding the current level letter and and push the letter node into the stack

s = Solution()
s.build(['dog', 'dark', 'cat', 'door', 'dodge'])
print(s.autocomplete('do'))
# ['dog', 'door', 'dodge']

