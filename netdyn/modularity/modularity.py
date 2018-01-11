import networkx as nx
import numpy as np

G = nx.read_gml('karate.gml')
net_size = len(G)
net_degree = G.degree().values()
net_adjmtx = nx.adjacency_matrix(G)
two_times_total_edges = sum(net_degree)

mod_mtx = []
for i in range(net_size):
	mod_mtx.append([])
	for j in range(net_size):
		mod_mtx[i].append(net_adjmtx[i,j] - net_degree[i]*net_degree[j]/float(two_times_total_edges))

print mod_mtx

eig_mtx = np.linalg.eig(mod_mtx)
eigenvalue_array = sorted(eig_mtx[0], reverse=True)
eigenvector_array = eig_mtx[1]

for count, i in enumerate(eig_mtx[0]):
	if i == eigenvalue_array[0]:
		print count

leading_eigenvector = eigenvector_array[count]
print eigenvalue_array[0]
print leading_eigenvector


