# goit-algo-hw-06

### Comparison of DFS and BFS Paths in the Social Network Graph

Based on the analysis of the results obtained:

- **DFS Paths**: 
    - ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    - ['Alice', 'Charlie', 'David', 'Eve']

- **BFS Paths**: 
    - ['Alice', 'Charlie', 'David', 'Eve']
    - ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

#### Differences in Paths:

1. **Order of Nodes Visited**:
   - DFS explores one branch of the graph until it reaches the end node or a dead end, then backtracks. As a result, it may find paths that are not necessarily the shortest. In this case, DFS first explores the path 'Alice' -> 'Bob' -> 'Charlie' -> 'David' -> 'Eve' before backtracking and exploring 'Alice' -> 'Charlie' -> 'David' -> 'Eve'.
   - BFS, on the other hand, explores all neighboring nodes of the current node before moving to the next level of nodes. It always finds the shortest path first. Thus, it first explores the path 'Alice' -> 'Charlie' -> 'David' -> 'Eve', which is shorter, before exploring the longer path 'Alice' -> 'Bob' -> 'Charlie' -> 'David' -> 'Eve'.

2. **Length of Paths**:
   - The paths obtained from DFS may not be the shortest possible paths between the start and end nodes. In this case, the first path found by DFS ('Alice' -> 'Bob' -> 'Charlie' -> 'David' -> 'Eve') is longer than the path found by BFS ('Alice' -> 'Charlie' -> 'David' -> 'Eve').
   - BFS always finds the shortest path first, which ensures that the paths obtained are the shortest possible paths between the start and end nodes. Therefore, the path found by BFS ('Alice' -> 'Charlie' -> 'David' -> 'Eve') is shorter than the one found by DFS.

#### Conclusion:
DFS may find paths that are not necessarily the shortest, while BFS always finds the shortest path first due to their traversal strategies.

