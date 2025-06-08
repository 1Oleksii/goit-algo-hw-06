import networkx as nx
import matplotlib.pyplot as plt

# Створюємо порожній граф
G = nx.Graph()

# Додаємо станції метро як вершини графа
stations = [
    "Akademmistechko", "Zhytomyrska", "Sviatoshyn", "Nyvky", "Beresteiska",
    "Shuliavska", "Politekhnichnyi Instytut", "Vokzalna", "Universytet", "Teatralna"
]
G.add_nodes_from(stations)

# Додаємо зв’язки між станціями як ребра графа
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

# Візуалізуємо граф
plt.figure(figsize=(10, 6))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_weight='bold')
plt.title("Лінія метро Києва — Червона лінія")
plt.show()

# Виводимо кількість вершин (станцій)
print("Кількість станцій (вершин):", G.number_of_nodes())

# Виводимо кількість ребер (зв’язків між станціями)
print("Кількість з’єднань (ребер):", G.number_of_edges())

# Виводимо ступінь кожної вершини (скільки з'єднань має кожна станція)
for station, degree in G.degree():
    print(f"Станція: {station}, Ступінь: {degree}")
