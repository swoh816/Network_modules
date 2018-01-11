import networkx as nx
import random as rd


def stochastic_block_model(total_number_of_nodes, number_of_groups, mean_degree, intra_edge_ratio): # inter_edge_ratio = 1 - intra_edge_ratio

	G = nx.Graph()
	G.add_nodes_from(range(total_number_of_nodes))
	
	node_group = {}
	for group in range(number_of_groups):
		node_group[group] = []
	
	for node in range(total_number_of_nodes):
		for group in range(number_of_groups):
			if node%number_of_groups == group:
				node_group[group].append(node)
		
	
	number_of_edges = total_number_of_nodes*mean_degree/2
	for i in range(number_of_edges):
		selected_group_1 = rd.randint(0, number_of_groups - 1)
		
		if intra_edge_ratio > rd.random(): #Prob. connecting intra-module.
			G.add_edge( rd.choice(node_group[selected_group_1]), rd.choice(node_group[selected_group_1]) )
		else:
			selected_group_2 = rd.randint(0, number_of_groups - 1)
			while selected_group_2 == selected_group_1:
				selected_group_2 = rd.randint(0, number_of_groups - 1)
			G.add_edge( rd.choice(node_group[selected_group_1]), rd.choice(node_group[selected_group_2]) )
		
	return G
