#!/usr/bin/python -tt

import networkx as nx
import matplotlib.pyplot as plt
import random as rd
import sys
import itertools as it

def ER(n, z, s):
	G=nx.Graph()
	G.add_nodes_from(range(n))
	edges=it.combinations(range(n),2) #builds tuples of (0,1) (0,2) to (n,n-1)
	p=float(z)/float(n)
	rd.seed(s)

	for e in edges:
		if rd.random()<p: #this would work if rd.random() is uniformly random func
			G.add_edge(*e) #unpack edge tuple

	return G




n=int(sys.argv[1])
z=float(sys.argv[2])
s=int(sys.argv[3])

G=ER(n, z, s)

#nx.draw(G)
#pl.show()


pos = nx.spring_layout(G)
plt.figure(figsize=(8,8))
nx.draw_networkx_edges(G,pos,alpha=0.4)
nx.draw_networkx_nodes(G,pos,
	               node_color=G.degree().values(),
	               cmap=plt.cm.Blues_r, node_size = 50)
plt.title('Threshold map1')
plt.colorbar()
plt.show()
