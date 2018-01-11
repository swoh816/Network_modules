# Test if the ensemble average of assorativity of networks matches with a given assortivity.

import assortative_network as asso
import networkx as nx
import random as rd
import pickle
import time

network_Size = 10000
mean_Degree = 5.0
number_of_Community = 2.0

assortativity_list = []

start_time = time.clock()
for i in xrange(100):
	G = nx.fast_gnp_random_graph(network_Size, mean_Degree/network_Size)
	node_list = G.nodes()
	rd.shuffle(node_list)

	number_of_node_in_community = 0
	for node in node_list:
		if number_of_node_in_community < network_Size/number_of_Community:
			G.node[node]['timer'] = 8
		else:
			G.node[node]['timer'] = 0
		number_of_node_in_community += 1

	asso.newman_assortative_network_limit(G, number_of_Community, 0.4, 'timer', 1000, 1e-3)
	assortativity_list.append(float(asso.attribute_assortativity_coefficient(G, 'timer')))

pickle.dump(assortativity_list, open('./result.txt', 'wb'))
pickle.dump(time.clock() - start_time, open('./elapsed_time.txt', 'wb'))
