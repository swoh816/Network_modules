import networkx as nx
import random as rd

## 'triangle_proportion' decides the probability of having triangle for a node with degree larger than 1.

class newman_clustering_configuration(object):
	def __init__(self, deg_seq, triangle_proportion):

		self.deg_seq = deg_seq
		self.triangle_proportion = triangle_proportion
		
		number_of_nodes = len(self.deg_seq)
		triangular_degree_sequence = []
		while self.deg_seq:
			triangular_degree = 0
			single_edge_degree_of_selected_node = self.deg_seq.pop()
			if single_edge_degree_of_selected_node > 1:
				number_of_iteration = single_edge_degree_of_selected_node/2
				for iteration in range(number_of_iteration):
					if self.triangle_proportion > rd.random():
						#~ print 'wow'
						triangular_degree += 1
						single_edge_degree_of_selected_node -= 2
					

			triangular_degree_sequence.append([single_edge_degree_of_selected_node, triangular_degree])
			#print [single_edge_degree_of_selected_node, triangular_degree]
		

		#### Add more edges if the sum of all single edges are not even, and add more triangles if the sum of all triangles are not divisible by 3. ###
		single_degree_list = [triangular_degree_sequence[i][0] for i in range(number_of_nodes)]
		while sum(single_degree_list)%2 != 0:
			print 'not enough single edge'
			randomly_chosen_node = rd.randint(0, number_of_nodes - 1)
			triangular_degree_sequence[randomly_chosen_node][0] += 1
			single_degree_list = [triangular_degree_sequence[i][0] for i in range(number_of_nodes)]

		triangular_degree_list = [triangular_degree_sequence[i][1] for i in range(number_of_nodes)]
		while sum(triangular_degree_list)%3 != 0:
			print 'not enough single edge'
			randomly_chosen_node = rd.randint(0, number_of_nodes - 1)
			triangular_degree_sequence[randomly_chosen_node][1] += 1
			triangular_degree_list = [triangular_degree_sequence[i][1] for i in range(number_of_nodes)]

		G = nx.random_clustered_graph(triangular_degree_sequence)

		#### Remove self edges and multi edges. ####
		G = nx.Graph(G)
		G.remove_edges_from(G.selfloop_edges())

		self.triangular_degree_list = triangular_degree_list
		self.single_degree_list = single_degree_list
	
	
	
	def get_triangular_degree_list(self):
		return self.triangular_degree_list

	def get_single_degree_list(self):
		return self.single_degree_list
		


	
		#~ return G


	# An element of degree sequence in nx.random_clustered_graph is composed of [s, t] where s: single edge, t: triangle. The degree of the node is s + 2t.
