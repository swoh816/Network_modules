#!/usr/bin/python -tt

import networkx as nx
import sys
import random as rd
import numpy as np

#~ n = int(sys.argv[1])
#~ p = float(sys.argv[2])
#~ mean = float(sys.argv[3])
#~ std = float(sys.argv[4])


def homo_str(p, nodal_attri):
	n = len(nodal_attri)
	G = nx.Graph()
	G.add_nodes_from(range(n))
	
	############# Matrix version ############
	differences = np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			differences[i][j] = abs(nodal_attri[i]-nodal_attri[j])
	inverse_differences = 1. / differences

	for i in range(n):
		for j in range(n):
			if i == j:
				inverse_differences[i][j] = 0

	for i in range(n):
		indi_norm = sum(inverse_differences[i])
		for j in range(n): #combination.2
			if p*inverse_differences[i][j]/indi_norm > rd.random():
				G.add_edge(i, j)
					

	#~ nod_p = 
	#~ str_p = float(G.degree())/G.degreesum(G.degree().values())
	
	
	return G
