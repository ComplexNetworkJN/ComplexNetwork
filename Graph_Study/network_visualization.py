'''
Created on Jan 8, 2019

@author: wangweisheng
'''
import networkx as nx
f='b.net'


# Creating a Graph
G = nx.Graph() # Right now G is empty
file=open(f)

f=iter(file)
num_nodes=int(next(f))
for i in range(0,num_nodes):
    G.add_node(int(i))

for line in f:
    start_node,end_node=[i for i in line.rstrip().split('\t')]

    G.add_edge(start_node,end_node)
#print(list(nx.connected_components(G)))
print(len(list(nx.connected_components(G))))

import matplotlib.pyplot as plt
nx.draw(G,with_label=True)
#nx.random_layout(G)
plt.show()
file.close()
