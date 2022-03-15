class Node:
	def __init__(self):
		self.count = 0
		# {'a': Node, 'b': Node, ...}
		self.children = {}


class Solution:
	def build(self, words):
		trie = Node()  # Star constructing the Trie with an empty node
		for word in words:
			curr = trie
			for c in word:
				if c not in curr.children:
					curr.children[c] = Node()  # if is a new letter, create a new node for it
				curr = curr.children[c]  # if is an existing letter point the curr node to it and continue iterating
				curr.count += 1
		self.trie = trie  # update the trie

	def shortest_unique_prefix_iter(self, words):
		prefixes = []  # List of possible unique prefix found on the Trie
		# Iterate though all the letters and verify that each exist in the Trie, until the last one
		for word in words:
			curr = self.trie  # Start with the root node (usually empty node in a Trie)
			prefix = ''
			for c in word:
				if curr.count == 1:
					break
				else:
					curr = curr.children[c]
					prefix += c
			prefixes.append(prefix)  # Explore and all shortest unique prefix found for each word
		return prefixes

	def shortest_unique_prefix_dfs(self):
		prefixes = []  # List of possible unique prefix found on the Trie
		# Iterate though all the letters and verify that each exist in the Trie, until the last one
		curr = self.trie  # Start with the root node (usually empty node in a Trie)
		prefix = ''
		self.dfs_recur(curr, prefix, prefixes)
		return prefixes

	def dfs_recur(self, node, prefix, words):
		if node.count == 1:  # if the current node is a word
			words.append(prefix)  # Then, append the prefix (as a word) to the list of possible words autocompleted
			return
		for c in node.children:  # If not, continue to explore the children of the node (following letters) until there are no more children
			self.dfs_recur(node.children[c], prefix + c,
						   words)  # update the prefix by adding the current level letter and continue the search
	# * The DFS will finished when there no more node to explore *


class Trie:
	def __init__(self):
		self.root = Node()

	def insert(self, word):
		curr = self.root

		for c in word:
			if c not in curr.children:
				curr.children[c] = Node()
			curr = curr.children[c]
			curr.count += 1

	def unique_prefix(self, word):
		node = self.root
		prefix = ''

		for c in word:
			if node.count == 1:
				return prefix
			else:
				node = node.children[c]
				prefix += c
		return prefix


def shortest_unique_prefix(words):
	trie = Trie()

	for word in words:
		trie.insert(word)

	unique_prefixes = []
	for word in words:
		unique_prefixes.append(trie.unique_prefix(word))

	return unique_prefixes


s = Solution()
s.build(['jon', 'john', 'jack', 'tech'])
print(s.shortest_unique_prefix_iter(['jon', 'john', 'jack', 'tech']))  # ['jon', 'joh', 'ja', t]
print(s.shortest_unique_prefix_dfs())  # ['jon', 'joh', 'ja', t]
print(shortest_unique_prefix(['jon', 'john', 'jack', 'tech']))  # ['jon', 'joh', 'ja', t]
