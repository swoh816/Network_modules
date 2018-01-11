import random as rd
#~ import networkx as nx
#~ import numpy as np
#~ import matplotlib.pyplot as plt

## Algorithm ###
# node i is instantaneously activated and contacts a randomly selected node j --> neighbour j of node i is selected from the neighbours of node i with equal probability.
#==> QUOTE (p.22)
#~ When an event occurs, node i is instantaneously activated and
#~ contacts a randomly selected node j. In the case of a well-mixed population, each j is selected
#~ with probability 1/(N −1). In the case of a network, which is fixed over time, j is selected from
#~ the neighbours of node i with the equal probability. If either i or j is infected and the other is
#~ susceptible, the infection is transmitted such that the susceptible node becomes infected. Then,
#~ node i waits for another time τ drawn from ψ(τ ) before the next activation.

# beta = infection probability
def sir_model_on_network(G, beta, gamma):
	for i in G:
		if G.node[i]['state'] == 's':
			for j in G[i]:
				if G.node[j]['state'] == 'i':
					if rd.random() < beta:
						G.node[i]['state'] = 'i'
					
		elif G.node[i]['state'] == 'i':
			if rd.random() < gamma:
				G.node[i]['state'] = 'r'


#### example: ####
#~ import sir_model as sir
#~ import networkx as nx
#~ import numpy as np
#~ import matplotlib.pyplot as plt
#~ import sir_model as sir
#~ 
#~ numberof_Realizations = 100
#~ G = nx.complete_graph(500)
#~ s_compilation = np.zeros(101)
#~ i_compilation = np.zeros(101)
#~ r_compilation = np.zeros(101)
#~ 
#~ for nth_realization in range(numberof_Realizations):
	#~ for i in G:
		#~ if i == 0:
			#~ G.node[i]['state'] = 'i'
		#~ else:
			#~ G.node[i]['state'] = 's'
#~ 
#~ 
	#~ s_num = [len([i for i in G if G.node[i]['state'] == 's'])]
	#~ i_num = [len([i for i in G if G.node[i]['state'] == 'i'])]
	#~ r_num = [len([i for i in G if G.node[i]['state'] == 'r'])]
#~ 
	#~ for i in range(100):
		#~ sir.sir_model_on_network(G, 1e-3, 1e-1)
		#~ s_num.append(len([i for i in G if G.node[i]['state'] == 's']))
		#~ i_num.append(len([i for i in G if G.node[i]['state'] == 'i']))
		#~ r_num.append(len([i for i in G if G.node[i]['state'] == 'r']))
	#~ s_compilation = (nth_realization*s_compilation + np.asarray(s_num))/(nth_realization+1)
	#~ i_compilation = (nth_realization*i_compilation + np.asarray(i_num))/(nth_realization+1)
	#~ r_compilation = (nth_realization*r_compilation + np.asarray(r_num))/(nth_realization+1)
#~ 
#~ plt.figure()
#~ plt.plot(np.array((s_compilation/101.0)).tolist())
#~ plt.plot(np.array((i_compilation/101.0)).tolist())
#~ plt.plot(np.array((r_compilation/101.0)).tolist())
#~ plt.show()
	





def sir_model_ode(s_frac_past, i_frac_past, r_frac_past, beta, gamma):	
	s_frac_current = s_frac_past - beta*s_frac_past*i_frac_past
	i_frac_current = i_frac_past + beta*s_frac_past*i_frac_past - gamma*i_frac_past
	r_frac_current = r_frac_past + gamma*i_frac_past
	
	return s_frac_current, i_frac_current, r_frac_current


#### example: ####
#~ import random as rd
#~ import networkx as nx
#~ import numpy as np
#~ import matplotlib.pyplot as plt
#~ import sir_model as sir
#~ 
#~ G = nx.complete_graph(500)
#~ for i in G:
	#~ if i == 0:
		#~ G.node[i]['state'] = 'i'
	#~ else:
		#~ G.node[i]['state'] = 's'
		#~ 
#~ s_frac = [len([i for i in G if G.node[i]['state'] == 's'])]
#~ i_frac = [len([i for i in G if G.node[i]['state'] == 'i'])]
#~ r_frac = [len([i for i in G if G.node[i]['state'] == 'r'])]
#~ 
#~ for i in range(100):
	#~ s_frac_current, i_frac_current, r_frac_current = sir.sir_model_ode(s_frac[-1], i_frac[-1], r_frac[-1], 1e-3, 1e-1)
	#~ s_frac.append(s_frac_current)
	#~ i_frac.append(i_frac_current)
	#~ r_frac.append(r_frac_current)
#~ 
#~ plt.figure()
#~ plt.plot(s_frac)
#~ plt.plot(i_frac)
#~ plt.plot(r_frac)
#~ plt.show()
