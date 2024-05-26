import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append((to_node, distance))
        self.edges[to_node].append((from_node, distance))
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

def dijkstra(graph, initial):
    visited = {node: float('inf') for node in graph.nodes}
    visited[initial] = 0
    path = {node: None for node in graph.nodes}

    priority_queue = [(0, initial)]
    heapq.heapify(priority_queue)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > visited[current_node]:
            continue

        for neighbor, weight in graph.edges[current_node]:
            distance = current_distance + weight

            if distance < visited[neighbor]:
                visited[neighbor] = distance
                path[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return visited, path

def main():
    graph = Graph()
    nodes = ['A', 'B', 'C', 'D', 'E']
    for node in nodes:
        graph.add_node(node)

    edges = [
        ('A', 'B', 1),
        ('A', 'C', 4),
        ('B', 'C', 2),
        ('B', 'D', 5),
        ('C', 'D', 1),
        ('D', 'E', 3),
        ('C', 'E', 7)
    ]

    for edge in edges:
        graph.add_edge(*edge)

    initial_node = 'A'
    distances, paths = dijkstra(graph, initial_node)

    print(f"Найкоротші шляхи від вершини {initial_node}:")
    for node in distances:
        print(f"Відстань до {node}: {distances[node]}")
        print(f"Шлях: {get_path(paths, initial_node, node)}")

def get_path(paths, start, end):
    path = []
    while end is not None:
        path.append(end)
        end = paths[end]
    path.reverse()
    return path

if __name__ == "__main__":
    main()
