# QRL_graph
Reinforcement Learning for the quantum speedup in the graph

Given a graph, we try to compute the classical and quantum critical time. The definition of the criticial time is defined as the hitting time of the endpoints with the probility bigger than $p_0$. 

### Install

```markdown
pip install qrl_graph==0.0.13
```


### Usage

```python
import numpy as np
from scipy.sparse.csgraph import laplacian
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib 
from qrl_graph.graph_env.graph import Graph

g = np.array([[0, 1, 1, 0],
              [1, 0, 0, 1],
              [1, 0, 0, 1],
              [0, 1, 1, 0]])

g_env = Graph(g=g)
print('Laplacian matrix:\n', g_env.laplacian)

t_cl = g_env.get_classical_time(p0=0.1)
t_q = g_env.get_quantum_time(p0=0.1)

print('Classical time:', t_cl)
print('Quantum time:', t_q)
print('Speed up:', t_cl / t_q)


# uncomment to show the graph
# g_env.show_graph()
```


The results are 
```markdown
Laplacian matrix:
 [[ 2 -1 -1  0]
 [-1  2  0 -1]
 [-1  0  2 -1]
 [ 0 -1 -1  2]]
Classical time: 0.25000000000000006
Quantum time: 0.6000000000000003
Speed up: 0.4166666666666665
```


##### Linear chain 

```python
from qrl_graph.graph_env.graph import Graph
from qrl_graph.utils import construct_linear_graph

N = 40
g = construct_linear_graph(N)

g_env = Graph(g=g)
# print('Laplacian matrix:\n', g_env.laplacian)

p0 = 1.0/(2*N)
t_cl = g_env.get_classical_time(p0=p0)
t_q = g_env.get_quantum_time(p0=p0)

print('Linear chain, N =', N)
print('Classical time:', t_cl)
print('Quantum time:', t_q)
print('Speed up:', t_cl / t_q)
```


#### glued tree

```python
from qrl_graph.graph_env.graph import Graph
from qrl_graph.utils import construct_glued_tree_graph

# this is the height of binary tree, and total height of the glued tree is 2*height
h = 3
g = construct_glued_tree_graph(h)
N = g.shape[0]

g_env = Graph(g=g)
# print('Laplacian matrix:\n', g_env.laplacian)

p0 = 1.0/(2*N)
t_cl = g_env.get_classical_time(p0=p0)
t_q = g_env.get_quantum_time(p0=p0)

print('Glued tree, N =', N)
print('Classical time:', t_cl)
print('Quantum time:', t_q)
print('Speed up:', t_cl / t_q)
```