# Grafos direcionados
# Lista de arestas
# busca O(n)
g = [(1, 2, 10),
     (2, 3, 20)]

print(g)

# Lista de adjacência
# busca O(1)
n_nodes = 3
g = [[0 for i in range(n_nodes)]
     for j in range(n_nodes)]

g[0][1] = 10
g[1][2] = 20

for i in range(n_nodes):
    print(g[i])

# Dicionário de vértices
# busca O(n)
g = {1: [(2, 10)], 2: [(3, 20)], 3: []}
print(g)



# Grafos Bidirecionados
# Lista de arestas
g = [(1, 2, 10),
     (2, 3, 20),
     (2, 1, 10),
     (3, 2, 20)]

print(g)
# Lista de adjacência
n_nodes = 3
g = [[0 for i in range(n_nodes)]
     for j in range(n_nodes)]

g[0][1] = 10
g[1][0] = 10
g[1][2] = 20
g[2][1] = 20

for i in range(n_nodes):
    print(g[i])

# Dicionário de vértices
g = {1: [(2, 10)], 2: [(3, 20), (1, 10)], 3: [(2, 20)]}
print(g)
