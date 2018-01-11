import networkx as nx

import sys, os
sys.path.append(os.path.abspath('../../../../'))
import functions.distribution_functions.poisson_dist.poisson as pd
import netstr.configuration_model.newman_triangle.newman_triangle as nt
import netstr.configuration_model.newman_square.newman_square as nq
import netstr.configuration_model.james_clique_graph.clique_graph as cg
import numpypy as np
import pickle


edge_triangle_ratio = 0
edge_square_ratio = edge_triangle_ratio
clique_ratio = edge_square_ratio


for realization in range(100):

	############### STORAGES ###############
	
	list_of_triangular_clustering_coefficient_tri = []
	list_of_number_of_cliques_tri = []
	list_of_average_shortest_patlen_tri = []
	list_of_square_clustering_coefficient_tri = []
	list_of_degree_distribution_tri = []

	list_of_triangular_clustering_coefficient_sqr = []
	list_of_number_of_cliques_sqr = []
	list_of_average_shortest_patlen_sqr = []
	list_of_square_clustering_coefficient_sqr = []
	list_of_degree_distribution_sqr = []

	list_of_triangular_clustering_coefficient_cliq_4 = []
	list_of_number_of_cliques_cliq_4 = []
	list_of_average_shortest_patlen_cliq_4 = []
	list_of_square_clustering_coefficient_cliq_4 = []
	list_of_degree_distribution_cliq_4 = []

	list_of_triangular_clustering_coefficient_cliq_5 = []
	list_of_number_of_cliques_cliq_5 = []
	list_of_average_shortest_patlen_cliq_5 = []
	list_of_square_clustering_coefficient_cliq_5 = []
	list_of_degree_distribution_cliq_5 = []

	list_of_triangular_clustering_coefficient_cliq_6 = []
	list_of_number_of_cliques_cliq_6 = []
	list_of_average_shortest_patlen_cliq_6 = []
	list_of_square_clustering_coefficient_cliq_6 = []
	list_of_degree_distribution_cliq_6 = []




	############### INVESTIGATE ###############
	
	deg_seq_tri = [pd.poisson_random_variable(6) for i in range(1000)]
	deg_seq_sqr = deg_seq_tri[:]
	deg_seq_cliq_4 = deg_seq_tri[:]
	deg_seq_cliq_5 = deg_seq_tri[:]
	deg_seq_cliq_6 = deg_seq_tri[:]
	
	
	G_tri = nt.newman_clustering_configuration(deg_seq_tri, edge_triangle_ratio)
	Gcc_tri = sorted(nx.connected_component_subgraphs(G_tri), key = len)[-1]
	Gcc_tri = nx.convert_node_labels_to_integers(Gcc_tri, first_label = 0)

	
	G_sqr = nq.newman_square_configuration(deg_seq_sqr, edge_square_ratio)
	Gcc_sqr = sorted(nx.connected_component_subgraphs(G_sqr), key = len)[-1]
	Gcc_sqr = nx.convert_node_labels_to_integers(Gcc_sqr, first_label = 0)

	
	G_cliq_4 = cg.single_clique_configuration(deg_seq_cliq_4, [4, clique_ratio])
	Gcc_cliq_4 = sorted(nx.connected_component_subgraphs(G_cliq_4), key = len)[-1]
	Gcc_cliq_4 = nx.convert_node_labels_to_integers(Gcc_cliq_4, first_label = 0)

	
	G_cliq_5 = cg.single_clique_configuration(deg_seq_cliq_5, [5, clique_ratio])
	Gcc_cliq_5 = sorted(nx.connected_component_subgraphs(G_cliq_5), key = len)[-1]
	Gcc_cliq_5 = nx.convert_node_labels_to_integers(Gcc_cliq_5, first_label = 0)

	
	G_cliq_6 = cg.single_clique_configuration(deg_seq_cliq_6, [6, clique_ratio])
	Gcc_cliq_6 = sorted(nx.connected_component_subgraphs(G_cliq_6), key = len)[-1]
	Gcc_cliq_6 = nx.convert_node_labels_to_integers(Gcc_cliq_6, first_label = 0)
	
			
	list_of_square_clustering_coefficient_tri.append(float(np.mean(nx.square_clustering(Gcc_tri).values())))
	list_of_triangular_clustering_coefficient_tri.append(float(np.mean(nx.clustering(Gcc_tri).values())))
	list_of_number_of_cliques_tri.append(len([i for i in nx.find_cliques(Gcc_tri) if len(i) >= 4]))
	list_of_average_shortest_patlen_tri.append(nx.average_shortest_path_length(Gcc_tri))
	list_of_degree_distribution_tri.append(Gcc_tri.degree().values())

	list_of_square_clustering_coefficient_sqr.append(float(np.mean(nx.square_clustering(Gcc_sqr).values())))
	list_of_triangular_clustering_coefficient_sqr.append(float(np.mean(nx.clustering(Gcc_sqr).values())))
	list_of_number_of_cliques_sqr.append(len([i for i in nx.find_cliques(Gcc_sqr) if len(i) >= 4]))
	list_of_average_shortest_patlen_sqr.append(nx.average_shortest_path_length(Gcc_sqr))
	list_of_degree_distribution_sqr.append(Gcc_sqr.degree().values())
	
	list_of_square_clustering_coefficient_cliq_4.append(float(np.mean(nx.square_clustering(Gcc_cliq_4).values())))
	list_of_triangular_clustering_coefficient_cliq_4.append(float(np.mean(nx.clustering(Gcc_cliq_4).values())))
	list_of_number_of_cliques_cliq_4.append(len([i for i in nx.find_cliques(Gcc_cliq_4) if len(i) >= 4]))
	list_of_average_shortest_patlen_cliq_4.append(nx.average_shortest_path_length(Gcc_cliq_4))
	list_of_degree_distribution_cliq_4.append(Gcc_cliq_4.degree().values())
	
	list_of_square_clustering_coefficient_cliq_5.append(float(np.mean(nx.square_clustering(Gcc_cliq_5).values())))
	list_of_triangular_clustering_coefficient_cliq_5.append(float(np.mean(nx.clustering(Gcc_cliq_5).values())))
	list_of_number_of_cliques_cliq_5.append(len([i for i in nx.find_cliques(Gcc_cliq_5) if len(i) >= 4]))
	list_of_average_shortest_patlen_cliq_5.append(nx.average_shortest_path_length(Gcc_cliq_5))
	list_of_degree_distribution_cliq_5.append(Gcc_cliq_5.degree().values())
	
	list_of_square_clustering_coefficient_cliq_6.append(float(np.mean(nx.square_clustering(Gcc_cliq_6).values())))
	list_of_triangular_clustering_coefficient_cliq_6.append(float(np.mean(nx.clustering(Gcc_cliq_6).values())))
	list_of_number_of_cliques_cliq_6.append(len([i for i in nx.find_cliques(Gcc_cliq_6) if len(i) >= 4]))
	list_of_average_shortest_patlen_cliq_6.append(nx.average_shortest_path_length(Gcc_cliq_6))
	list_of_degree_distribution_cliq_6.append(Gcc_cliq_6.degree().values())



	data_compilation = {}
	data_compilation['triangle'] = {}
	data_compilation['square'] = {}
	data_compilation['clique_4'] = {}
	data_compilation['clique_5'] = {}
	data_compilation['clique_6'] = {}

	data_compilation['triangle']['triangular_clustering'] = list_of_triangular_clustering_coefficient_tri
	data_compilation['triangle']['square_clustering'] = list_of_square_clustering_coefficient_tri
	data_compilation['triangle']['average_shortest_patlen'] = list_of_average_shortest_patlen_tri
	data_compilation['triangle']['number_of_cliques'] = list_of_number_of_cliques_tri
	data_compilation['triangle']['degree_distribution'] = list_of_degree_distribution_tri

	data_compilation['square']['triangular_clustering'] = list_of_triangular_clustering_coefficient_sqr
	data_compilation['square']['square_clustering'] = list_of_square_clustering_coefficient_sqr
	data_compilation['square']['average_shortest_patlen'] = list_of_average_shortest_patlen_sqr
	data_compilation['square']['number_of_cliques'] = list_of_number_of_cliques_sqr
	data_compilation['square']['degree_distribution'] = list_of_degree_distribution_sqr

	data_compilation['clique_4']['triangular_clustering'] = list_of_triangular_clustering_coefficient_cliq_4
	data_compilation['clique_4']['square_clustering'] = list_of_square_clustering_coefficient_cliq_4
	data_compilation['clique_4']['average_shortest_patlen'] = list_of_average_shortest_patlen_cliq_4
	data_compilation['clique_4']['number_of_cliques'] = list_of_number_of_cliques_cliq_4
	data_compilation['clique_4']['degree_distribution'] = list_of_degree_distribution_cliq_4

	data_compilation['clique_5']['triangular_clustering'] = list_of_triangular_clustering_coefficient_cliq_5
	data_compilation['clique_5']['square_clustering'] = list_of_square_clustering_coefficient_cliq_5
	data_compilation['clique_5']['average_shortest_patlen'] = list_of_average_shortest_patlen_cliq_5
	data_compilation['clique_5']['number_of_cliques'] = list_of_number_of_cliques_cliq_5
	data_compilation['clique_5']['degree_distribution'] = list_of_degree_distribution_cliq_5

	data_compilation['clique_6']['triangular_clustering'] = list_of_triangular_clustering_coefficient_cliq_6
	data_compilation['clique_6']['square_clustering'] = list_of_square_clustering_coefficient_cliq_6
	data_compilation['clique_6']['average_shortest_patlen'] = list_of_average_shortest_patlen_cliq_6
	data_compilation['clique_6']['number_of_cliques'] = list_of_number_of_cliques_cliq_6
	data_compilation['clique_6']['degree_distribution'] = list_of_degree_distribution_cliq_6

	pickle.dump(data_compilation, open('./net_Str_comparison_data/netstr_comparison' + str(realization) + '.txt', 'wb'))
