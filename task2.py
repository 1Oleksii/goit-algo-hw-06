import networkx as nx
from collections import deque

# Створюємо граф
G = nx.Graph()

# Додаємо вершини (станції метро)
stations = [
    "Akademmistechko", "Zhytomyrska", "Sviatoshyn", "Nyvky", "Beresteiska",
    "Shuliavska", "Politekhnichnyi Instytut", "Vokzalna", "Universytet", "Teatralna"
]
G.add_nodes_from(stations)

# Додаємо ребра (зв'язки між станціями)
edges = [
    ("Akademmistechko", "Zhytomyrska"),
    ("Zhytomyrska", "Sviatoshyn"),
    ("Sviatoshyn", "Nyvky"),
    ("Nyvky", "Beresteiska"),
    ("Beresteiska", "Shuliavska"),
    ("Shuliavska", "Politekhnichnyi Instytut"),
    ("Politekhnichnyi Instytut", "Vokzalna"),
    ("Vokzalna", "Universytet"),
    ("Universytet", "Teatralna")
]
G.add_edges_from(edges)

# Реалізація алгоритму пошуку в глибину (DFS)
def dfs(graph, start, goal, path=None, visited=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    visited.add(start)
    path = path + [start]
    if start == goal:
        return path
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, path, visited)
            if new_path:
                return new_path
    return None

# Реалізація алгоритму пошуку в ширину (BFS)
def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph.neighbors(vertex):
                if neighbor == goal:
                    return path + [neighbor]
                else:
                    queue.append((neighbor, path + [neighbor]))
    return None

# Визначаємо початкову і кінцеву станцію
start_station = "Akademmistechko"
end_station = "Teatralna"

# Шлях DFS
dfs_path = dfs(G, start_station, end_station)
print("Шлях DFS:", dfs_path)

# Шлях BFS
bfs_path = bfs(G, start_station, end_station)
print("Шлях BFS:", bfs_path)
