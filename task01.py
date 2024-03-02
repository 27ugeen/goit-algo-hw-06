import networkx as nx
import matplotlib.pyplot as plt

# Creating an empty graph
social_network = nx.Graph()

# Adding nodes (people) to the graph
social_network.add_nodes_from([
    ('Alice', {'age': 30, 'gender': 'female'}),  # Adding node with attributes (age, gender)
    ('Bob', {'age': 25, 'gender': 'male'}),
    ('Charlie', {'age': 35, 'gender': 'male'}),
    ('David', {'age': 40, 'gender': 'male'}),
    ('Eve', {'age': 28, 'gender': 'female'})
])

# Adding edges (connections between people) to the graph
social_network.add_edges_from([
    ('Alice', 'Bob'),
    ('Alice', 'Charlie'),
    ('Bob', 'Charlie'),
    ('David', 'Charlie'),
    ('David', 'Eve')
])

# Analyzing the main characteristics of the graph
print("Number of vertices (nodes):", social_network.number_of_nodes())
print("Number of edges:", social_network.number_of_edges())
print("Degree of vertices:")
for node, degree in social_network.degree():
    print(f"{node}: {degree}")
    
# Visualizing the graph
nx.draw(social_network, with_labels=True, node_size=1000, node_color='lightblue', font_size=12, font_weight='bold')
plt.title("Social Network")
plt.show()


