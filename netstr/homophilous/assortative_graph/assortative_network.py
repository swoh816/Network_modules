import random as rd
import networkx as nx
import numpy as np


def attribute_assortativity_coefficient(G, nodal_attribute):
	mixing_dict = nx.attribute_mixing_dict(G, nodal_attribute)
	total_sum_of_degree = float(2*G.size())
		
	sum_e_ii = 0
	for row in mixing_dict:
		column = row
		sum_e_ii += mixing_dict[row][column]/total_sum_of_degree
	
	sum_e_ij = 0
	for row in mixing_dict:
		sum_e_ij += sum(np.asarray(mixing_dict[row].values())/total_sum_of_degree)**2 # (\sum_i e_ij)**2 as a_i == b_i for undirected graph.
	
	return (sum_e_ii - sum_e_ij)/(1 - sum_e_ij)
	

def newman_assortative_network_limit(G, number_of_Community, mixing_dict, nodal_attribute, number_of_iterations, accuracy):
	#### READTHIS #####
	# Nodal attributes should be distributed randomly throughout the nodes.
	# Example)
	#~ node_list = G.nodes()
	#~ rd.shuffle(node_list)
	#~ community_Size = network_Size/number_of_Community
	#~ for count, node in enumerate(node_list):
		#~ if count/int(community_Size) == 0:
			#~ G.node[node]['timer'] = 3
		#~ elif count/int(community_Size) == 1:
			#~ G.node[node]['timer'] = 6
		#~ elif count/int(community_Size) == 2:
			#~ G.node[node]['timer'] = 9
		#~ elif count/int(community_Size) == 3:
			#~ G.node[node]['timer'] = 12

	# Calculate assortativity
	sum_e_ii = 0
	for row in mixing_dict:
		column = row
		sum_e_ii += mixing_dict[row][column]
	sum_e_ij = 0
	for row in mixing_dict:
		sum_e_ij += sum(np.asarray(mixing_dict[row].values()))**2 # (\sum_i e_ij)**2 as a_i == b_i for undirected graph.
	assortativity = (sum_e_ii - sum_e_ij)/(1 - sum_e_ij)
	
	while 1:
		list_of_assortativity = []
		for i in xrange(number_of_iterations):
		# Rewire until you find two distinctive edges that have no overlapping node
			while 1:
				random_edge_1 = G.edges()[rd.randint(0,G.size()-1)]
				random_edge_2 = G.edges()[rd.randint(0,G.size()-1)]
				if random_edge_1[0] not in G[random_edge_2[0]] and random_edge_1[0] not in G[random_edge_2[1]]:
					if random_edge_1[1] not in G[random_edge_2[0]] and random_edge_1[1] not in G[random_edge_2[1]]:
						break

			timer_random_edge_1_node_1 = G.node[random_edge_1[0]]['timer']
			timer_random_edge_1_node_2 = G.node[random_edge_1[1]]['timer']
			timer_random_edge_2_node_1 = G.node[random_edge_2[0]]['timer']
			timer_random_edge_2_node_2 = G.node[random_edge_2[1]]['timer']
		
			frac_1_1_to_1_2 = mixing_dict[timer_random_edge_1_node_1][timer_random_edge_1_node_2]
			frac_1_1_to_2_1 = mixing_dict[timer_random_edge_1_node_1][timer_random_edge_2_node_1]
			frac_2_2_to_2_1 = mixing_dict[timer_random_edge_2_node_2][timer_random_edge_2_node_1]
			frac_2_2_to_1_2 = mixing_dict[timer_random_edge_2_node_2][timer_random_edge_1_node_2]
			
			if frac_1_1_to_1_2*frac_2_2_to_2_1 == 0:
				if frac_1_1_to_2_1*frac_2_2_to_1_2 != 0:
					G.remove_edges_from([random_edge_1, random_edge_2])
					G.add_edges_from([(random_edge_1[0], random_edge_2[0]), (random_edge_1[1],random_edge_2[1])])				
			else:
				if rd.random() < (frac_1_1_to_2_1*frac_2_2_to_1_2)/(frac_1_1_to_1_2*frac_2_2_to_2_1):
					G.remove_edges_from([random_edge_1, random_edge_2])
					G.add_edges_from([(random_edge_1[0], random_edge_2[0]), (random_edge_1[1],random_edge_2[1])])
		
			list_of_assortativity.append(attribute_assortativity_coefficient(G,'timer'))
		    
		# Check until assortativity converges
		if abs(np.mean(list_of_assortativity) - assortativity) < accuracy:
			break




def kristina_assortative_network(G, assortativity, nodal_attribute):
	past_assortativity = attribute_assortativity_coefficient(G,nodal_attribute)
	while 1:
		while 1:
			random_edge_1 = G.edges()[rd.randint(0,G.size()-1)]
			random_edge_2 = G.edges()[rd.randint(0,G.size()-1)]
			if random_edge_1[0] not in G[random_edge_2[0]] and random_edge_1[0] not in G[random_edge_2[1]]:
				if random_edge_1[1] not in G[random_edge_2[0]] and random_edge_1[1] not in G[random_edge_2[1]]:
					break
		previous_G = G.copy()
		
		G.remove_edges_from([random_edge_1, random_edge_2])
		G.add_edges_from([(random_edge_1[0], random_edge_2[0]), (random_edge_1[1],random_edge_2[1])])
		if assortativity > 0:
			if attribute_assortativity_coefficient(G,nodal_attribute) > past_assortativity:
				past_assortativity = attribute_assortativity_coefficient(G,nodal_attribute)
				if past_assortativity >= assortativity:
					return G
					break
			else:
				G = previous_G
		else:
			if attribute_assortativity_coefficient(G,nodal_attribute) < past_assortativity:
				past_assortativity = attribute_assortativity_coefficient(G,nodal_attribute)
				if past_assortativity <= assortativity:
					return G
					break
			else:
				G = previous_G




def kristina_assortative_network_2(G, assortativity, nodal_attribute, accuracy):
    network_assortativity_past = attribute_assortativity_coefficient(G,nodal_attribute)
    while 1:
        while 1:
            random_edge_1 = G.edges()[rd.randint(0,G.size()-1)]
            random_edge_2 = G.edges()[rd.randint(0,G.size()-1)]
            if random_edge_1[0] not in G[random_edge_2[0]] and random_edge_1[0] not in G[random_edge_2[1]]:
                if random_edge_1[1] not in G[random_edge_2[0]] and random_edge_1[1] not in G[random_edge_2[1]]:
                    break

        G.remove_edges_from([random_edge_1, random_edge_2])
        G.add_edges_from([(random_edge_1[0], random_edge_2[0]), (random_edge_1[1],random_edge_2[1])])

        network_assortativity_new = attribute_assortativity_coefficient(G,nodal_attribute)
        if assortativity >= 0:
            if (1 + accuracy)*assortativity > network_assortativity_new >= (1 - accuracy)*assortativity:
                break
            elif network_assortativity_new < (1 - accuracy)*assortativity:
                if network_assortativity_new > network_assortativity_past:
                    network_assortativity_past = network_assortativity_new
                    continue
                else:
                    G.remove_edges_from([(random_edge_1[0], random_edge_2[0]), (random_edge_1[1],random_edge_2[1])])
                    G.add_edges_from([random_edge_1, random_edge_2])                    
            elif network_assortativity_new > (1 + accuracy)*assortativity:
                if network_assortativity_new < network_assortativity_past:
                    network_assortativity_past = network_assortativity_new
                    continue
                else:
                    G.remove_edges_from([(random_edge_1[0], random_edge_2[0]), (random_edge_1[1],random_edge_2[1])])
                    G.add_edges_from([random_edge_1, random_edge_2])
            
        if assortativity < 0:
            if (1 + accuracy)*assortativity <= network_assortativity_new < (1 - accuracy)*assortativity:
                break
            elif network_assortativity_new > (1 - accuracy)*assortativity:
                if network_assortativity_new < network_assortativity_past:
                    network_assortativity_past = network_assortativity_new
                    continue
                else:
                    G.remove_edges_from([(random_edge_1[0], random_edge_2[0]), (random_edge_1[1],random_edge_2[1])])
                    G.add_edges_from([random_edge_1, random_edge_2])                    
            elif network_assortativity_new < (1 + accuracy)*assortativity:
                if network_assortativity_new > network_assortativity_past:
                    network_assortativity_past = network_assortativity_new
                    continue
                else:
                    G.remove_edges_from([(random_edge_1[0], random_edge_2[0]), (random_edge_1[1],random_edge_2[1])])
                    G.add_edges_from([random_edge_1, random_edge_2])



#~ def assortative_network(G, assortativity, nodal_attribute):
	#~ while 1:
		#~ while 1:
			#~ random_edge_1 = G.edges()[rd.randint(0,G.size()-1)]
			#~ random_edge_2 = G.edges()[rd.randint(0,G.size()-1)]
			#~ if random_edge_1[0] not in G[random_edge_2[0]] and random_edge_1[0] not in G[random_edge_2[1]]:
				#~ if random_edge_1[1] not in G[random_edge_2[0]] and random_edge_1[1] not in G[random_edge_2[1]]:
					#~ break
		#~ 
		#~ timer_random_edge_1_node_1 = G.node[random_edge_1[0]][nodal_attribute]
		#~ timer_random_edge_1_node_2 = G.node[random_edge_1[1]][nodal_attribute]
		#~ timer_random_edge_2_node_1 = G.node[random_edge_2[0]][nodal_attribute]
		#~ timer_random_edge_2_node_2 = G.node[random_edge_2[1]][nodal_attribute]
		#~ 
		#~ if timer_random_edge_1_node_1 == timer_random_edge_1_node_2:
			#~ frac_1_1_to_1_2 = assortativity
		#~ else:
			#~ frac_1_1_to_1_2 = 1 - assortativity
		#~ if timer_random_edge_1_node_1 == timer_random_edge_2_node_1:
			#~ frac_1_1_to_2_1 = assortativity
		#~ else:
			#~ frac_1_1_to_2_1 = 1 - assortativity
		#~ if timer_random_edge_2_node_2 == timer_random_edge_2_node_1:
			#~ frac_2_2_to_2_1 = assortativity
		#~ else:
			#~ frac_2_2_to_2_1 = 1 - assortativity
		#~ if timer_random_edge_2_node_2 == timer_random_edge_1_node_2:
			#~ frac_2_2_to_1_2 = assortativity
		#~ else:
			#~ frac_2_2_to_1_2 = 1 - assortativity
		#~ 
		#~ if rd.random() < (frac_1_1_to_2_1*frac_2_2_to_1_2)/(frac_1_1_to_1_2*frac_2_2_to_2_1):
			#~ G.remove_edges_from([random_edge_1, random_edge_2])
			#~ G.add_edges_from([(random_edge_1[0], random_edge_2[0]), (random_edge_1[1],random_edge_2[1])])
		#~ 
		#~ if attribute_assortativity_coefficient(G,nodal_attribute) >= assortativity:
			#~ break
