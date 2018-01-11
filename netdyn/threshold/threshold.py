import numpy as np

def thr_dyn(G, node_Phi):
	total_neighbor_state = {}
	phi = np.mean(node_Phi)
	if phi<1:
#def frac_thr(G, node_Phi):
		for i in G.nodes():
			total_neighbor_state[i] = 0
			for j in G[i].keys():
				total_neighbor_state[i] = total_neighbor_state[i] + G.node[j]
		for i in G.nodes():
			if len(G[i])>0:
				if float(total_neighbor_state[i])/float(len(G[i]))>node_Phi[i]:
					G.node[i] = 1

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
				if total_neighbor_state[i]>node_Phi[i]:
					G.node[i] = 1

			else:
				G.node[i] = G.node[i]
