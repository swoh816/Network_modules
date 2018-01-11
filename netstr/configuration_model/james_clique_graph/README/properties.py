import networkx as nx

import sys, os
sys.path.append(os.path.abspath('../../../../'))
import functions.distribution_functions.poisson_dist.poisson as pd
sys.path.append(os.path.abspath('../'))
import clique_graph as cg
import numpypy as np
import pickle

list_of_mean_clustering_coefficient = []
list_of_mean_number_of_cliques = []
list_of_mean_average_shortest_patlen = []
list_of_clique_ratio = [i*0.02 for i in range(51)]

for clique_ratio in list_of_clique_ratio:
    list_of_clustering_coefficient = []
    list_of_number_of_cliques = []
    list_of_average_shortest_patlen = []
    for i in range(100):
        deg_seq = [pd.poisson_random_variable(6) for i in range(1000)]
        G = cg.single_clique_configuration(deg_seq, [4, clique_ratio])
        Gcc = sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)[0]
        Gcc = nx.convert_node_labels_to_integers(Gcc, first_label = 0)
        list_of_clustering_coefficient.append(np.mean(nx.clustering(G).values()))
        list_of_number_of_cliques.append(len([i for i in nx.find_cliques(G) if len(i) >= 4]))
        list_of_average_shortest_patlen.append(nx.average_shortest_path_length(Gcc))
    
    list_of_mean_number_of_cliques.append(float(np.mean(list_of_number_of_cliques)))
    list_of_mean_clustering_coefficient.append(float(np.mean(list_of_clustering_coefficient)))
    list_of_mean_average_shortest_patlen.append(float(np.mean(list_of_average_shortest_patlen)))

data_compilation = {}
data_compilation['triangle_clustering'] = list_of_mean_clustering_coefficient
data_compilation['average_shortest_patlen'] = list_of_mean_average_shortest_patlen
data_compilation['number_of_cliques'] = list_of_mean_number_of_cliques
pickle.dump(data_compilation, open('./properties.txt', 'wb'))
