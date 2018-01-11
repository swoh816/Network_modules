#!/usr/bin/python -tt

import networkx as nx
import sys
import random as rd
import numpy as np
import math

# z: mean degree of a network.
# homo_fact: homophily factor (\alpha in the literature)
# nodal_attri: the list of nodal attributes in which a network has homophily.

# char_deg_leng: characteristic degree length (b in the literature)

def homo_str(z, homo_fact, nodal_attri):
	n = len(nodal_attri)
	G = nx.Graph()
	G.add_nodes_from(range(n))

	if max(nodal_attri) > 0:

		############# Matrix version ############
		boguna_numerator = np.zeros((n,n))
		char_deg_leng = (z*homo_fact*math.sin(math.pi/homo_fact))/(math.pi*2.0*n/max(nodal_attri))
		
		for i in range(n):
			for j in range(n):
				boguna_numerator[i][j] = char_deg_leng**homo_fact+(abs(nodal_attri[i]-nodal_attri[j]))**homo_fact
		boguna_probability = char_deg_leng**homo_fact / boguna_numerator

		for i in range(n):
			for j in range(n):
				if i == j:
					boguna_probability[i][j] = 0

		for i in range(n):
			for j in range(i+1, n): #combination.2
				if boguna_probability[i][j] > rd.random():
					G.add_edge(i, j)
	return G
