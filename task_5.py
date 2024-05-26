import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4()) 

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)
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

def dfs_traversal(node, visited, colors):
    if node is not None:
        visited.append(node)
        colors[node.id] = '#{:06x}'.format(0xffffff - len(visited) * 0x111111)
        dfs_traversal(node.left, visited, colors)
        dfs_traversal(node.right, visited, colors)

def bfs_traversal(node, colors):
    visited = []
    queue = [node]

    while queue:
        current = queue.pop(0)
        visited.append(current)
        colors[current.id] = '#{:06x}'.format(0xffffff - len(visited) * 0x111111)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

def draw_tree(tree_root, traversal_type):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = {}
    if traversal_type == 'dfs':
        dfs_traversal(tree_root, [], colors)
    elif traversal_type == 'bfs':
        bfs_traversal(tree_root, colors)

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=list(colors.values()))
    plt.show()

root = Node(0)
root.left = Node(1)
root.left.left = Node(2)
root.left.right = Node(3)
root.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

draw_tree(root, 'dfs')
draw_tree(root, 'bfs')
