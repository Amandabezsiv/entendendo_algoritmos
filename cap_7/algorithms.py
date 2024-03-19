def dijkstra(graph, origin, destiny):
    """
    dijkstra: shortest path from one node to all nodes
    args:
        graph Dict[List<Tuple>]: adjacency dict representation of a graph
        origin Int: vertex representing origin to dijkstra algorithm
        destiny Int: vertex representing destiny to dijkstra algorithm
    complexity: O(V)
    """
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


def floyd_warshal(graph):
    """
    floyd_warshal: shortest path from all pairs of nodes, negative weight allowd
    args:
        graph Dict[List<Tuple>]: adjacency dict representation of a graph
    complexity: O(V^3)
    """

    n_vertex = len(graph)
    distance_v = [[float('inf') for i in range(n_vertex)] for j in range(n_vertex)]

    for v in range(n_vertex):
        distance_v[v][v] = 0

    for u in graph:
        for edge in graph[u]:
            v, weight = edge
            distance_v[u-1][v-1] = weight
            distance_v[v-1][u-1] = weight

    for k in range(n_vertex):
        for i in range(n_vertex):
            for j in range(n_vertex):
                if distance_v[i][j] > distance_v[i][k] + distance_v[k][j]:
                    distance_v[i][j] = distance_v[i][k] + distance_v[k][j]
                    distance_v[j][i] = distance_v[i][k] + distance_v[k][j]

    return distance_v                          
                
    

g = {1: [(2, 1), (3, 5)], 2: [(4, 100)], 3: [(4, 5)], 4: []}
print(f'Graph {g} \n')

print('Dijkstra origin(1) source(4)')
print(dijkstra(g,1,4), '\n')

print('Floyd-warshal')      
for i in floyd_warshal(g):
    print(i)


