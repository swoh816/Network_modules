#### Make a configuraiton model with power-law degree distribution ####
import os, sys
import networkx as nx
sys.path.append(os.path.abspath('../../../'))
import functions.distribution_functions.power_law_gen.power_law_gen as pl_gen

def power_law_graph(x_min, power_law_exponent, size_of_net):

	degree_sequence = [1]
	#~ G = nx.fast_gnp_random_graph(1, 1)
	#~ while min(G.degree().values()) != x_min:
	while sum(degree_sequence)%2 == 1:
		degree_sequence = []
		for i in range(size_of_net):
			degree_sequence.append(int(pl_gen.random_power_no(x_min, power_law_exponent)))
		
	G = nx.configuration_model(degree_sequence)
	G=nx.Graph(G)
	G.remove_edges_from(G.selfloop_edges())

	return G


def power_law_graph_cuts(size_of_net, x_min, power_law_exponent):
	degree_sequence = []
	norm_const = float(size_of_net)/sum([var**(-power_law_exponent) for var in range(x_min, size_of_net)]) #The maximum degree fo an undirected simple graph is N-1 where N is size_of_net.
	for i in range(x_min, size_of_net):
		for j in range(int(round(norm_const*i**(-power_law_exponent)))):
			degree_sequence.append(i)
	if sum(degree_sequence)%2 != 0:
		if x_min%2 != 0:
			degree_sequence.append(x_min)
		else:
			degree_sequence.append(x_min+1)
	
	G = nx.configuration_model(degree_sequence)
	G=nx.Graph(G)
	G.remove_edges_from(G.selfloop_edges())

	return G

