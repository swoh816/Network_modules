#!/usr/bin/python -tt

import networkx as nx
import numpy as  np
import sys
import random as rd
import matplotlib.axes as ax
import matplotlib.pyplot as plt

n = int(sys.argv[1])
p = float(sys.argv[2])
phi = float(sys.argv[3])
sigma = float(sys.argv[4])
ensemble_size = int(sys.argv[5])

clustering = []
total_num_edges = []

for m in range(ensemble_size):
	G = nx.Graph()
	G.add_nodes_from(range(n))
	#node_Phi = np.array(np.random.random(n)).tolist()
	node_Phi = np.array(np.random.normal(phi, sigma, n)).tolist()

	#differences = []

	#for i in range(n): # sum of all differences
	#	for j in range(n)[i:]:
	#		differences.append(abs(node_Phi[i]-node_Phi[j]))

	############# Matrix version ############
	differences = np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			differences[i][j] = abs(node_Phi[i]-node_Phi[j])
	inverse_differences = 1. / differences
	np.fill_diagonal(inverse_differences, 0)
	#print inverse_differences

	################## Check whether difference distribution follows gaussian ################

	#differences2 = np.zeros((n,n))
	#for i in range(n):
	#	for j in range(n):
	#		differences2[i][j] = node_Phi[i]-node_Phi[j]

	#x = differences2
	#hist, bins = np.histogram(x, bins = 25, range = [0, 1.4])
	#width = 0.7*(bins[1]-bins[0])
	#center = (bins[:-1] + bins[1:])/2

	#plt.bar(center, hist, align = 'center', width = width)
	##plt.show()
	#.2

	#plt.figure()
	#y = differences
	#hist, bins = np.histogram(y, bins = 50)
	#width = 0.7*(bins[1]-bins[0])
	#center = (bins[:-1] + bins[1:])/2

	#plt.bar(center, hist, align = 'center', width = width)
	#plt.show()


	sum_inverse_differences = sum(sum(inverse_differences))/2
	avg_inverse_differences = sum_inverse_differences/float(n)
	#print p*differences/avg_inverse_differences

	edge = 0

	for i in range(n):
		for j in range(n)[i:]: #combination.2
	#		print inverse_differences[i][j]
			if p*inverse_differences[i][j]/avg_inverse_differences > rd.random():
				G.add_edge(i, j)
				edge = edge+1

	total_num_edges.append(edge)
	clustering.append(sum(nx.clustering(G).values())/len(G))



hist, bins = np.histogram(total_num_edges, bins = 50)
width = 0.7*(bins[1]-bins[0])
center = (bins[:-1] + bins[1:])/2

plt.bar(center, hist, align = 'center', width = width)
#plt.show()

plt.figure()
hist, bins = np.histogram(clustering, bins = 50)
width = 0.7*(bins[1]-bins[0])
center = (bins[:-1] + bins[1:])/2

plt.bar(center, hist, align = 'center', width = width)
plt.show()

#for i in range(n):
#	for j in range(i, n): #permutation
#		if p*inverse_differences[i][j]/avg_inverse_differences > rd.random():
#			G.add_edge(i, j)

#print sum(G.degree().values())/2




#print G.number_of_edges()
#print nx.clustering

##G = nx.connected_component_subgraphs(G)[0]

#pos = nx.spring_layout(G)
#plt.figure(figsize=(8,8))
#nx.draw_networkx_edges(G,pos,alpha=0.4)
#nx.draw_networkx_nodes(G,pos,
#		       node_color=node_Phi,
#		       cmap=plt.cm.Reds_r)
#plt.title('Threshold map2-1')
#plt.colorbar()
#plt.xlim(-0.05,1.05)
#plt.ylim(-0.05,1.05)
##plt.axis('off')
##plt.savefig('Figures2/' + file_name + '-Threshold2' + '-' + str(T) + '.png')

##plt.savefig('Figures/Disconnected2.eps')
#plt.show()







####### Draw Giant component ######

#Gcc = nx.connected_component_subgraphs(G)

#pos = nx.spring_layout(Gcc)
#plt.figure(figsize=(8,8))
#nx.draw_networkx_edges(G,pos,alpha=0.4)
#nx.draw_networkx_nodes(G,pos,
#		       node_color=node_Phi,
#		       cmap=plt.cm.Reds_r)
#plt.title('Threshold map2-1')
#plt.colorbar()
#plt.xlim(-0.05,1.05)
#plt.ylim(-0.05,1.05)
##plt.axis('off')
##plt.savefig('Figures2/' + file_name + '-Threshold2' + '-' + str(T) + '.png')
#plt.show()
