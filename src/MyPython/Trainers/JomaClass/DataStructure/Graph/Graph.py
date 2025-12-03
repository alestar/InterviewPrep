from JomaClass.DataStructure.List.LinkedListStack import LinkedListStack
from JomaClass.DataStructure.Queue.LinkedListQueue import LinkedListQueue



class GraphVertex:

	def __init__(self, val):
		self.val = val
		#  self.edges = LinkedListHeadTail()  # Adjacency List / Edges
		self.edges = {}


class Graph:

	def __init__(self):
		self.vertices = {}

	def build_graph_from_dic(self, dic):
		return

	def add_vertex(self, value):
		return

	def add_vertices(self, values):
		return

	def add_edge(self, src, dest):
		vertex_src = GraphVertex(src)
		if src not in self.vertices:
			self.vertices[src] = vertex_src
		else:
			vertex_src = self.vertices[src]

		vertex_dest = GraphVertex(dest)
		if dest not in self.vertices:
				self.vertices[dest] = vertex_dest
		else:
			vertex_dest = self.vertices[dest]

		vertex_src.edges[dest] = vertex_dest
		vertex_dest.edges[src] = vertex_src

	# Function to print the graph
	def print_graph(self):
		for key in self.vertices:
			print("Adjacency list of vertex {}: ".format(key), end="")
			vertex = self.vertices[key]
			for value in vertex.edges.values():
				print(" -> {}".format(value.val), end="")
			print(" \n")


def bfs_traverse(start):
	print("Traversing BFS inter")
	explore = LinkedListQueue()  # Use a Queue for vertex that has not been visited yet and are pending to explore
	explore.enqueue(start)
	visited = {start.val: start}  # Use a Dictionary/Hash table to avoid revisiting neighbors (avoid g loop)
	while not explore.is_empty():
		v = explore.dequeue()
		print("Looking at: " + str(v.val))
		for neighbor in v.edges.values():
			if neighbor.val not in visited:
				visited[neighbor.val] = neighbor
				explore.enqueue(neighbor)


def dfs_traverse_iterative(start):
	print("Traversing DFS inter: ")
	explore = LinkedListStack()
	explore.push(start)


	visited = {start.val: start}  # Discovered Dictionary to avoid graph node cycles
	while not explore.is_empty():
		v = explore.pop()
		print("Looking at: " + str(v.val))

		for neighbor in reversed(v.edges.values()):
			if neighbor.val not in visited:
				explore.push(neighbor)
				visited[neighbor.val] = neighbor

def dfs_traverse_recur(vertex): # Use the Function Call Stack instead of creating a new object
	print("Traversing DFS recur: ")
	dfs_traverse_recur_helper(vertex, {})

def dfs_traverse_recur_helper(vertex, discovered): # Use the Function Call Stack instead of creating a new object
	print("Looking at: " + str(vertex.val))
	discovered[vertex.val] = vertex
	for neighbor in vertex.edges.values():
		if neighbor.val not in discovered:
			dfs_traverse_recur_helper(neighbor, discovered)
	# vertex is finished when there are no more neighbors to explore

# Graph
#       0
#      / \
#     1 - 4
#    / \ /
#   2 - 3

# Driver program to the above graph class
if __name__ == "__main__":
	graph = Graph()
	graph.add_edge(0, 1)
	graph.add_edge(0, 4)
	graph.add_edge(1, 2)
	graph.add_edge(1, 3)
	graph.add_edge(1, 4)
	graph.add_edge(2, 3)
	graph.add_edge(3, 4)
	graph.print_graph()
	bfs_traverse(graph.vertices[0])
	dfs_traverse_recur(graph.vertices[0])
	dfs_traverse_iterative(graph.vertices[0])


