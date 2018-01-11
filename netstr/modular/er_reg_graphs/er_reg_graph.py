import networkx as nx
import random as rd
import sys, os
sys.path.append(os.path.abspath('../../../'))
import netstr.power_law_graph.power_law_graph as pl_gra
import numpy as np

def test(A):
	return np.exp(A)

def two_reg_edge_addition(n1, k1, n2, k2, inter_connect_prob, convert_integer):
	G1 = nx.random_regular_graph(k1, n1)
	G2 = nx.random_regular_graph(k2, n2)

	
	elist = []
	for i in range(n1):
		print i
		if inter_connect_prob>rd.random():
			selected_G1_edge = G1.edges()[rd.randint(0, (n1*k1)/2-1)]
			selected_G2_edge = G2.edges()[rd.randint(0, (n2*k2)/2-1)]
			print selected_G1_edge, selected_G2_edge
			print 'yes'
			elist.append(('G1-'+str(selected_G1_edge[0]), 'G2-'+str(selected_G2_edge[0])))
			print 'done1'
			elist.append(('G1-'+str(selected_G1_edge[1]), 'G2-'+str(selected_G2_edge[1])))
			print 'done2'
			G1.remove_edge(selected_G1_edge[0], selected_G1_edge[1])
			print 'done3'
			G2.remove_edge(selected_G2_edge[0], selected_G2_edge[1])
			print 'done4'
		
	H = nx.union(G1, G2, rename = ['G1-', 'G2-'])
	H.add_edges_from(elist)

	H = nx.connected_component_subgraphs(H)[0]


	if convert_integer == 'yes':
		H = nx.convert_node_labels_to_integers(H, first_label = 0)
	
	return H


def er_reg_edge_rewiring(n1, k1, n2, k2, rat11, rat12, rat22):
	G1 = nx.fast_gnp_random_graph(n1, k1/float(n1))
	G2 = nx.random_regular_graph(k2, n2)
	#~ print len(G1.edges())
	#~ print len(G2.edges())
	H = nx.union(G1, G2, rename = ['G1-', 'G2-'])

	mix_mat = np.zeros((2, 2)) #make 2-by-2 mixing matrix
	mix_mat[0, 0] = rat11 #G1-G1
	mix_mat[0, 1] = rat12 #G1-G2
	mix_mat[1, 0] = rat12 #G2-G1
	mix_mat[1, 1] = rat22 #G2-G2
	mix_mat = 1/sum(sum(mix_mat))*mix_mat
	
	print mix_mat
	
	for i in range(int(n1*k1+n2*k2)/2):
		selected_H1_edge = H.edges()[rd.randint(0, (n1*k1+n2*k2)/2-1)]
		H1_edge_ele_1 = selected_H1_edge[0]
		H1_edge_ele_2 = selected_H1_edge[1]
		#~ print len(H.edges())
		while 1:
			selected_H2_edge = H.edges()[rd.randint(0, (n1*k1+n2*k2)/2-1)]
			#~ print selected_H1_edge
			#~ print selected_H2_edge
			H2_edge_ele_1 = selected_H2_edge[0]
			H2_edge_ele_2 = selected_H2_edge[1]
			if H1_edge_ele_1 != H2_edge_ele_1 and H1_edge_ele_2 != H2_edge_ele_2 and H1_edge_ele_1 != H2_edge_ele_2 and H1_edge_ele_2 != H2_edge_ele_1 and H1_edge_ele_1 not in H[H2_edge_ele_1] and H1_edge_ele_2 not in H[H2_edge_ele_2]:
				break
				
		if (mix_mat[int(H1_edge_ele_1[1])-1, int(H2_edge_ele_1[1])-1] * mix_mat[int(H1_edge_ele_2[1])-1, int(H2_edge_ele_2[1])-1] ) / (mix_mat[int(H1_edge_ele_1[1])-1, int(H1_edge_ele_2[1])-1] * mix_mat[int(H2_edge_ele_1[1])-1, int(H2_edge_ele_2[1])-1])>rd.random():
			H.add_edge(H1_edge_ele_1, H2_edge_ele_1)
			H.add_edge(H1_edge_ele_2, H2_edge_ele_2)
			#~ elist = []
			#~ elist.append((H1_edge_ele_1, H2_edge_ele_1))
			#~ elist.append((H1_edge_ele_2, H2_edge_ele_2))
			#~ H.add_edges_from(elist)
			#~ print elist
			H.remove_edge(H1_edge_ele_1, H1_edge_ele_2)
			H.remove_edge(H2_edge_ele_1, H2_edge_ele_2)
			
	#~ print len(H.edges())
	return H
