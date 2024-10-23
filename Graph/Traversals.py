def create_undirected_graph(pairs):
    edges = [pair.split() for pair in pairs.split(',')]
    graph = {}
    for start, end in edges:
        if start not in graph:
            graph[start] = []
        if end not in graph:
            graph[end] = []
        graph[start].append(end)
        graph[end].append(start)

    for node in graph:
        graph[node].sort()

    return graph

def dfs_full(graph, start, visited):
    stack = [start]
    traversal = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            # Append neighbors in reverse order to ensure smallest nodes are processed first
            stack.extend(reversed([neighbor for neighbor in graph[node] if neighbor not in visited]))

    return traversal

def dfs(graph):
    visited = set()
    traversal = []

    for node in sorted(graph):
        if node not in visited:
            traversal.extend(dfs_full(graph, node, visited))

    return traversal

def bfs_full(graph, start, visited):
    queue = [start]
    traversal = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            queue.extend([neighbor for neighbor in graph[node] if neighbor not in visited])

    return traversal

def bfs(graph):
    visited = set()
    traversal = []

    for node in sorted(graph):
        if node not in visited:
            traversal.extend(bfs_full(graph, node, visited))

    return traversal

if __name__ == "__main__":
	input_data = input("Enter : ")
	graph = create_undirected_graph(input_data)

	dfs_result = dfs(graph)
	print(f"Depth First Traversals : {' '.join(dfs_result)}")

	bfs_result = bfs(graph)
	print(f"Bredth First Traversals : {' '.join(bfs_result)}", end='')
