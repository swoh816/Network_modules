#!/usr/bin/python -tt

import networkx as nx
import random as rd
import numpy as np


def two_er(n1, z1, n2, z2, p3, convert_integer):



	p1 = float(z1)/float(n1)
	p2 = float(z2)/float(n2)

	G1 = nx.fast_gnp_random_graph(n1, p1)
	G2 = nx.fast_gnp_random_graph(n2, p2)

	H = nx.union(G1, G2, rename = ['G1-', 'G2-'])


	elist = []

	for i in range(int(n1*n2)):
		if p3>rd.random():
			e1 = rd.randint(0, n1-1)
			e2 = rd.randint(0, n2-1)
			while ('G1-'+str(e1), 'G2-'+str(e2)) in elist:
				e1 = rd.randint(0, n1-1)
				e2 = rd.randint(0, n2-1)
				if ('G1-'+str(e1), 'G2-'+str(e2)) not in elist:
					break
			elist.append(('G1-'+str(e1), 'G2-'+str(e2)))


	H.add_edges_from(elist)

	H = nx.connected_component_subgraphs(H)[0]
	if convert_integer == 'yes':
		H = nx.convert_node_labels_to_integers(H, first_label = 0)
	
	return H
	
