#!/usr/bin/python -tt

import networkx as nx
import pylab as pl
import random as rd
import sys
import itertools as it

def ER(n, p):
  G=nx.Graph()
  G.add_nodes_from(range(n))
  edges=it.combinations(range(n),2) #builds tuples of (0,1) (0,2) to (n,n-1)


  for e in edges:
    if rd.random()<p: #this would work if rd.random() is uniformly random func
      G.add_edge(*e) #unpack edge tuple

  return G



N=int(sys.argv[1])
P=float(sys.argv[2])
G=ER(N, P)

nx.draw(G)
pl.show()
