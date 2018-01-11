import networkx as nx
import random as rd

## 'triangle_proportion' decides the probability of having triangle for a node with degree larger than 1.

def newman_clustering_configuration(deg_seq, triangle_proportion):
	number_of_nodes = len(deg_seq)
	triangular_degree_sequence = []
	while deg_seq:
		triangular_degree = 0
		single_edge_degree_of_selected_node = deg_seq.pop()
		#~ if single_edge_degree_of_selected_node > 1:
		number_of_iteration = single_edge_degree_of_selected_node/2
		for iteration in range(number_of_iteration):
			if triangle_proportion > rd.random():
				#~ print 'wow'
				triangular_degree += 1
				single_edge_degree_of_selected_node -= 2
				

		triangular_degree_sequence.append([single_edge_degree_of_selected_node, triangular_degree])
		#print [single_edge_degree_of_selected_node, triangular_degree]
	

	#### Add more edges if the sum of all single edges are not even, and add more triangles if the sum of all triangles are not divisible by 3. ###
	single_degree_list = [triangular_degree_sequence[i][0] for i in range(number_of_nodes)]
	while sum(single_degree_list)%2 != 0:
		#~ print 'not enough single edge'
		randomly_chosen_node = rd.randint(0, number_of_nodes - 1)
		triangular_degree_sequence[randomly_chosen_node][0] += 1
		single_degree_list = [triangular_degree_sequence[i][0] for i in range(number_of_nodes)]

	triangular_degree_list = [triangular_degree_sequence[i][1] for i in range(number_of_nodes)]
	while sum(triangular_degree_list)%3 != 0:
		#~ print 'not enough single edge'
		randomly_chosen_node = rd.randint(0, number_of_nodes - 1)
		triangular_degree_sequence[randomly_chosen_node][1] += 1
		triangular_degree_list = [triangular_degree_sequence[i][1] for i in range(number_of_nodes)]

	G = nx.random_clustered_graph(triangular_degree_sequence)

	#### Remove self edges and multi edges. ####
	G = nx.Graph(G)
	G.remove_edges_from(G.selfloop_edges())

	return G
	

class square_sequence_class(object):
	def __init__(self, G):
		self.G = G

		self.triangle_list = {}
		self.triangle_details = {}
		for i in self.G:
			self.triangle_details[i] = []
			number_of_triangle = 0
			for j in self.G[i]:
				for k in self.G[j]:
					if k in self.G[i]:
						self.triangle_details[i].append([i, j, k])
						number_of_triangle += 1
			triangle_list[i] = number_of_triangle/2

	def get_triangle_list(self):
		return self.triangle_list
	def get_square_details(self):
		return self.triangle_details

#### If you would like to get the list of number of squares of nodes, then you would do
#~ 		square_graph.square_sequence_class(G).get_square_list()
#~ 	similarly,
#~ 		square_graph.square_sequence_class(G).get_square_details()








#~ def triangle_sequence(G):
	#~ triangle_list = {}
	#~ for i in G:
		#~ number_of_triangle = 0
		#~ for j in G[i]:
			#~ for k in G[j]:
				#~ if k in G[i]:
					#~ number_of_triangle += 1
		#~ triangle_list[i] = number_of_triangle/2
#~ 
	#~ return triangle_list


# An element of degree sequence in nx.random_clustered_graph is composed of [s, t] where s: single edge, t: triangle. The degree of the node is s + 2t.

