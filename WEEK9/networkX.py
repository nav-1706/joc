import networkx as nx

# Create an empty graph
g = nx.Graph()

g2 = nx.complete_graph(20)  #To draw conplete graph --> all nodes drectly connected to every other nodes

g3 = nx.barabasi_albert_graph(50,2)

g4 = nx.gnp_random_graph(25,1)

# Add nodes
g.add_node(1)
g.add_node(2)
g.add_node(3)

# Add edges
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(1, 3)

# Print nodes and edges
print("Nodes:", g.nodes)
print("Edges:", g.edges)

# Visualize the graph
import matplotlib.pyplot as plt
nx.draw(g4)
# nx.draw(g)
# nx.draw(g2)
# nx.draw(g3)
plt.show()