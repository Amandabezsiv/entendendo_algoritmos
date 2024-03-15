#Pesquisa em largura

class Queue:
    def __init__(self):
        self.array = []
        self.len = 0

    def __len__(self):
        return self.len            

    def push(self, value):
        self.array.append(value)
        self.len += 1

    def pop(self):
        if self.len > 0:
            self.len -= 1
            return self.array.pop(0)
        raise IndexError('empty queue received a pop.')     
    
        

def best_way(graph, origin, destiny):  

    queue = Queue()
    queue.push((origin, 0, {}))    
    minimum_weight= float('inf')
    
    while len(queue) > 0:
        vertex, edge_wight, neighbor = queue.pop()   
                           
        for next_vertex, current_weight in graph[vertex]:
            if neighbor.get(next_vertex, 0):
                continue

            novo_edge_wight = edge_wight + current_weight

            if next_vertex == destiny:
                minimum_weight = min(novo_edge_wight,minimum_weight)
            else:
                neighbor[next_vertex] = True
                queue.push((next_vertex, novo_edge_wight, neighbor))

    return minimum_weight


print(best_way({1: [(2,10), (3,1)], 2: [(5,200)], 3: [(4,100)], 4: [(5,30)], 5: []},1,5))

