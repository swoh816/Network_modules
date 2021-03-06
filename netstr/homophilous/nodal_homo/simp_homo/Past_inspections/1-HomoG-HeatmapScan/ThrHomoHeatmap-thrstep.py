#!/usr/bin/python -tt

import networkx as nx
import random as rd

import matplotlib.pyplot as plt
import inspect
import time
import scipy.io
import os
import numpy as np

import sys
import imp
homostr = imp.load_source('homostr', 'modules/homostr.py')
threshold = imp.load_source('threshold', 'modules/threshold.py')
#sys.path.append('/home/oh/Desktop/Simulations/MyModel/ThrHomo/DifferentThrHomo/StrHomo/HomoGraph/1-HomoG-HeatmapScan/modules')
#import homostr
#import threshold

n = int(sys.argv[1])
#Z = int(sys.argv[2])
p = float(sys.argv[2]) # edge probability between two graphs
rho = float(sys.argv[3])
phi = float(sys.argv[4])
sig = float(sys.argv[5])
MAX_Steps_to_cascade=int(sys.argv[6])
res_p = int(sys.argv[7])
res_Phi = int(sys.argv[8])
NO_realization_at_each_meandegree_step = int(sys.argv[9])



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


#node_Phi = []
node_Phi = np.array(np.random.normal(phi, sig, n)).tolist()
#z_list = [float(Z*x)/float(res_Z) for x in range(res_Z+1)] #Mean degrees are set constant.
#z2_list = [float(Z2*x)/float(res) for x in range(res+1)]

phi_list = [float(phi)*float(r)/float(res_Phi) for r in range(res_Phi+1)]
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
for phi in phi_list[order+1:]:
#	mean_giant_component_size_at_degree = []
	final_mean_at_each_meandegree_step = []
	for p in p_list:
		steps_to_cascade_at_each_realization[p] = [] #
#		p = float(z)/float(n)
#		giant_component_size_at_degree = []
		for m in range(NO_realization_at_each_meandegree_step):

			NO_infected_nodes[m] = [] # 'data' in previous version. (global variable?)
			G = homostr.homostr(n, p, phi, sig, node_Phi)
#			print sum(G.degree().values())
#			Gcc = nx.connected_component_subgraphs(G)
#			giant_component_size_at_degree.append(len(Gcc[0].nodes()))
#			node_Phi = G.node_Phi

			for i in G.nodes():
				G.node[i] = 0

			r = rd.randint(0,n-1)
			for i in range(int(rho*(n))):
				G.node[r] = 1
				r = rd.randint(0,n-1)
				while G.node[r] == 1:
					r = rd.randint(0,n-1)
					if G.node[r] == 0:
						break
			a = sum(G.node.values())

			if phi<1:
				threshold.frac_thr(G, phi, MAX_Steps_to_cascade, NO_infected_nodes, m, neighbor_Phi, node_Phi, n, a)
				steps_to_cascade_at_each_realization[p].append(len(NO_infected_nodes[m]))

			else:
				abs_thr(phi)
				steps_to_cascade_at_each_realization[p].append(len(NO_infected_nodes[m]))

			final_value_at_each_realization[m] = sum(G.node.values())
		final_mean_at_each_meandegree_step.append(sum(final_value_at_each_realization.values())/NO_realization_at_each_meandegree_step) # ==> try changing to ''NO_realization_at_each_meandegree_step''

	#	print steps_to_cascade_at_each_realization

#		mean_NO_steps_to_cascade_at_each_Z.append(sum(steps_to_cascade_at_each_realization[p])/len(steps_to_cascade_at_each_realization[p]))

#		mean_giant_component_size_at_degree.append(sum(giant_component_size_at_degree)/NO_realization_at_each_meandegree_step)

#	print final_mean_at_each_meandegree_step
	board.append(final_mean_at_each_meandegree_step)
#	scipy.io.savemat(data_path + Filename_str, dict(A=board))


board = np.asarray(board)

if os.path.exists(figure_path) == False:
	os.mkdir(figure_path)

fig, ax = plt.subplots()
cax = ax.imshow(board.T, cmap = plt.cm.gist_yarg_r, origin = 'lower', vmin = 0, vmax = n, extent = [0, phi, 0, p], aspect='auto')
ax.set_title('No-Stop updating')
cbar = fig.colorbar(cax, ticks = [0, n/2, n])
cbar.ax.set_yticklabels(['0', '0.5', '1'])
ax.set_xlabel('Mean threshold ' + r'$\phi$')
ax.set_ylabel('Mean degree ' + r'$z$')
cbar.set_label('Fraction of activated nodes ' + r'$\rho$')

#plt.savefig('Figures/' + Filename_str + '.pdf')

plt.show()



