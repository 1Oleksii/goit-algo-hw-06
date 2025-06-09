import heapq
import matplotlib.pyplot as plt
import networkx as nx

class MetroGraph:
    def __init__(self):
        self.graph = {}
        
    def add_station(self, name):
        if name not in self.graph:
            self.graph[name] = {}
    
    def add_connection(self, station1, station2, distance):
        self.graph[station1][station2] = distance
        self.graph[station2][station1] = distance
    
    def dijkstra(self, start):
        distances = {station: float('infinity') for station in self.graph}
        distances[start] = 0
        previous = {station: None for station in self.graph}
        
        priority_queue = [(0, start)]
        
        while priority_queue:
            current_distance, current_station = heapq.heappop(priority_queue)
            
            if current_distance > distances[current_station]:
                continue
                
            for neighbor, weight in self.graph[current_station].items():
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_station
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances, previous
    
    def get_shortest_path(self, start, end):
        distances, previous = self.dijkstra(start)
        path = []
        current = end
        
        if previous[current] is None and current != start:
            return None, float('infinity')
            
        while current is not None:
            path.append(current)
            current = previous[current]
            
        path.reverse()
        return path, distances[end]
    
    def get_all_shortest_paths(self):
        all_paths = {}
        for station in self.graph:
            distances, _ = self.dijkstra(station)
            all_paths[station] = distances
        return all_paths
    
    def visualize(self):
        G = nx.Graph()
        
        for station in self.graph:
            G.add_node(station)
            for neighbor, weight in self.graph[station].items():
                G.add_edge(station, neighbor, weight=weight)
        
        pos = nx.spring_layout(G, seed=42)
        plt.figure(figsize=(12, 7))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', 
                node_size=2500, font_weight='bold')
        
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        
        plt.title("Граф метро Києва з вагами ребер")
        plt.show()

# Створення графа метро
metro = MetroGraph()

# Додавання станцій
stations = [
    "Akademmistechko", "Zhytomyrska", "Sviatoshyn", "Nyvky", "Beresteiska",
    "Shuliavska", "Politekhnichnyi Instytut", "Vokzalna", "Universytet", "Teatralna"
]
for station in stations:
    metro.add_station(station)

# Додавання з'єднань
connections = [
    ("Akademmistechko", "Zhytomyrska", 2),
    ("Zhytomyrska", "Sviatoshyn", 3),
    ("Sviatoshyn", "Nyvky", 4),
    ("Nyvky", "Beresteiska", 2),
    ("Beresteiska", "Shuliavska", 1),
    ("Shuliavska", "Politekhnichnyi Instytut", 3),
    ("Politekhnichnyi Instytut", "Vokzalna", 2),
    ("Vokzalna", "Universytet", 3),
    ("Universytet", "Teatralna", 2)
]
for conn in connections:
    metro.add_connection(*conn)

# Візуалізація графа
metro.visualize()

# Демонстрація роботи алгоритму
print("Демонстрація роботи алгоритму Дейкстри:\n")

# Приклади конкретних маршрутів
example_routes = [
    ("Akademmistechko", "Teatralna"),
    ("Zhytomyrska", "Universytet"),
    ("Sviatoshyn", "Politekhnichnyi Instytut"),
    ("Nyvky", "Vokzalna")
]

for start, end in example_routes:
    path, distance = metro.get_shortest_path(start, end)
    print(f"Найкоротший шлях з {start} до {end}:")
    print(" -> ".join(path))
    print(f"Загальна відстань: {distance}\n")

# Матриця найкоротших відстаней між першими 5 станціями
print("Матриця найкоротших відстаней (перші 5 станцій):")
header = "Станція".ljust(20) + "".join([f"{s[:10]:>12}" for s in stations[:5]])
print(header)
print("-" * len(header))

for i, start in enumerate(stations[:5]):
    row = f"{start[:19]:<20}"
    for j, end in enumerate(stations[:5]):
        if i <= j:
            _, distance = metro.get_shortest_path(start, end)
            row += f"{distance:>12}"
        else:
            row += " " * 12
    print(row)

# Інформація про кількість можливих маршрутів
total_pairs = len(stations) * (len(stations) - 1) // 2
print(f"\nЗагальна кількість можливих маршрутів між станціями: {total_pairs}")