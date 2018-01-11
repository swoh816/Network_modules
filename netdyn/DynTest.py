#!/usr/bin/python -tt

import networkx as nx
import numpy as  np
import sys
import random as rd
import matplotlib.axes as ax
import matplotlib.pyplot as plt

n = int(sys.argv[1])
p = float(sys.argv[2])
phi = float(sys.argv[3])
sigma = float(sys.argv[4])

G = nx.Graph()
G.add_nodes_from(range(n))
node_Phi = np.array(np.random.normal(phi, sigma, n)).tolist()

differences = np.zeros((n,n))
for i in range(n):
	for j in range(n):
		differences[i][j] = abs(node_Phi[i]-node_Phi[j])
inverse_differences = 1. / differences
np.fill_diagonal(inverse_differences, 0)

sum_inverse_differences = sum(sum(inverse_differences))/2
avg_inverse_differences = sum_inverse_differences/float(n)

for i in range(n):
	for j in range(n)[i:]: #combination.2
#		print inverse_differences[i][j]
		if p*inverse_differences[i][j]/avg_inverse_differences > rd.random():
			G.add_edge(i, j)

print G.number_of_edges()
print nx.clustering

pos = nx.spring_layout(G)
plt.figure(figsize=(8,8))
nx.draw_networkx_edges(G,pos,alpha=0.4)
nx.draw_networkx_nodes(G,pos,
		       node_color=node_Phi,
		       cmap=plt.cm.Reds_r)
plt.title('Threshold map2-1')
plt.colorbar()
plt.xlim(-0.05,1.05)
plt.ylim(-0.05,1.05)
plt.show()
