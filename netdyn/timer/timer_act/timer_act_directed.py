import numpy as np
import random as rd

def timer_thr_dyn(G, unadopted_nodes, frac_or_abs): # 0 < async_frac < 1: fraction, 1 < async_frac: absolute number of nodes are selected.
	updated_nodes = []
	ticking_nodes = []
	
	sum_neighbor_state = {}
	# size_of_net = len(G)
	# how_many_nodes_to_update = size_of_net # if async_frac in none, do synchronous update.
		
	# if not async_frac is None:
	# 	if async_frac < 1:
	# 		how_many_nodes_to_update = int(round(len(G)*async_frac))
	# 	elif async_frac >= 1:
	# 		how_many_nodes_to_update = async_frac
	
	rd.shuffle(unadopted_nodes)
	# selection_of_nodes = unadopted_nodes[:how_many_nodes_to_update]
	
	if frac_or_abs == 'frac': # fractional threshold model.
		for i in unadopted_nodes:
			sum_neighbor_state[i] = 0
			for j in G.predecessors(i):
				sum_neighbor_state[i] = sum_neighbor_state[i] + G.node[j]['state']
                for i in unadopted_nodes: 
			if len(G.predecessors(i))>0:
				if float(sum_neighbor_state[i])/float(len(G.predecessors(i))) >= G.node[i]['threshold']:
					if G.node[i]['timer'] <= 0:
						G.node[i]['state'] = 1
						updated_nodes.append(i)
					elif G.node[i]['timer'] > 0:
						G.node[i]['timer'] = G.node[i]['timer'] - 1
						ticking_nodes.append(i)
			else:
				G.node[i]['state'] = G.node[i]['state']
			

	#def abs_thr(G, node_Phi):
	elif frac_or_abs == 'abs':
		for i in unadopted_nodes:
			sum_neighbor_state[i] = 0
			for j in G.predecessors(i):
				sum_neighbor_state[i] = sum_neighbor_state[i] + G.node[j]['state']
                for i in unadopted_nodes: 
			if len(G.predecessors(i))>0:
				if float(sum_neighbor_state[i]) >= G.node[i]['threshold']:
					if G.node[i]['timer'] <= 0:
						G.node[i]['state'] = 1
						updated_nodes.append(i)
					elif G.node[i]['timer'] > 0:
						G.node[i]['timer'] = G.node[i]['timer'] - 1
						ticking_nodes.append(i)
			else:
				G.node[i]['state'] = G.node[i]['state']
        return updated_nodes, ticking_nodes
