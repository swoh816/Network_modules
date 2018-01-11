import networkx as nx
import numpy as np
import random as rd

def sec_ord_simil(nodal_attri, sociability, p):
	
	G = nx.Graph()
	n = len(nodal_attri)
	G.add_nodes_from(range(n))
	
	for i in range(n):
		#~ for j in range(i+1, n): #combination.2
		for j in range(n):
			for k in G.neighbors(i):
				if j in G.neighbors(k):
					if sociability[i]*p*abs(nodal_attri[i]-nodal_attri[j]) > rd.random():
						G.add_edge(i, j)

				else:
					if p*abs(nodal_attri[i]-nodal_attri[j]) > rd.random():
						G.add_edge(i, j)
					
	return G
