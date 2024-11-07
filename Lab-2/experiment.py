from collections import deque

def bfs_collect_26_paths(graph, start, goal, max_paths=26):
    queue = deque([[start]])
    all_paths = []

    while queue and len(all_paths) < max_paths:
        path = queue.popleft()
        node = path[-1]

        # If we have reached the goal, add the path to all_paths
        if node == goal:
            all_paths.append(path)
        else:
            # Explore all neighbors of the node
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return all_paths

# Updated graph with 'J' as the endpoint goal
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F', 'G'],
    'C': ['F', 'G', 'H'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['K', 'L'],
    'G': ['L', 'M'],
    'H': ['M', 'N'],
    'I': ['N', 'O'],
    'J': [],
    'K': ['P', 'Q'],
    'L': ['Q', 'R'],
    'M': ['R', 'S'],
    'N': ['S', 'T'],
    'O': ['T'],
    'P': ['J'],
    'Q': ['T'],
    'R': ['J'],
    'S': ['J'],
    'T': ['J']
}

start_node = 'A'
goal_node = 'J'
paths = bfs_collect_26_paths(graph, start_node, goal_node)

# Print out the first 26 found paths (or as many as exist)
for i, path in enumerate(paths, start=1):
    print(f"Väg {i}: {path}")
