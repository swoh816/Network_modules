import random as rd
import networkx as nx

def two_pkk(n1, k1, n2, k2, rat):
	G=nx.Graph()
	G.add_nodes_from(range(n1+n2))
	
	for i in range(n1+n2):
		for j in range(n1+n2):
			if i < n1 and j < n1:
				if rd.random() < (k1-rat)/float(2*n1):
					G.add_edge(i, j)

			if i < n1 and j >= n1:
				if rd.random() < rat/float(2*n2):
					G.add_edge(i, j)

			if i >= n1 and j < n1:
				if rd.random() < rat/float(2*n1):
					G.add_edge(i, j)

			if i >= n1 and j >= n1:
				if rd.random() < (k2-rat)/float(2*n2):
					G.add_edge(i, j)

	return G





def two_reg_edge_rewiring(n1, k1, n2, k2, rat):
	G1 = nx.random_regular_graph(k1, n1)
	G2 = nx.random_regular_graph(k2, n2)

	H = nx.union(G1, G2, rename = ['G1-', 'G2-'])

	mix_mat = nx.degree_mixing_matrix(H)
	mix_mat[k1, k2] = rat
	mix_mat[k2, k1] = mix_mat[k1, k2]
	mix_mat[k1, k1] -= rat
	mix_mat[k2, k2] -= rat
	print mix_mat
	
	for i in range((n1*k1+n2*k2)):
		selected_H1_edge = H.edges()[rd.randint(0, (n1*k1+n2*k2)/2-1)]
		H1_edge_ele_1 = selected_H1_edge[0]
		H1_edge_ele_2 = selected_H1_edge[1]

		while 1:
			selected_H2_edge = H.edges()[rd.randint(0, (n1*k1+n2*k2)/2-1)]
			H2_edge_ele_1 = selected_H2_edge[0]
			H2_edge_ele_2 = selected_H2_edge[1]
			if H1_edge_ele_1 != H2_edge_ele_1 and H1_edge_ele_2 != H2_edge_ele_2 and H1_edge_ele_1 != H2_edge_ele_2 and H1_edge_ele_2 != H2_edge_ele_1 and H1_edge_ele_1 not in H[H2_edge_ele_1] and H1_edge_ele_2 not in H[H2_edge_ele_2]:
				break

		if (mix_mat[len(H[H1_edge_ele_1]), len(H[H2_edge_ele_1])] * mix_mat[len(H[H1_edge_ele_2]), len(H[H2_edge_ele_2])] ) / ( mix_mat[len(H[H1_edge_ele_1]), len(H[H1_edge_ele_2])] * mix_mat[len(H[H2_edge_ele_1]), len(H[H2_edge_ele_2])] ) > rd.random():
			H.add_edge(H1_edge_ele_1, H2_edge_ele_1)
			H.add_edge(H1_edge_ele_2, H2_edge_ele_2)
			H.remove_edge(H1_edge_ele_1, H1_edge_ele_2)
			H.remove_edge(H2_edge_ele_1, H2_edge_ele_2)
			
	return H





#~ 
#~ deg_sequence = []
#~ for i in range(n1):
	#~ deg_sequence.append(k1)
#~ for i in range(n2):
	#~ deg_sequence.append(k2)
#~ 
#~ stublist = []
#~ for i in range(n1+n2):
	#~ for j in range(deg_sequence[i]):
		#~ stublist.append(i)
#~ 
#~ shuffle(stublist)
#~ 
                #~ if s1 > s2:
                    #~ s1, s2 = s2, s1
                #~ if s1 != s2 and ((s1, s2) not in edges):
                    #~ edges.add((s1, s2))
                    #~ 
                    #~ 
#~ while stublist:
	#~ n1 = stublist[0]
	#~ n2 = stublist[1]
	#~ if n1 == n2:
		#~ stublist.pop(0)
		#~ stublist.append(n1)
	#~ else:
		#~ if (n1, n2) not in G.edges():
			#~ G.add_edge(n1,n2)
			#~ stublist.pop(0)
			#~ stublist.pop(1)
#~ 






	
#~ def two_pkk_newm_metho()
	
	
	
	#~ 
	#~ 
	#~ 
	#~ 
	#~ 
	#~ 
	#~ 
	#~ stublist = []
	#~ for n in range(n1+n2):
		#~ for i in range(degree_sequence[n]):
			#~ stublist.append(n)
	#~ rd.shuffle(stublist)
	#~ 
	#~ 
	#~ 
	#~ 
	#~ while stublist:
		#~ randly_picked_node_1 = stublist.pop()
		#~ randly_picked_node_2 = stublist.pop()
		#~ 
	#~ 
	#~ for j in Piikk[i]:
		#~ if Piikk[i][j] < p:
			#~ G.add_edge(i, j)
