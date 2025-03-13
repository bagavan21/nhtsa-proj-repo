def getMinimumStress(graph_nodes, graph_from, graph_to, graph_weight, source, destination):
    # Initialize distances
    distances = [float('inf')] * (graph_nodes + 1)
    distances[source] = 0

    # Relax edges repeatedly
    for _ in range(graph_nodes):
        for i in range(len(graph_from)):
            u, v, w = graph_from[i], graph_to[i], graph_weight[i]
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    # Return the distance to the destination or -1 if unreachable
    if distances[destination] == float('inf'):
        return -1
    else:
        return distances[destination]

# Example usage
graph_nodes = 5
graph_from = [1, 1, 2, 3]
graph_to = [2, 3, 4, 5]
graph_weight = [2, 3, 1, 4]
source = 1
destination = 5

result = getMinimumStress(graph_nodes, graph_from, graph_to, graph_weight, source, destination)
print(result)  # Output: 7
