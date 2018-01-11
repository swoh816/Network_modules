def thr_dyn(G, phi, act_node_Phi, deact_node_Phi, node_time):
	total_neighbor_state = {}
	if phi<1:
#def frac_thr(G, node_Phi):
		for i in G.nodes():
			total_neighbor_state[i] = 0
			for j in G[i].keys():
				if G.node[j] != 0.5:
					total_neighbor_state[i] = total_neighbor_state[i] + G.node[j]
		for i in G.nodes():
			if len(G[i])>0:
				if node_time[i] > 0:
					node_time[i] = node_time[i] - 1
				elif node_time[i] <= 0:
					if float(total_neighbor_state[i])/float(len(G[i]))> act_node_Phi[i]:
						if float(total_neighbor_state[i])/float(len(G[i])) < 1-deact_node_Phi[i]:
							G.node[i] = 0.5
				
						else:
							G.node[i] = 1
					elif float(total_neighbor_state[i])/float(len(G[i])) < 1-deact_node_Phi[i]:
						G.node[i] = 0

			else:
				G.node[i] = G.node[i]

#def abs_thr(G, node_Phi):


	else:
		for i in G.nodes():
			total_neighbor_state[i] = 0
			for j in G[i].keys():
				total_neighbor_state[i] = total_neighbor_state[i] + G.node[j]
		for i in G.nodes():
			if len(G[i])>0:
				if len(G[i])-total_neighbor_state[i] > node_Phi[i]:
					G.node[i] = 0

			else:
				G.node[i] = G.node[i]
