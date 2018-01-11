import networkx as nx
import random as rd
import itertools


### James's configuration model of clique-based graph is constructed as follows: (from "Bond percolation on a class of clustered frandom networks", PRE (2009))
#each node is a member of at most one clique, and so the network can be decomposed into _DISJOINT CLIQUES_ which are linked together by the set of external links. If each clique is regarded as a supernode, then realizations of the random network maybe generated by conncting together randomly chosen pairs of the external link stubs as in the configuration model for standrard random networks.






def random_clique_graph(joint_degree_sequence, clique_size, create_using=None, seed=None):
	
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

	if len(ilist)%2 != 0 or len(slist)%clique_size != 0:
		raise nx.NetworkXError('Invalid degree sequence')

	rd.shuffle(ilist)
	rd.shuffle(slist)
	while ilist:
		G.add_edge(ilist.pop(),ilist.pop())
	while slist:
		clique_group = []
		for clique_member in range(clique_size):
			clique_group.append(slist.pop())
		edges = itertools.combinations(clique_group, 2)
		G.add_edges_from(edges)
			
	G.name = "random_clustered %d nodes %d edges"%(G.order(),G.size())
	return G

## 'triangle_proportion' decides the probability of having triangle for a node with degree larger than 1.

def single_clique_configuration(deg_seq, clique_profile): # clique_profile: list of list elements where a list element is (clique_size, proportion of the clique).
	number_of_nodes = len(deg_seq)
	clique_size = clique_profile[0]
	clique_proportion = clique_profile[1]
	clique_degree_sequence = []
	while deg_seq:
		clique_degree = 0
		single_edge_degree_of_selected_node = deg_seq.pop()
		#~ if single_edge_degree_of_selected_node > 1:
		number_of_iteration = single_edge_degree_of_selected_node/(clique_size - 1)
		for iteration in range(number_of_iteration):
			if clique_proportion > rd.random():
				#~ print 'wow'
				clique_degree += 1
				single_edge_degree_of_selected_node -= clique_size - 1 # A node in a clique has the number of 'internal' links that is same as clique_size - 1.

		clique_degree_sequence.append([single_edge_degree_of_selected_node, clique_degree])
		#print [single_edge_degree_of_selected_node, triangular_degree]
	
	#### Add more edges if the sum of all single edges are not even, and add more triangles if the sum of all triangles are not divisible by 3. ###
	single_degree_list = [clique_degree_sequence[i][0] for i in range(number_of_nodes)]
	while sum(single_degree_list)%2 != 0:
		#~ print 'not enough single edge'
		randomly_chosen_node = rd.randint(0, number_of_nodes - 1)
		clique_degree_sequence[randomly_chosen_node][0] += 1
		single_degree_list = [clique_degree_sequence[i][0] for i in range(number_of_nodes)]

	clique_degree_list = [clique_degree_sequence[i][1] for i in range(number_of_nodes)]
	while sum(clique_degree_list)%clique_size != 0:
		#~ print 'not enough single edge'
		randomly_chosen_node = rd.randint(0, number_of_nodes - 1)
		clique_degree_sequence[randomly_chosen_node][1] += 1
		clique_degree_list = [clique_degree_sequence[i][1] for i in range(number_of_nodes)]

	G = random_clique_graph(clique_degree_sequence, clique_size)

	#### Remove self edges and multi edges. ####
	G = nx.Graph(G)
	G.remove_edges_from(G.selfloop_edges())

	return G
	






#~ def james_clique_graph(clique):

def james_clique_graph(edge_cluster_pair_list):
	
	edge_list = []
	clique_list = []

	for node in G:
		while edge_cluster_pair_list:
			edge_cluster_pair_list.pop()
			
			edge_list.append([0])
			clique_list.append(edge_cluster_pair_list[i][1])
