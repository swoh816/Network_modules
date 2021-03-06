#!/usr/bin/python -tt

import networkx as nx
import matplotlib.pyplot as plt
import sys
import random as rd
import numpy as np

def two_er_graphs(n1, z1, n2, z2, p3, phi1, sig1, phi2, sig2):
	p1 = float(z1)/float(n1)
	p2 = float(z2)/float(n2)

	G1 = nx.fast_gnp_random_graph(n1, p1)
	G2 = nx.fast_gnp_random_graph(n2, p2)

	H = nx.union(G1, G2, rename = ['G1-', 'G2-'])



	######## leave only giant component #########
	elist = []

	for i in range(int(n1*n2*p3)):
		e1 = rd.randint(0, n1-1)
		e2 = rd.randint(0, n2-1)
		elist.append(('G1-'+str(e1), 'G2-'+str(e2)))

	H.add_edges_from(elist)

	H = nx.connected_component_subgraphs(H)[0]

	return H


#def main():
#	n=int(sys.argv[1])
#	z=float(sys.argv[2])
#	s=int(sys.argv[3])

#	G=two_er_graphs(n, z, s)

#	nx.draw(G)
#	pl.show()


#if __name__ == '__main__':
#	main()
