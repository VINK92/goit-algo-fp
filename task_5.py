import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    node_colors = [colors[node] for node in tree.nodes()]

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

def bfs(root):
    queue = deque([root])
    visited = set()
    order = []
    while queue:
        node = queue.popleft()
        if node and node.id not in visited:
            visited.add(node.id)
            order.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return order

def dfs(root):
    stack = [root]
    visited = set()
    order = []
    while stack:
        node = stack.pop()
        if node and node.id not in visited:
            visited.add(node.id)
            order.append(node)
            stack.append(node.right)
            stack.append(node.left)
    return order

def generate_colors(order):
    base_color = 0x1296F0
    colors = {}
    for i, node in enumerate(order):
        color = f"#{base_color + i * 0x101010:06X}"
        colors[node.id] = color
    return colors

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Візуалізація обходу в ширину (BFS)
bfs_order = bfs(root)
bfs_colors = generate_colors(bfs_order)
print("BFS Order:")
for node in bfs_order:
    print(node.val, end=" ")
print("\n")

draw_tree(root, bfs_colors)

# Візуалізація обходу в глибину (DFS)
dfs_order = dfs(root)
dfs_colors = generate_colors(dfs_order)
print("DFS Order:")
for node in dfs_order:
    print(node.val, end=" ")
print("\n")

draw_tree(root, dfs_colors)
