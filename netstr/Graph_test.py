import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random as rd

########## import graph file to test ##########
import homophilous.nodal_homo.boguna_model.boguna_model as boguna_model

########## Graph parameters ##########

n = 250
#~ p=50000000
z = 10
homo_fact = 3
NO_of_iteration = 50

nodal_attri = []
for i in range(n):
	nodal_attri.append(rd.gauss(5, 3))

#~ sociability = []
#~ for i in range(n):
	#~ sociability.append(rd.gauss(100000, 0))
	
#for i in range(n):
#	node_Phi.append(rd.gauss(mean, std))

list_of_mean_degree = []
list_of_glob_clustering = []
for i in range(NO_of_iteration):
	G = boguna_model.homo_str(z, homo_fact, nodal_attri)
	#~ print G
	list_of_mean_degree.append(2*G.number_of_edges()/float(n))
	list_of_glob_clustering.append(sum(nx.clustering(G).values())/n)



########## graph properties ##########

#for i in range(n):
#	for j in range(i, n): #permutation
#		if p*inverse_differences[i][j]/avg_inverse_differences > rd.random():
#			G.add_edge(i, j)

#print sum(G.degree().values())/2
print 'mean degree: ' + str(sum(list_of_mean_degree)/NO_of_iteration)
print 'global clustering coefficient: ' + str(sum(list_of_glob_clustering)/NO_of_iteration)

#G = nx.connected_component_subgraphs(G)[0]




########## Draw graph ##########

G = nx.connected_component_subgraphs(G)[0]
pos = nx.spring_layout(G)

plt.figure(figsize=(8,8))
nx.draw_networkx_edges(G,pos,alpha=0.4)

nodal_attri_extracted = []
for i in G.nodes():
	nodal_attri_extracted.append(nodal_attri[i])

nx.draw_networkx_nodes(G,pos, node_color=nodal_attri_extracted, cmap=plt.cm.Greens_r)
# cmap=plt.cm.Reds_r, vmin = 0.1, vmax = 0.2)

#~ nx.draw_networkx_labels(G, pos)

plt.title('Graph')
plt.colorbar()
plt.xlim(-0.05,1.05)
plt.ylim(-0.05,1.05)
plt.axis('off')
#~ plt.savefig('Threshold_map4.png')
plt.show()







########## Lineplots ##########











####### Draw Giant component ######

#Gcc = nx.connected_component_subgraphs(G)

#pos = nx.spring_layout(Gcc)
#plt.figure(figsize=(8,8))
#nx.draw_networkx_edges(G,pos,alpha=0.4)
#nx.draw_networkx_nodes(G,pos,
#		       node_color=node_Phi,
#		       cmap=plt.cm.Reds_r)
#plt.title('Giant component')
#plt.colorbar()
#plt.xlim(-0.05,1.05)
#plt.ylim(-0.05,1.05)
##plt.axis('off')
##plt.savefig('Figures2/' + file_name + '-Threshold2' + '-' + str(T) + '.png')
#plt.show()



########## draw histogram ##########
#~ plt.figure()
#~ y = node_Phi
#~ hist, bins = np.histogram(y, bins = 50)
#~ width = 0.7*(bins[1]-bins[0])
#~ center = (bins[:-1] + bins[1:])/2
#~ plt.xlabel('Threshold size')
#~ plt.ylabel('Frequency')
#~ plt.bar(center, hist, align = 'center', width = width)
#~ plt.show()
#~ plt.savefig('thr_hist_after.pdf')














#~ p=nx.single_source_shortest_path_length(G,ncenter)
#~ 
#~ plt.figure(figsize=(8,8))
#~ nx.draw_networkx_edges(G,pos,nodelist=[ncenter],alpha=0.4)
#~ nx.draw_networkx_nodes(G,pos,nodelist=p.keys(),
                       #~ node_size=80,
                       #~ node_color=p.values(),
                       #~ cmap=plt.cm.Reds_r)
#~ 
#~ plt.xlim(-0.05,1.05)
#~ plt.ylim(-0.05,1.05)
#~ plt.axis('off')
#~ plt.savefig('random_geometric_graph.png')
#~ plt.show()

