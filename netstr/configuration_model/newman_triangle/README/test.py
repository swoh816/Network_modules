#### Test the change of global clustering coefficient (average over all local clusterings) by increasing triangle_proportion. ####

import newman_triangle as nt
import networkx as nx
import numpypy as np
import pickle

import sys
import os
sys.path.append(os.path.abspath('../../../'))

import functions.distribution_functions.poisson_dist.poisson as pd

### try 3-regular graphs ###
tri_proport_list = [i*0.02 for i in range(51)]
global_clustering_list = []

for tri_proport in tri_proport_list:
	clustering_list = []
	for i in range(1000):
		#### 3-regular graph ####
		#~ deg_seq = [3 for i in range(10000)]
		
		#### er-graph with mean degree 3 ####
		deg_seq = [pd.poisson_random_variable(3) for i in range(10000)]
		G = nt.newman_clustering_configuration(deg_seq, tri_proport)
		clustering_list.append(np.mean(nx.clustering(G).values()))
	global_clustering_list.append(np.mean(clustering_list))

pickle.dump(np.array(global_clustering_list).tolist(), open('./result_er.txt', 'wb'))
