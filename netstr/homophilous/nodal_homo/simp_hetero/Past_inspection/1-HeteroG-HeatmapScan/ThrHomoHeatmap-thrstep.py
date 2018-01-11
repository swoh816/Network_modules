#!/usr/bin/python -tt

import networkx as nx
import random as rd
import sys
sys.path.append('/home/oh/Desktop/Simulations/MyModel/ThrHomo/DifferentThrHomo/StrHomo/TwoERGraph/1-TwoER-HeatmapScan/modules')

import matplotlib.pyplot as plt
import inspect
import time
import scipy.io
import os
import numpy as np

import imp

#two_er_graphs = imp.load_source('two_er_graphs.py', 'modules/two_er_graphs.py')
#threshold = imp.load_source('threshold.py', 'modules/threshold.py')
#clustering = imp.load_source('clustering.py', 'modules/clustering.py')
import two_er_graphs
import threshold

n1 = int(sys.argv[1])
z1 = int(sys.argv[2])

n2 = int(sys.argv[3])
z2 = int(sys.argv[4])

p = float(sys.argv[5]) # edge probability between two graphs

rho = float(sys.argv[6])
phi1 = float(sys.argv[7])
phi2 = float(sys.argv[8])

sig1 = float(sys.argv[9])
sig2 = float(sys.argv[10])

NO_Phi_realization = int(sys.argv[11])
MAX_Steps_to_cascade=int(sys.argv[12])
res_p=int(sys.argv[13])
res_Phi = int(sys.argv[14])
NO_realization_at_each_meandegree_step = int(sys.argv[15])



Filename_str = ''
for i in sys.argv:
	Filename_str = Filename_str+ '-' + i
Filename_str = Filename_str[3:]



NO_infected_nodes = {}

neighbor_Phi = {}

steps_to_cascade_at_each_realization = {}
mean_NO_steps_to_cascade_at_each_Z = []
edges_btn_neighbors = {}

local_clustering_coeffs = {}


node_Phi = {}
#z1_list = [float(Z1*x)/float(res) for x in range(res+1)] #Mean degrees are set constant.
#z2_list = [float(Z2*x)/float(res) for x in range(res+1)]

phi1_list = [float(phi1)*float(r)/float(res_Phi) for r in range(res_Phi+1)]
#phi2_list = [float(phi2)*float(r)/float(res_Phi) for r in range(res_Phi+1)] 

p_list = [float(p*x)/float(res_p) for x in range(res_p+1)]

final_value_at_each_realization = {} #'final_value = []' in previous version (list => dict)

current_path = os.getcwd()

data_path = current_path + '/Data/'
figure_path = current_path + '/Figures/'

if os.path.exists(data_path) == False:
	os.mkdir(data_path)


###################################	Save Structure	###################################

if os.path.exists(data_path + Filename_str + '.mat') == True:
	board = np.array(scipy.io.loadmat(data_path + Filename_str)['A']).tolist()
	order = sorted(enumerate(board))[-1][0]

else:
	board = []
	order = -1



#cascade model.
for phi in phi1_list[order+1:]:
#	mean_giant_component_size_at_degree = []
	final_mean_at_each_meandegree_step = []
	for p in p_list:
		steps_to_cascade_at_each_realization[p] = [] #

#		giant_component_size_at_degree = []
		for m in range(NO_realization_at_each_meandegree_step):

			NO_infected_nodes[m] = [] # 'data' in previous version. (global variable?)
			G = two_er_graphs.two_er_graphs(n1, z1, n2, z2, p, phi1, sig1, phi2, sig2)
#			Gcc = nx.connected_component_subgraphs(G)
#			giant_component_size_at_degree.append(len(Gcc[0].nodes()))


			######## Selective phi assignment ##########

			node_Phi = {}
			for i in G:
				if 'G1' in i:
					node_Phi[i] = rd.gauss(phi1, sig1)
				elif 'G2' in i:
					node_Phi[i] = rd.gauss(phi2, sig2)


			########## Calculate separate mean / std for G1 and G2 ############

			init_G1_node_Phi = []
			init_G2_node_Phi = []

			for i in G:
				if 'G1' in i:
					init_G1_node_Phi.append(node_Phi[i])
				elif 'G2' in i:
					init_G2_node_Phi.append(node_Phi[i])
			init_G1_mean = np.mean(init_G1_node_Phi)
			init_G1_std = np.std(init_G1_node_Phi)

			init_G2_mean = np.mean(init_G2_node_Phi)
			init_G2_std = np.std(init_G2_node_Phi)






			############ Homophily ##############

			for T in range(NO_Phi_realization):
				neighbour_Phi = {}
				for i in G.nodes():
					neighbour_Phi[i] = [node_Phi[i]]
					for j in G[i].keys():
						neighbour_Phi[i].append(node_Phi[j])
				for i in G.nodes():
					node_Phi[i] = sum(neighbour_Phi[i])/(len(G[i])+1)



			########## Calculate separate mean / std for G1 and G2 ############

			final_G1_node_Phi = []
			final_G2_node_Phi = []

			for i in G:
				if 'G1' in i:
					final_G1_node_Phi.append(node_Phi[i])
				elif 'G2' in i:
					final_G2_node_Phi.append(node_Phi[i])
			final_G1_mean = np.mean(final_G1_node_Phi)
			final_G1_std = np.std(final_G1_node_Phi)

			final_G2_mean = np.mean(final_G2_node_Phi)
			final_G2_std = np.std(final_G2_node_Phi)





			for i in G.nodes():
				G.node[i] = 0

			r = rd.randint(0,n1+n2-1)
			for i in range(int(rho*(n1*n2))):
				G.node[r] = 1
				r = rd.randint(0,n1+n2-1)
				while G.node[r] == 1:
					r = rd.randint(0,n1+n2-1)
					if G.node[r] == 0:
						break
			a = sum(G.node.values())

	#		NO_infected_nodes[m].append(sum(G.node.values())) => defunctionalized because the number of steps to cascade is one smaller than the length of entire list.


			if phi<1:
				threshold.frac_thr(G, phi, MAX_Steps_to_cascade, NO_infected_nodes, m, neighbor_Phi, node_Phi, n1+n2, a)
				steps_to_cascade_at_each_realization[p].append(len(NO_infected_nodes[m]))

	#			plt.figure(figsize=(8,8))
	#			nx.draw_networkx_edges(G,pos,alpha=0.4)
	#			nx.draw_networkx_nodes(G,pos,
	#					       node_color=node_Phi.values(),
	#					     final_mean  cmap=plt.cm.Reds_r)

	#			plt.xlim(-0.05,1.05)
	#			plt.ylim(-0.05,1.05)
	#			plt.axis('off')
	#			plt.savefig('Figures/Threshold_map m-2.png')

			else:
				abs_thr(phi)
				steps_to_cascade_at_each_realization[p].append(len(NO_infected_nodes[m]))

	 #NO_infected nodes is the list of NO of infected nodes at each steps to cascade. Therefore, len(NO_infected_nodes) is the number of steps needed to reach cascade.

			final_value_at_each_realization[m] = sum(G.node.values())
		final_mean_at_each_meandegree_step.append(sum(final_value_at_each_realization.values())/NO_realization_at_each_meandegree_step) # ==> try changing to ''NO_realization_at_each_meandegree_step''

	#	print steps_to_cascade_at_each_realization

#		mean_NO_steps_to_cascade_at_each_Z.append(sum(steps_to_cascade_at_each_realization[p])/len(steps_to_cascade_at_each_realization[p]))

#		mean_giant_component_size_at_degree.append(sum(giant_component_size_at_degree)/NO_realization_at_each_meandegree_step)


	board.append(final_mean_at_each_meandegree_step)
	scipy.io.savemat(data_path + Filename_str, dict(A=board))


board = np.asarray(board)

if os.path.exists(figure_path) == False:
	os.mkdir(figure_path)

fig, ax = plt.subplots()
cax = ax.imshow(board.T, cmap = plt.cm.gist_yarg_r, origin = 'lower',  vmin = 0, vmax = n1+n2, extent = [0, phi1-phi2, 0, p], aspect='auto')
ax.set_title('No-Stop updating')
cbar = fig.colorbar(cax, ticks = [0, (n1+n2)/2, n1+n2])
cbar.ax.set_yticklabels(['0', '0.5', '1'])
ax.set_xlabel('Mean threshold ' + r'$\phi$')
ax.set_ylabel('Mean degree ' + r'$z$')
cbar.set_label('Fraction of activated nodes ' + r'$\rho$')

plt.savefig('Figures/' + Filename_str + '.pdf')

plt.show()



