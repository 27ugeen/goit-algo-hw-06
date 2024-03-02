import networkx as nx
import matplotlib.pyplot as plt

# Creating the social network graph with weighted edges
social_network = nx.Graph()
social_network.add_nodes_from([
    ('Alice', {'age': 30, 'gender': 'female'}),
    ('Bob', {'age': 25, 'gender': 'male'}),
    ('Charlie', {'age': 35, 'gender': 'male'}),
    ('David', {'age': 40, 'gender': 'male'}),
    ('Eve', {'age': 28, 'gender': 'female'})
])
social_network.add_weighted_edges_from([
    ('Alice', 'Bob', 2),
    ('Alice', 'Charlie', 1),
    ('Bob', 'Charlie', 3),
    ('David', 'Charlie', 2),
    ('David', 'Eve', 1)
])

# Function to implement Dijkstra's algorithm
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.nodes()}  # Initialize distances to infinity
    distances[start] = 0  # Distance from start node to itself is 0
    visited = set()  # Set to keep track of visited nodes

    while len(visited) < len(graph.nodes()):
        # Select the node with the minimum distance that is not visited
        current_node = min({node: distance for node, distance in distances.items() if node not in visited}, key=distances.get)
        visited.add(current_node)

        # Update distances to its neighbors
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']  # Accessing the weight of the edge
            if neighbor not in visited:
                distances[neighbor] = min(distances[neighbor], distances[current_node] + weight)

    return distances

# Finding the shortest paths from each node to all other nodes
shortest_paths = {}
for node in social_network.nodes():
    shortest_paths[node] = dijkstra(social_network, node)

# Printing the shortest paths
for start_node, distances in shortest_paths.items():
    print(f"Shortest paths from {start_node}:")
    for end_node, distance in distances.items():
        print(f"To {end_node}: {distance}")


# Visualizing the graph
pos = nx.spring_layout(social_network, seed=42)
nx.draw(social_network, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=10, font_weight='bold', width=2)
labels = nx.get_edge_attributes(social_network, 'weight')
nx.draw_networkx_edge_labels(social_network, pos, edge_labels=labels)
plt.title("Social Network with Weighted Edges")
plt.show()