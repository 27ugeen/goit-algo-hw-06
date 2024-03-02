import networkx as nx
import matplotlib.pyplot as plt

# Creating the social network graph (same as in Task 1)
social_network = nx.Graph()
social_network.add_nodes_from([
    ('Alice', {'age': 30, 'gender': 'female'}),
    ('Bob', {'age': 25, 'gender': 'male'}),
    ('Charlie', {'age': 35, 'gender': 'male'}),
    ('David', {'age': 40, 'gender': 'male'}),
    ('Eve', {'age': 28, 'gender': 'female'})
])
social_network.add_edges_from([
    ('Alice', 'Bob'),
    ('Alice', 'Charlie'),
    ('Bob', 'Charlie'),
    ('David', 'Charlie'),
    ('David', 'Eve')
])

# Visualizing the graph
nx.draw(social_network, with_labels=True, node_size=1000, node_color='lightblue', font_size=12, font_weight='bold')
plt.title("Social Network")
plt.show()

# Function to find paths using Depth-First Search (DFS)
def dfs_paths(graph, start, end, path=None):
    if path is None:
        path = [start]
    if start == end:
        yield path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            yield from dfs_paths(graph, neighbor, end, path + [neighbor])

# Function to find paths using Breadth-First Search (BFS)
def bfs_paths(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == end:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Finding paths using DFS and BFS
start_node = 'Alice'
end_node = 'Eve'
dfs_result = list(dfs_paths(social_network, start_node, end_node))
bfs_result = list(bfs_paths(social_network, start_node, end_node))

# Comparing the results of both algorithms
print("DFS Paths:", dfs_result)
print("BFS Paths:", bfs_result)

# Explanation of the differences in paths obtained
print("\nExplanation:")
print("DFS explores one branch of the graph until it reaches the end node or a dead end, then backtracks.")
print("BFS explores all neighboring nodes of the current node before moving to the next level of nodes.")
print("As a result, DFS may find a path that is not the shortest, while BFS always finds the shortest path first.")
