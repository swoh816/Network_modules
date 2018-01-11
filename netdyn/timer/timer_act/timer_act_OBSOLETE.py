import numpy as np
import random as rd

def timer_thr_dyn(G, frac_or_abs, async_frac=None): # 0 < async_frac < 1: fraction, 1 < async_frac: absolute number of nodes are selected.
	sum_neighbor_state = {}
	size_of_net = len(G)
	how_many_nodes_to_update = size_of_net # if async_frac in none, do synchronous update.
		
	if not async_frac is None:
		if async_frac < 1:
			how_many_nodes_to_update = int(round(len(G)*async_frac))
		elif async_frac >= 1:
			how_many_nodes_to_update = async_frac
	
	node_list = G.nodes()
	rd.shuffle(node_list)
	selection_of_nodes = node_list[:how_many_nodes_to_update]
	
	if frac_or_abs == 'frac': # fractional threshold model.
		for i in selection_of_nodes:
			sum_neighbor_state[i] = 0
			for j in G[i].keys():
				sum_neighbor_state[i] = sum_neighbor_state[i] + G.node[j]['state']
		for i in selection_of_nodes:
			if len(G[i])>0:
				if float(sum_neighbor_state[i])/float(len(G[i])) >= G.node[i]['threshold']:
					if G.node[i]['timer'] <= 0:
						G.node[i]['state'] = 1
					elif G.node[i]['timer'] > 0:
						G.node[i]['timer'] = G.node[i]['timer'] - 1
			else:
				G.node[i]['state'] = G.node[i]['state']


	#def abs_thr(G, node_Phi):
	elif frac_or_abs == 'abs':
		for i in G.nodes():
			sum_neighbor_state[i] = 0
			for j in G[i].keys():
				sum_neighbor_state[i] = sum_neighbor_state[i] + G.node[j]
		for i in G.nodes():
			if len(G[i])>0:
				if sum_neighbor_state[i]>=node_Phi[i]:
					if node_time[i] <= 0:
						G.node[i] = 1
					elif node_time[i] > 0:
						node_time[i] = node_time[i] - 1

			else:
				G.node[i] = G.node[i]
