colors = ['yellow', 'red', 'green', 'blue', 'black'] 

graph1 = [ #macierz opisujaca graf 1
    [0,1,1,0,0],
    [1,0,1,1,0],
    [1,1,0,1,0],
    [0,1,1,0,1],
    [0,0,0,1,0]
    ]

graph2 = [ #macierz opisujaca graf 2
    [0,1,1,0,0],
    [1,0,1,1,0],
    [1,1,0,1,0],
    [0,0,0,0,1],
    [0,1,1,1,0]
    ]

def color_graph(graph):
    color_list = [None] * len(graph) 
    color_list[0] = 0 
    for v in range(1, len(graph)): 
        used = [False] * len(graph) 
        neighbours = [x for x in range(len(graph)) if graph[v][x]==1]
        for i in neighbours: 
            if color_list[i] != None: 
                used[color_list[i]] = True 
        free_color = 0 
        while used[free_color]: 
            free_color += 1 
        color_list[v] = free_color
    return color_list

colors_for_graph1 = color_graph(graph1)
print([colors[i] for i in colors_for_graph1])

colors_for_graph2 = color_graph(graph2)
print([colors[i] for i in colors_for_graph2])