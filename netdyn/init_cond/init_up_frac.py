import random as rd
import math
import sys

def init_activate(G, n):
	if type(n) == float: # Update n FRACTION of nodes
		for i in G:
			if n < rd.random():
				G.node[i]['state'] = 0
			else:
				G.node[i]['state'] = 1

	
	elif type(n) == int: # Update n NUMBER of nodes
		for i in G:
			G.node[i]['state'] = 0

		r = rd.choice(G.nodes())
		for i in range(n):
			G.node[r]['state'] = 1
			r = rd.choice(G.nodes())
			if len(G) < n:
				print 'Error:The number of nodes lower than the number of seed nodes.'
				sys.exit()
			elif len(G) == n:
				G.node[G.nodes()[i]]['state'] = 1
			else:
				while G.node[r]['state'] == 1:
					r = rd.choice(G.nodes())
					if G.node[r]['state'] == 0:
						break


#~ def init_up_frac_num(G, n): #update n number of nodes.
	#~ for i in G:
		#~ G.node[i]['state'] = 0
#~ 
	#~ r = rd.choice(G.nodes())
	#~ for i in range(n):
		#~ G.node[r]['state'] = 1
		#~ r = rd.choice(G.nodes())
		#~ if len(G) < n:
			#~ print 'Error:The number of nodes lower than the number of seed nodes.'
			#~ sys.exit()
		#~ elif len(G) == n:
			#~ G.node[G.nodes()[i]]['state'] = 1
		#~ else:
			#~ while G.node[r]['state'] == 1:
				#~ r = rd.choice(G.nodes())
				#~ if G.node[r]['state'] == 0:
					#~ break



#~ def init_up_frac_prob(G, rho): #update nodes with rho probability.
	#~ for i in G:
		#~ if rho < rd.random():
			#~ G.node[i]['state'] = 0
		#~ else:
			#~ G.node[i]['state'] = 1
	




#~ def init_up_frac(G, rho):
	#~ for i in G:
		#~ G.node[i]['state'] = 0
#~ 
	#~ r = rd.randint(0,len(G)-1)
	#~ for i in range(int(math.ceil(rho*(len(G))))):
		#~ G.node[r]['state'] = 1
		#~ r = rd.randint(0,len(G)-1)
		#~ while G.node[r]['state'] == 1:
			#~ r = rd.randint(0,len(G)-1)
			#~ if G.node[r]['state'] == 0:
				#~ break
#~ 
