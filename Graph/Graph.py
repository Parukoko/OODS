def create_adjacency_matrix(pairs):
    # แยกคู่ของ input
    edges = [pair.split() for pair in pairs.split(',')]
    nodes = sorted(set([node for edge in edges for node in edge]))
    node_to_index = {node: i for i, node in enumerate(nodes)}
    n = len(nodes)
    adj_matrix = [[0] * n for _ in range(n)]

    for start, end in edges:
        adj_matrix[node_to_index[start]][node_to_index[end]] = 1

    print(f"    {'  '.join(nodes)}")
    for i, row in enumerate(adj_matrix):
        print(f"{nodes[i]} : {', '.join(map(str, row))}")


inp = input("Enter : ")
create_adjacency_matrix(inp)
