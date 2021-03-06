#!/usr/bin/python -tt

import networkx as nx
import numpy as  np
import sys
import random as rd

n = int(sys.argv[1])
p = float(sys.argv[2])
phi = float(sys.argv[3])
sigma = float(sys.argv[4])

def homostr(n, p, phi, sigma, node_Phi):

	G = nx.Graph()
	G.add_nodes_from(range(n))
#	node_Phi = np.array(np.random.normal(phi, sigma, n)).tolist()

	differences = np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			differences[i][j] = abs(node_Phi[i]-node_Phi[j])
	inverse_differences = 1. / differences
	np.fill_diagonal(inverse_differences, 0)

	sum_inverse_differences = sum(sum(inverse_differences))/2
	avg_inverse_differences = sum_inverse_differences/float(n)

#	for i in range(n):
#		for j in range(n)[i:]: #combination
#	#		print inverse_differences[i][j]
#			if p*inverse_differences[i][j]/avg_inverse_differences > rd.random():
#				G.add_edge(i, j)

	for i in range(n):
		for j in range(i, n): #permutation
			if p*inverse_differences[i][j]/avg_inverse_differences > rd.random():
				G.add_edge(i, j)
#	print sum(G.degree().values())
	return G
