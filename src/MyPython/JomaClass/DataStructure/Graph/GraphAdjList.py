
"""
A Python program to demonstrate the adjacency
list representation of the graph
"""

# A class to represent the adjacency list of the node


class AdjNode:
	def __init__(self, data):
		self.vertex = data
		self.next = None


# A class to represent a graph. A graph
# is the list of the adjacency lists.
# Size of the array will be the no. of the
# vertices "V"
class Graph:
	def __init__(self, num_vertices):
		self.num_vertices = num_vertices
		self.graph = [None] * self.num_vertices

	# Function to add an edge in an undirected graph
	def add_edge(self, src, dest):
		# Adding the destiny node to the source node
		node_dest = AdjNode(dest)
		node_dest.next = self.graph[src]  # Point new node to the head node in edge list of src
		self.graph[src] = node_dest  # Add node_dest as and edge_node of src

		# Adding the source node to the destiny because is an undirected graph
		node_src = AdjNode(src)
		node_src.next = self.graph[dest]  # Point new node to the head node in edge list of dest
		self.graph[dest] = node_src  # Add node_src as and edge_node of dest

	# Function to print the graph
	def print_graph(self):
		for i in range(self.num_vertices):
			print("Adjacency list of vertex {}\n head".format(i), end="")
			temp = self.graph[i]
			while temp:
				print(" -> {}".format(temp.vertex), end="")
				temp = temp.next
			print(" \n")


# Driver program to the above graph class
if __name__ == "__main__":
	V = 5
	graph = Graph(V)
	graph.add_edge(0, 1)
	graph.add_edge(0, 4)
	graph.add_edge(1, 2)
	graph.add_edge(1, 3)
	graph.add_edge(1, 4)
	graph.add_edge(2, 3)
	graph.add_edge(3, 4)

	graph.print_graph()

