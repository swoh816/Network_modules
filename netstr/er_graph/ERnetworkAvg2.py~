#!/usr/bin/python -tt

import networkx as nx
import pylab as pl
import random as rd
import sys
import itertools as it
import time

#The fastest code (5 times faster than the third)

def ER(n, z, s):
	G=nx.Graph()
	G.add_nodes_from(range(n))
	p=float(z)/float(n)
	rd.seed(s)
	A = range(n)
	for i in A:
		for j in A[i+1:]:
			if rd.random()<p:
				G.add_edge(i, j)

	return G



#Second fastest code (almost as same as the third code)

#def ER(n, z, s):
#	G=nx.Graph()
#	G.add_nodes_from(range(n))
#	p=float(z)/float(n)
#	rd.seed(s)

#	for i in range(n):
#		for j in range(n)[i+1:]:
#			if rd.random()<p:
#				G.add_edge(i, j)

#	return G



#slowest code (the slowest)

#def ER(n, z, s):
#	G=nx.Graph()
#	G.add_nodes_from(range(n))
#	edges=it.combinations(range(n),2) #builds tuples of (0,1) (0,2) to (n,n-1)
#	p=float(z)/float(n)
#	rd.seed(s)

#	for e in edges:
#		if rd.random()<p: #this would work if rd.random() is uniformly random func
#			G.add_edge(*e) #unpack edge tuple

#	return G






n=int(sys.argv[1])
z=float(sys.argv[2])
s=int(sys.argv[3])


elapsed_time = []

for i in range(100):
	start_time = time.clock()
	G=ER(n, z, s)
	elapsed_time.append(time.clock() - start_time)



pl.plot(range(100), elapsed_time)
pl.title('1')
#nx.draw(G)
pl.show()
