#!/usr/bin/python -tt
import os, sys
sys.path.append(os.path.abspath('../../../'))
import netstr.configuration_model.power_law_graph.power_law_graph as pl_gra
import networkx as nx
import random as rd
import numpy as np


def two_pl_gra(n1, x_min1, power_law_exp1, n2, x_min2, power_law_exp2, p3, convert_integer):
	
	G1 = pl_gra.power_law_graph_cuts(n1, x_min1, power_law_exp1)
	G2 = pl_gra.power_law_graph_cuts(n2, x_min2, power_law_exp2)

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
	
