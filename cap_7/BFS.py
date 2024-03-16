def dijkstra(graph, origin, destiny):
    best_path = [float('inf') for i in range(len(graph))]
    best_path[origin-1] = 0
    
    queue = [origin]
    
    while queue:

        current_node = queue.pop(0)
        lesser_path = float('inf')
        lesser_weight = float('inf')
        
        for vertex, weight in graph[current_node]:

            new_weight = weight + best_path[current_node-1]                   
            best_path[vertex-1] = min(new_weight, best_path[vertex-1])

            if lesser_weight > best_path[vertex-1]:
                lesser_weight = best_path[vertex-1]
                lesser_path = vertex

        if lesser_path != float('inf'):
            queue.append(lesser_path)
            
        
    return best_path
        
        
        
        
    
    

g = {1: [(2,10), (3,1)], 2: [(5,200)], 3: [(4,100)], 4: [(5,30)], 5: []}
print(dijkstra(g,1,5))

