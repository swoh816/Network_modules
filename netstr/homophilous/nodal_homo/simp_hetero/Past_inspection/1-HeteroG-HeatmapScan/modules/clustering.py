#!/usr/bin/python -tt


#		clustering

def clustering_coeff(G, local_clustering_coeffs):

	def local_clustering_coeff(i):
		if len(G[i])>1:
			edges_btn_neighbors[i] = 0
			for j in G[i].keys():
				for k in G[j].keys():
					if k in G[i]:
						edges_btn_neighbors[i] = edges_btn_neighbors[i] + 1
			coeff = float(edges_btn_neighbors[i])/float(len(G[i])*(len(G[i])-1))
		else:
			coeff = 0
		return coeff


	for i in G.nodes():
		local_clustering_coeffs[i] = local_clustering_coeff(i)
	total_clustering = sum(local_clustering_coeffs.values())
	return total_clustering

