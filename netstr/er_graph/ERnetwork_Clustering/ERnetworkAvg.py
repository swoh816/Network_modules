#!/usr/bin/python -tt

import networkx as nx
import pylab as pl
import random as rd
import sys
import itertools as it

n=int(sys.argv[1])
z=float(sys.argv[2])
s=int(sys.argv[3])
edges_btn_neighbors = {}
local_clustering_coeffs = {}
final_data = []

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

ER = ER(n, z, s)



def local_clustering_coeff(i):
	if len(ER[i])>1:
		edges_btn_neighbors[i] = 0
		for j in ER[i].keys():
			for k in ER[j].keys():
				if k in ER[i]:
					edges_btn_neighbors[i] = edges_btn_neighbors[i] + 1
		coeff=float(edges_btn_neighbors[i])/float(len(ER[i])*(len(ER[i])-1)) # don't divide into two, because edges are counted twice already. So, originally it's:
# 2 * float(edges_btn_neighbors[i])/ 2 * float(len(ER[i])*(len(ER[i])-1))
	else:
		coeff = 0
	return coeff



for i in ER.nodes():
	local_clustering_coeffs[i] = local_clustering_coeff(i)


def clustering_coeff(ER):
	total_clustering = sum(local_clustering_coeffs.values())
	return total_clustering


print local_clustering_coeffs
print clustering_coeff(ER)


pl.figure()
pl.plot(range(n), local_clustering_coeffs.values())
pl.show()

nx.draw(ER)
pl.show()
