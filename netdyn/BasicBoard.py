#!/home/oh/Downloads/pypy-2.1/bin/pypy -tt

save structure


import networkx as nx
import random as rd
import sys
#sys.path.append('/home/oh/Desktop/Simulations/MyModel/ThrHomo/DifferentThrHomo/StrHomo/TwoERGraph/1-TwoER-HeatmapScan/modules')

#import matplotlib.pyplot as plt
import inspect
import time
#import scipy.io
import os
import numpypy as np

import pickle

import imp
two_er_graphs = imp.load_source('two_er_graphs', 'modules/two_er_graphs.py')
threshold = imp.load_source('threshold', 'modules/threshold.py')
#clustering = imp.load_source('clustering', 'modules/clustering.py')
#import two_er_graphs
#import threshold

n1 = int(sys.argv[1])
z1 = int(sys.argv[2])

n2 = int(sys.argv[3])
z2 = int(sys.argv[4])

p = float(sys.argv[5]) # edge probability between two graphs

rho = float(sys.argv[6])
phi1 = float(sys.argv[7])
sig1 = float(sys.argv[8])

phi2 = float(sys.argv[9])
sig2 = float(sys.argv[10])

NO_Phi_realization = int(sys.argv[11])
MAX_Steps_to_cascade=int(sys.argv[12])
res_p=int(sys.argv[13])
res_Z = int(sys.argv[14])
NO_realization_at_each_meandegree_step = int(sys.argv[15])



Filename_str = ''
for i in sys.argv:
	Filename_str = Filename_str+ '-' + i
Filename_str = Filename_str[1:]


NO_infected_nodes = {} # 'data' in previous version.

neighbor_Phi = {}

steps_to_cascade_at_each_realization = {}
mean_NO_steps_to_cascade_at_each_Z = []
edges_btn_neighbors = {}

local_clustering_coeffs = {}


node_Phi = []

z_list = [float((Z-Z_min)*x)/float(res)+Z_min for x in range(res+1)] # 'prob_list' in previous version. Z_min <= x <= Z (Z_min = x = Z when res=0, Z_min = Z.)

phi_list = [float(phi-min_phi)*float(r)/float(resPhi) + min_phi for r in range(resPhi+1)] 

final_value_at_each_realization = {} #'final_value = []' in previous version (list => dict)
#final_mean_at_each_meandegree_step = []

#for z in z_list:
#	steps_to_cascade_at_each_realization[z] = []  => moved to under cascade part.

#A = inspect.getfile(inspect.currentframe())
#path = data_path + A[2:len(A)-3] + '2 - %d, %d, %d, %f, %f, %f, %f, %d, %d, %d, %d, %d/' %(n, Z, Z_min, rho, phi, min_phi, sigma, NO_Phi_realization, MAX_Steps_to_cascade, res, resPhi, NO_realization_at_each_meandegree_step)

current_path = os.getcwd()

data_path = current_path + '/Data/'
figure_path = current_path + '/Figures/'

if os.path.exists(data_path) == False:
	os.mkdir(data_path)


if os.path.exists(data_path + Filename_str + '.mat') == True:
	board = np.array(scipy.io.loadmat(data_path + Filename_str)['A']).tolist()
#	board2  = np.array(scipy.io.loadmat(data_path + Filename_str + 'GiantComponent')['A']).tolist()
#	board2 = []
#	new_mean = np.array(scipy.io.loadmat(data_path + Filename_str + 'Mean.mat')['A']).tolist()
#	new_std = np.array(scipy.io.loadmat(data_path + Filename_str + 'STD.mat')['A']).tolist()
#	node_Phi_data = np.array(scipy.io.loadmat(data_path + Filename_str + 'node_Phi_data')['A']).tolist()
#	order = sorted(enumerate(board), reverse = True)[0][0]
	order = sorted(enumerate(board))[-1][0]
else:
	board = []
#	board2 = []
	new_mean = []
	new_std = []
	node_Phi_data = []
	order = -1


#board = np.zeros((resPhi+1, res+1))
#board2 = np.zeros((resPhi+1, res+1)) #heatmap of giant cluster
#board_Phi_step = 0
#new_mean = np.array(np.zeros((resPhi+1, res+1))).tolist()
#new_std = np.array(np.zeros((resPhi+1, res+1))).tolist()


#cascade model.
phi_itr = 0
for phi in phi_list[order+1:]:
#	mean_giant_component_size_at_degree = []
	final_mean_at_each_meandegree_step = []
	new_mean.append([])
	new_std.append([])
	z_itr = 0

	for z in z_list:

		p = float(z)/float(n)
		steps_to_cascade_at_each_realization[z] = [] #

	#	print NO_infected_nodes
		giant_component_size_at_degree = []

		new_mean[phi_itr].append([])
		new_std[phi_itr].append([])

		for m in range(NO_realization_at_each_meandegree_step):

			NO_infected_nodes[m] = [] # 'data' in previous version. (global variable?)
			G = nx.fast_gnp_random_graph(n, p)
			Gcc = nx.connected_component_subgraphs(G)
			giant_component_size_at_degree.append(len(Gcc[0].nodes()))
	#		clustering.clustering_coeff(G, local_clustering_coeffs) => activate in case clustering coefficient is needed.


	#		pos = nx.spring_layout(G)
	#		plt.figure(figsize=(8,8))
	#		nx.draw_networkx_edges(G,pos,alpha=0.4)
	#		nx.draw_networkx_nodes(G,pos,
	#				       node_color=node_Phi.values(),
	#				       cmap=plt.cm.Reds_r)

	#		plt.xlim(-0.05,1.05)
	#		plt.ylim(-0.05,1.05)
	#		plt.axis('off')
	#		plt.savefig('Figures/Threshold_map m-1.pdf')

#			for i in G.nodes():
#				node_Phi[i] = rd.gauss(phi, sigma)
#			print sigma
			node_Phi = np.random.normal(phi, sigma, n)

		
	#for more reality:
	#			while node_Phi[i] < 0:
	#				node_Phi[i] = rd.gauss(phi, sigma)

			#Homophiliation

			for t in range(NO_Phi_realization):
				for i in G.nodes():
					neighbor_Phi[i] = [node_Phi[i]]
					for j in G[i].keys():
						neighbor_Phi[i].append(node_Phi[j])
				for i in G.nodes():
					node_Phi[i] = np.mean(neighbor_Phi[i])
#					node_Phi[i] = sum(neighbor_Phi[i])/(len(G[i])+1)
	#		print node_Phi

			new_mean[phi_itr][z_itr].append(np.mean(node_Phi))
			new_std[phi_itr][z_itr].append(np.std(node_Phi))
#			print new_mean
#			print new_std

			node_Phi_data.append(node_Phi)

			for i in G.nodes():
				G.node[i] = 0

			r = rd.randint(0,n-1)
			for i in range(int(rho*n)):
				G.node[r] = 1
				r = rd.randint(0,n-1)
				while G.node[r] == 1:
					r = rd.randint(0,n-1)
					if G.node[r] == 0:
						break
			a = sum(G.node.values())

	#		NO_infected_nodes[m].append(sum(G.node.values())) => defunctionalized because the number of steps to cascade is one smaller than the length of entire list.


			if phi<1:
				threshold.frac_thr(G, phi, z, MAX_Steps_to_cascade, NO_infected_nodes, m, neighbor_Phi, node_Phi, n, a)
				steps_to_cascade_at_each_realization[z].append(len(NO_infected_nodes[m]))

	#			plt.figure(figsize=(8,8))
	#			nx.draw_networkx_edges(G,pos,alpha=0.4)
	#			nx.draw_networkx_nodes(G,pos,
	#					       node_color=node_Phi.values(),
	#					       cmap=plt.cm.Reds_r)

	#			plt.xlim(-0.05,1.05)
	#			plt.ylim(-0.05,1.05)
	#			plt.axis('off')
	#			plt.savefig('Figures/Threshold_map m-2.pdf')

			else:
				abs_thr(phi)
				steps_to_cascade_at_each_realization[z].append(len(NO_infected_nodes[m]))

	 #NO_infected nodes is the list of NO of infected nodes at each steps to cascade. Therefore, len(NO_infected_nodes) is the number of steps needed to reach cascade.

			final_value_at_each_realization[m] = sum(G.node.values())
		final_mean_at_each_meandegree_step.append(sum(final_value_at_each_realization.values())/NO_realization_at_each_meandegree_step) # ==> try changing to ''NO_realization_at_each_meandegree_step''

	#	print steps_to_cascade_at_each_realization

		mean_NO_steps_to_cascade_at_each_Z.append(sum(steps_to_cascade_at_each_realization[z])/len(steps_to_cascade_at_each_realization[z]))

#		mean_giant_component_size_at_degree.append(sum(giant_component_size_at_degree)/NO_realization_at_each_meandegree_step)

	#	print len(steps_to_cascade_at_each_realization)
	#	print len(steps_to_cascade_at_each_realization[z])
	#	print m
		z_itr = z_itr + 1
	board.append(final_mean_at_each_meandegree_step)
#	print board
#	board2.append(mean_giant_component_size_at_degree)
#	print board2
	scipy.io.savemat(data_path + Filename_str, dict(A=board))
#	scipy.io.savemat(data_path + Filename_str + 'GiantComponent', dict(A=board2))
#	scipy.io.savemat(data_path + Filename_str + 'Mean', dict(A=new_mean))
#	scipy.io.savemat(data_path + Filename_str + 'STD', dict(A=new_std))
#	scipy.io.savemat(data_path + Filename_str + 'node_Phi_data', dict(A=node_Phi_data))
#	time.sleep(30)
#	board_Phi_step = 1 + board_Phi_step
	phi_itr = phi_itr + 1

#print board
#print board2

#print mean_NO_steps_to_cascade_at_each_Z


#A = inspect.getfile(inspect.currentframe())

board = np.asarray(board)
#board2 = np.asarray(board2)
#print new_mean
#print new_std
if os.path.exists(figure_path) == False:
	os.mkdir(figure_path)

p = plt.imshow(board.T, cmap = plt.cm.gist_yarg_r, vmin=0, vmax=n, origin = 'lower',  extent = [0, phi, 0, Z], aspect='auto')
fig = plt.gcf()
plt.clim()
plt.colorbar()
#plt.title(A[2:len(A)-3] + ' - %d, %d, %d, %f, %f, %f, %d, %d, %d, %d' %(n, Z, Z_min, rho, phi, sigma, MAX_Steps_to_cascade, res, resPhi, NO_realization_at_each_meandegree_step))
#plt.savefig(figure_path + A[2:len(A)-3] + ' 2- %d, %d, %d, %f, %f, %f, %d, %d, %d, %d.eps' %(n, Z, Z_min, rho, phi, sigma, MAX_Steps_to_cascade, res, resPhi, NO_realization_at_each_meandegree_step))
plt.title('Mean degree VS Mean threshold')
plt.ylabel('Mean degree')
plt.xlabel('Mean threshold')
plt.savefig(figure_path + Filename_str + '-Homophily.pdf')
#plt.show()

#elapsed_time = time.clock() - start_time
#print elapsed_time

##plt.show()


#plt.figure()
#p = plt.imshow(board2.T, cmap = plt.cm.gist_yarg_r, vmin=0, vmax=n, origin = 'lower',  extent = [0, phi, 0, Z], aspect='auto')
#fig = plt.gcf()
#plt.clim()
#plt.colorbar()
##plt.title('GiantComponent Heatmap2 - %d, %d, %d, %f, %f, %f, %d, %d, %d, %d' %(n, Z, Z_min, rho, phi, sigma, MAX_Steps_to_cascade, res, resPhi, NO_realization_at_each_meandegree_step))
#plt.title('GiantComponent Heatmap')
#plt.ylabel('Mean degree')
#plt.xlabel('Mean threshold')
#plt.savefig(figure_path + Filename_str+ 'GiantComponent-Homophily.pdf')



plt.figure()
hist, bins = np.histogram(node_Phi_data, bins = 50)
width = 0.7*(bins[1]-bins[0])
center = (bins[:-1] + bins[1:])/2
plt.title('Threshold distribution after homophily update')
plt.xlabel('Threshold value')
plt.ylabel('Frequency')
plt.bar(center, hist, align = 'center', width = width)
plt.savefig(figure_path + Filename_str+ 'Histogram-Homophily.pdf')














########################################################################################






#print np.random.normal(new_mean[phi_itr][z_itr], new_std[phi_itr][z_itr], n)












#Filename_str = ''
#for i in sys.argv:
#	Filename_str = Filename_str+ ', ' + i
#Filename_str = Filename_str[2:]

#print Filename_str

NO_infected_nodes = {} # 'data' in previous version.

neighbor_Phi = {}

steps_to_cascade_at_each_realization = {}
mean_NO_steps_to_cascade_at_each_Z = []
edges_btn_neighbors = {}

local_clustering_coeffs = {}


node_Phi = []


z_list = [float((Z-Z_min)*x)/float(res)+Z_min for x in range(res+1)] # 'prob_list' in previous version. Z_min <= x <= Z (Z_min = x = Z when res=0, Z_min = Z.)

phi_list = [float(phi-min_phi)*float(r)/float(resPhi) + min_phi for r in range(resPhi+1)] 

final_value_at_each_realization = {} #'final_value = []' in previous version (list => dict)
#final_mean_at_each_meandegree_step = []

#for z in z_list:
#	steps_to_cascade_at_each_realization[z] = []  => moved to under cascade part.

#A = inspect.getfile(inspect.currentframe())
#path = data_path + A[2:len(A)-3] + '2 - %d, %d, %d, %f, %f, %f, %f, %d, %d, %d, %d, %d/' %(n, Z, Z_min, rho, phi, min_phi, sigma, NO_Phi_realization, MAX_Steps_to_cascade, res, resPhi, NO_realization_at_each_meandegree_step)


if os.path.exists(data_path) == False:
	os.mkdir(data_path)


if os.path.exists(data_path + Filename_str + str([2]) + '.mat') == True:
	board = np.array(scipy.io.loadmat(data_path + Filename_str + str([2]) + '.mat')['A']).tolist()
#	board2 = np.array(scipy.io.loadmat(data_path + Filename_str + str([2]) + 'GiantComponent.mat')['A']).tolist()
#	order = sorted(enumerate(board), reverse = True)[0][0]
	board2 = []
#	new_mean = np.array(scipy.io.loadmat(data_path + Filename_str + 'Mean')['A']).tolist()
#	new_std = np.array(scipy.io.loadmat(data_path + Filename_str + 'STD')['A']).tolist()
#	node_Phi_data2 = np.array(scipy.io.loadmat(data_path + Filename_str + str([2]) + 'node_Phi_data')['A']).tolist()
	order = sorted(enumerate(board))[-1][0]

else:
	board = []
	board2 = []
	node_Phi_data2 = []
	order = -1


#board = np.zeros((resPhi+1, res+1))
#board2 = np.zeros((resPhi+1, res+1)) #heatmap of giant cluster
#board_Phi_step = 0


#new_mean = np.array(np.zeros((resPhi+1, res+1))).tolist()
#new_std = np.array(np.zeros((resPhi+1, res+1))).tolist()
#new_mean = []
#new_std = []

#cascade model.
phi_itr = 0
for phi in phi_list[order+1:]:
#	mean_giant_component_size_at_degree = []
	final_mean_at_each_meandegree_step = []
#	new_mean.append([])
#	new_std.append([])
	z_itr = 0

	for z in z_list:

		p = float(z)/float(n)
		steps_to_cascade_at_each_realization[z] = [] #

	#	print NO_infected_nodes
		giant_component_size_at_degree = []

#		new_mean[phi_itr].append([])
#		new_std[phi_itr].append([])

		for m in range(NO_realization_at_each_meandegree_step):

			NO_infected_nodes[m] = [] # 'data' in previous version. (global variable?)
			G = nx.fast_gnp_random_graph(n, p)
			Gcc = nx.connected_component_subgraphs(G)
			giant_component_size_at_degree.append(len(Gcc[0].nodes()))
	#		clustering.clustering_coeff(G, local_clustering_coeffs) => activate in case clustering coefficient is needed.


	#		pos = nx.spring_layout(G)
	#		plt.figure(figsize=(8,8))
	#		nx.draw_networkx_edges(G,pos,alpha=0.4)
	#		nx.draw_networkx_nodes(G,pos,
	#				       node_color=node_Phi.values(),
	#				       cmap=plt.cm.Reds_r)

	#		plt.xlim(-0.05,1.05)
	#		plt.ylim(-0.05,1.05)Filenam
	#		plt.axis('off')
	#		plt.savefig('Figures/Threshold_map m-1.pdf')

#			for i in G.nodes():
#				node_Phi[i] = rd.gauss(phi, sigma)
#			print sigma
			node_Phi = np.random.normal(new_mean[phi_itr][z_itr][m], new_std[phi_itr][z_itr][m], n)

		
	#for more reality:
	#			while node_Phi[i] < 0:
	#				node_Phi[i] = rd.gauss(phi, sigma)

#			#Homophiliation

#			for t in range(NO_Phi_realization):
#				for i in G.nodes():
#					neighbor_Phi[i] = [node_Phi[i]]
#					for j in G[i].keys():
#						neighbor_Phi[i].append(node_Phi[j])
#				for i in G.nodes():
#					node_Phi[i] = np.mean(neighbor_Phi[i])
##					node_Phi[i] = sum(neighbor_Phi[i])/(len(G[i])+1)
#	#		print node_Phi

#			new_mean[phi_itr][z_itr].append(np.mean(node_Phi))
#			new_std[phi_itr][z_itr].append(np.std(node_Phi))
#			print new_mean
#			print new_std

			node_Phi_data2.append(node_Phi)
			

			for i in G.nodes():
				G.node[i] = 0

			r = rd.randint(0,n-1)
			for i in range(int(rho*n)):
				G.node[r] = 1
				r = rd.randint(0,n-1)
				while G.node[r] == 1:
					r = rd.randint(0,n-1)
					if G.node[r] == 0:
						break
			a = sum(G.node.values())

	#		NO_infected_nodes[m].append(sum(G.node.values())) => defunctionalized because the number of steps to cascade is one smaller than the length of entire list.


			if phi<1:
				threshold.frac_thr(G, phi, z, MAX_Steps_to_cascade, NO_infected_nodes, m, neighbor_Phi, node_Phi, n, a)
				steps_to_cascade_at_each_realization[z].append(len(NO_infected_nodes[m]))

	#			plt.figure(figsize=(8,8))
	#			nx.draw_networkx_edges(G,pos,alpha=0.4)
	#			nx.draw_networkx_nodes(G,pos,
	#					       node_color=node_Phi.values(),
	#					       cmap=plt.cm.Reds_r)

	#			plt.xlim(-0.05,1.05)
	#			plt.ylim(-0.05,1.05)
	#			plt.axis('off')
	#			plt.savefig('Figures/Threshold_map m-2.pdf')

			else:
				abs_thr(phi)
				steps_to_cascade_at_each_realization[z].append(len(NO_infected_nodes[m]))

	 #NO_infected nodes is the list of NO of infected nodes at each steps to cascade. Therefore, len(NO_infected_nodes) is the number of steps needed to reach cascade.

			final_value_at_each_realization[m] = sum(G.node.values())
		final_mean_at_each_meandegree_step.append(sum(final_value_at_each_realization.values())/NO_realization_at_each_meandegree_step) # ==> try changing to ''NO_realization_at_each_meandegree_step''

	#	print steps_to_cascade_at_each_realization

		mean_NO_steps_to_cascade_at_each_Z.append(sum(steps_to_cascade_at_each_realization[z])/len(steps_to_cascade_at_each_realization[z]))

#		mean_giant_component_size_at_degree.append(sum(giant_component_size_at_degree)/NO_realization_at_each_meandegree_step)

	#	print len(steps_to_cascade_at_each_realization)
	#	print len(steps_to_cascade_at_each_realization[z])
	#	print m
		z_itr = z_itr + 1
	board.append(final_mean_at_each_meandegree_step)
#	print board
#	board2.append(mean_giant_component_size_at_degree)
#	print board2
	scipy.io.savemat(data_path + Filename_str + str([2]), dict(A=board))
#	scipy.io.savemat(data_path + Filename_str + str([2]) + 'GiantComponent', dict(A=board2))
#	scipy.io.savemat(data_path + Filename_str + str([2]) + 'Mean', dict(A=new_mean))
#	scipy.io.savemat(data_path + Filename_str + str([2]) + 'STD', dict(A=new_std))
#	scipy.io.savemat(data_path + Filename_str + str([2]) + 'node_Phi_data', dict(A=node_Phi_data2))
#	board_Phi_step = 1 + board_Phi_step
	phi_itr = phi_itr + 1



scratch_data_path = '/scratch/oh' + os.getcwd()[28:] + '/Data/' + Filename_str
scratch_figure_path = '/scratch/oh' + os.getcwd()[28:] + '/Figures/' + Filename_str



board = np.asarray(board)
#board2 = np.asarray(board2)


#os.makedirs(scratch_data_path)
#os.makedirs(scratch_figure_path)

ret = subprocess.call(['ssh', 'arabian-knights', 'mkdir -p ' + scratch_data_path])
ret = subprocess.call(['ssh', 'arabian-knights', 'mkdir -p ' + scratch_figure_path])

ret = subprocess.call(['ssh', 'arabian-knights', 'mv ' + data_path + Filename_str + '* ' + scratch_data_path])

ret = subprocess.call(['ssh', 'arabian-knights', 'mv ' + figure_path + Filename_str + '* ' + scratch_figure_path])

