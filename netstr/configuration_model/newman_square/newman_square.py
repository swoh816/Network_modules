import networkx as nx
import random as rd

## 'triangle_proportion' decides the probability of having triangle for a node with degree larger than 1.

def random_square_graph(joint_degree_sequence, create_using=None, seed=None):
	
	if create_using is None:
		create_using = nx.MultiGraph()
	elif create_using.is_directed():
		raise nx.NetworkXError("Directed Graph not supported")

	if not seed is None:
		rd.seed(seed)

	### joint_degree_sequence: list of integer pairs; [#single_edge, #square]
	joint_degree_sequence = list(joint_degree_sequence)

	N = len(joint_degree_sequence)
	G = nx.empty_graph(N,create_using)

	ilist = []
	slist = []
	for n in G:
		degrees = joint_degree_sequence[n]
		for icount in range(degrees[0]):
			ilist.append(n)
		for tcount in range(degrees[1]):
			slist.append(n)

	if len(ilist)%2 != 0 or len(slist)%4 != 0:
		raise nx.NetworkXError('Invalid degree sequence')

	rd.shuffle(ilist)
	rd.shuffle(slist)
	while ilist:
		G.add_edge(ilist.pop(),ilist.pop())
	while slist:
		n1 = slist.pop()
		n2 = slist.pop()
		n3 = slist.pop()
		n4 = slist.pop()
		G.add_edges_from([(n1,n2),(n1,n3),(n2,n4),(n3,n4)])
	G.name = "random_clustered %d nodes %d edges"%(G.order(),G.size())
	return G

	
	


def newman_square_configuration(deg_seq, square_proportion):
	number_of_nodes = len(deg_seq)
	square_degree_sequence = []
	while deg_seq:
		square_degree = 0
		single_edge_degree_of_selected_node = deg_seq.pop()
		if single_edge_degree_of_selected_node > 1:
			number_of_iteration = single_edge_degree_of_selected_node/2 # Not 3 but 2, because two of a node's edges are used to create a square; a node in a square has two edges in the square.
			for iteration in range(number_of_iteration):
				if square_proportion > rd.random():
					#~ print 'wow'
					square_degree += 1
					single_edge_degree_of_selected_node -= 2
				

		square_degree_sequence.append([single_edge_degree_of_selected_node, square_degree])
		#print [single_edge_degree_of_selected_node, square_degree]
	

	#### Add more edges if the sum of all single edges are not even, and add more squares if the sum of all squares are not divisible by 4. ###
	single_degree_list = [square_degree_sequence[i][0] for i in range(number_of_nodes)]
	while sum(single_degree_list)%2 != 0:
		#~ print 'not enough single edge'
		randomly_chosen_node = rd.randint(0, number_of_nodes - 1)
		square_degree_sequence[randomly_chosen_node][0] += 1
		single_degree_list = [square_degree_sequence[i][0] for i in range(number_of_nodes)]

	square_degree_list = [square_degree_sequence[i][1] for i in range(number_of_nodes)]
	while sum(square_degree_list)%4 != 0:
		#~ print 'not enough single edge'
		randomly_chosen_node = rd.randint(0, number_of_nodes - 1)
		square_degree_sequence[randomly_chosen_node][1] += 1
		square_degree_list = [square_degree_sequence[i][1] for i in range(number_of_nodes)]

	G = random_square_graph(square_degree_sequence)

	#### Remove self edges and multi edges. ####
	G = nx.Graph(G)
	G.remove_edges_from(G.selfloop_edges())

	return G


class square_sequence_class(object):
	def __init__(self, G):
		self.G = G

		self.square_list = {}
		self.square_details = {}
		for i in self.G:
			self.square_details[i] = []
			number_of_square = 0
			for j in self.G[i]:
				for k in self.G[j]:
					if k not in self.G[i] and k != i:
						for l in self.G[k]:
							if l in self.G[i] and j not in self.G[l] and l != j:
								self.square_details[i].append([i, j, k, l])
								number_of_square += 1
			self.square_list[i] = number_of_square/2
	
	def get_square_list(self):
		return self.square_list
	def get_square_details(self):
		return self.square_details


#### If you would like to get the list of number of squares of nodes, then you would do
#~ 		square_graph.square_sequence_class(G).get_square_list()
#~ 	similarly,
#~ 		square_graph.square_sequence_class(G).get_square_details()










#~ def square_sequence(G):
	#~ square_list = {}
	#~ square_details = {}
	#~ for i in G:
		#~ square_details[i] = []
		#~ number_of_square = 0
		#~ for j in G[i]:
			#~ for k in G[j]:
				#~ if k not in G[i] and k != i:
					#~ for l in G[k]:
						#~ if l in G[i] and j not in G[l] and l != j:
							#~ square_details[i].append([i, j, k, l])
							#~ number_of_square += 1
		#~ square_list[i] = number_of_square/2
#~ 
	#~ return square_list, square_details
	





# An element of degree sequence in nx.random_clustered_graph is composed of [s, t] where s: single edge, t: triangle. The degree of the node is s + 2t.
