from collections import OrderedDict

colors = ['yellow', 'red', 'green', 'blue', 'black']

graph_z_tablicy = {
    'A': ['H', 'B'],
    'B': ['A', 'D'],
    'C': ['D'],
    'D': ['C', 'I', 'K'],
    'E': ['F', 'K'],
    'F': ['E', 'G'],
    'G': ['F', 'K', 'H'],
    'H': ['G', 'K', 'J', 'I', 'A'],
    'I': ['H', 'J', 'D'],
    'J': ['K', 'I', 'H'],
    'K': ['G', 'H', 'J', 'E', 'D']
}

graph_z_tablicy = OrderedDict(sorted(graph_z_tablicy.items(), key=lambda v: len(v[1]), reverse=True))

wierzcholki = list(graph_z_tablicy.keys())
M = [ [0]*len(wierzcholki) for _ in range(len(wierzcholki)) ]
for a,b in [(wierzcholki.index(name), wierzcholki.index(vertex)) for name, vertices in graph_z_tablicy.items() for vertex in vertices]:
   M[a][b] = 1

def welsh_powell(graph):
    color_list = [None] * len(graph)
    color_list[0] = 0

    for v in range(1, len(graph)):
        used = [False] * len(graph)
        neighbours = [x for x in range(len(graph)) if graph[v][x] == 1]
        for i in neighbours:
            if color_list[i] is not None:
                used[color_list[i]] = True

        free_color = 0

        while used[free_color]:
            free_color += 1

        color_list[v] = free_color

    return color_list


print(graph_z_tablicy)

colors_for_graph1 = welsh_powell(M)
print([colors[i] for i in colors_for_graph1])
