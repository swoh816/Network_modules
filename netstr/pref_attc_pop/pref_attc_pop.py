# Basically preferential attachment model, but it has 'popularity' factor A.
# => p_k ~ A*k_i/sum(ki). (1)
# => this may be able to explain the emergence of 'new star' like facebook. 
# the point of making rule (1) is, because I want to make a rule that enables a node to 'get a huge attention with its emergence'. In short, p_k(t+1) ~ d(the number of new edges at t)/dt is big. Because facebook, and google, that kinds of 'new hubs' could be popular because it attracted AT THE VERY BEGINNING.
