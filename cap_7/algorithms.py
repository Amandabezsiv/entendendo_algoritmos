def dijkstra(graph, origin, destiny):
    best_path = [float("inf")] * len(graph)
    best_path[origin - 1] = 0

    queue = [origin]

    while queue:
        current_node = queue.pop(0)

        if current_node == destiny:
            break

        for vertex, weight in graph[current_node]:
            new_weight = weight + best_path[current_node - 1]
            if new_weight < best_path[vertex - 1]:
                best_path[vertex - 1] = new_weight
                queue.append(vertex)

    return best_path


g = {1: [(2, 1), (3, 5)], 2: [(4, 100)], 3: [(4, 5)], 4: []}
print(dijkstra(g, 1, 4))
