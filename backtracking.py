def is_safe(node, graph, colors, color):
    """
    Sprawdza, czy przypisanie koloru do wierzchołka jest bezpieczne.
    """
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def graph_coloring_util(graph, m, colors, node):
    """
    Główna funkcja wykorzystująca backtracking do kolorowania grafu.
    """
    # Jeśli wszystkie wierzchołki zostały pokolorowane, zwróć True
    if node == len(graph):
        return True

    # Próbujemy każdego koloru dla bieżącego wierzchołka
    for color in range(1, m + 1):
        if is_safe(node, graph, colors, color):
            # Przypisz kolor
            colors[node] = color
            
            # Rekurencyjnie sprawdź dla następnych wierzchołków
            if graph_coloring_util(graph, m, colors, node + 1):
                return True

            # Jeśli przypisanie koloru nie powiodło się, wycofaj się
            colors[node] = 0

    # Jeśli żaden kolor nie może zostać przypisany, zwróć False
    return False

def graph_coloring(graph, m):
    """
    Funkcja rozpoczynająca proces kolorowania grafu.

    :param graph: Lista sąsiedztwa reprezentująca graf
    :param m: Liczba dostępnych kolorów
    :return: Lista kolorów przypisana do każdego wierzchołka lub informacja o niepowodzeniu
    """
    # Inicjalizacja listy kolorów dla wierzchołków
    colors = [0] * len(graph)

    # Uruchom algorytm backtracking
    if not graph_coloring_util(graph, m, colors, 0):
        return "Rozwiązanie nie istnieje"

    return colors

# Przykładowe dane wejściowe (graf reprezentowany jako lista sąsiedztwa)
graph = [
    [1, 2, 3],  # Wierzchołek 0 jest połączony z 1, 2, 3
    [0, 2],      # Wierzchołek 1 jest połączony z 0, 2
    [0, 1, 3],   # Wierzchołek 2 jest połączony z 0, 1, 3
    [0, 2]       # Wierzchołek 3 jest połączony z 0, 2
]

# Liczba dostępnych kolorów
m = 3

# Uruchom funkcję kolorowania grafu
result = graph_coloring(graph, m)

print("Kolorowanie grafu:", result)
