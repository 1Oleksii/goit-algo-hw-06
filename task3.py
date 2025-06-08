import networkx as nx
import matplotlib.pyplot as plt

# Створюємо граф
G = nx.Graph()

# Список станцій метро
stations = [
    "Akademmistechko", "Zhytomyrska", "Sviatoshyn", "Nyvky", "Beresteiska",
    "Shuliavska", "Politekhnichnyi Instytut", "Vokzalna", "Universytet", "Teatralna"
]
G.add_nodes_from(stations)

# Додаємо ребра з вагами (ваги - уявна відстань між станціями)
edges = [
    ("Akademmistechko", "Zhytomyrska", 2),
    ("Zhytomyrska", "Sviatoshyn", 3),
    ("Sviatoshyn", "Nyvky", 4),
    ("Nyvky", "Beresteiska", 2),
    ("Beresteiska", "Shuliavska", 1),
    ("Shuliavska", "Politekhnichnyi Instytut", 3),
    ("Politekhnichnyi Instytut", "Vokzalna", 2),
    ("Vokzalna", "Universytet", 3),
    ("Universytet", "Teatralna", 2),
]

G.add_weighted_edges_from(edges)

# Візуалізація графа з вагами ребер
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(12, 7))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2500, font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Граф метро Києва з вагами ребер")
plt.show()

# Функція для знаходження найкоротшого шляху за алгоритмом Дейкстри між двома станціями
def shortest_path_dijkstra(graph, start, end):
    return nx.dijkstra_path(graph, start, end, weight='weight')

# Приклад: знаходимо найкоротший шлях між Академмістечком та Театральною
start_station = "Akademmistechko"
end_station = "Teatralna"
path = shortest_path_dijkstra(G, start_station, end_station)
print(f"Найкоротший шлях від {start_station} до {end_station}: {path}")

# Знаходимо найкоротші шляхи між усіма вершинами (опціонально)
all_shortest_paths = dict(nx.all_pairs_dijkstra_path(G, weight='weight'))
for source, paths in all_shortest_paths.items():
    for target, p in paths.items():
        print(f"Найкоротший шлях з {source} до {target}: {p}")
