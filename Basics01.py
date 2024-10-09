#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install networkx')


# In[39]:


import networkx as nx
import matplotlib.pyplot as plt

# Create the graph
G = nx.Graph()

# Add nodes
G.add_node("BOB")
G.add_node("ALICE")
G.add_node("CARL")
G.add_node("FRANK")
G.add_node("DUKE")

# Add edges with attributes
G.add_edge("BOB", "ALICE", relationship="friends")
G.add_edge("BOB", "CARL", relationship="siblings")
G.add_edge("BOB", "DUKE", relationship="siblings")
G.add_edge("CARL", "ALICE", relationship="married")
G.add_edge("FRANK", "ALICE", relationship="friends")
G.add_edge("DUKE", "ALICE", relationship="married")
G.add_edge("FRANK", "DUKE", relationship="siblings")
G.add_edge("CARL", "FRANK", relationship="friends")

# Prepare labels for the nodes (using the node names directly)
labels = {node: node for node in G.nodes}

# Prepare labels for the edges (using the relationship attribute)
edge_labels = {(u, v): data['relationship'] for u, v, data in G.edges(data=True)}

# Draw the graph with names as node labels
pos = nx.spring_layout(G)  # Positions for all nodes
nx.draw(G, pos, labels=labels, with_labels=True, node_color="pink", node_size=3000, font_color="black", font_size=10, font_family="Times New Roman", font_weight="bold")

# Draw edge labels
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')

plt.margins(0.2)
plt.show()


# In[54]:


import networkx as nx
import pandas as pd
node_df=pd.read_csv(r"C:\Users\Admin\Desktop\nodes.csv")
edges_df=pd.read_csv(r"C:\Users\Admin\Desktop\edges.csv")

G = nx.Graph()

for index, row in node_df.iterrows():
    G.add_node(row['node_id'], attribute=row['attribute'])


for index, row in edges_df.iterrows():
    G.add_edge(row['source'], row['target'], weight=row['weight'])


plt.figure(figsize=(6, 6))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=10)
plt.show()


# In[10]:


import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3,4])

G.add_edge(1,2)
G.add_edges_from([(2,3),(3,4)])
nx.draw(G,with_labels=True)
plt.show()



# In[31]:


#create graph and add nodes with attributes 
G=nx.Graph()
G.add_node(1,name="alice",age=25)
G.add_node(2,name="bob",age=30)
G.add_node(3,name="david",age=22)
G.add_node(4,name="carl",age=34)
G.add_edge(1,2,relationship="friends")
G.add_edge(2,3,relationship="siblings")
G.add_edge(3,4,relationship="frineds")
#access node and edges attribute
print(G.nodes[1]['name'])
print(G.nodes[2]['name'])
print(G.nodes[3]['name'])
print(G.nodes[4]['name'])
print(G.edges[1,2]['relationship'])
print(G.edges[2,3]['relationship'])
print(G.edges[3,4]['relationship'])

# Prepare labels for the nodes
labels = {1: G.nodes[1]['name'], 
          2: G.nodes[2]['name'], 
          3: G.nodes[3]['name'], 
          4: G.nodes[4]['name']}

# Draw the graph with names as labels
nx.draw(G, labels=labels, with_labels=True, node_color="ORANGE", node_size=3000, font_color="white", font_size=20, font_family="Times New Roman", font_weight="bold")
plt.margins(0.2)
plt.show()


# In[ ]:




