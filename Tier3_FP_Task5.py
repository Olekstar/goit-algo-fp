import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def visualize_tree(tree, traversal_order, traversal_type):
    G = nx.DiGraph()
    colors = []
    pos = {}
    def plot(node, depth=0, pos_x=0):
        if node is not None:
            G.add_node(node.val)
            pos[node.val] = (pos_x, -depth)
            if node in traversal_order:
                # Генерація кольору в залежності від позиції вузла в обході
                idx = traversal_order.index(node)
                colors.append((0.1 + 0.9 * (idx / len(traversal_order)), 0.1, 0.9 - 0.9 * (idx / len(traversal_order)), 1.0))
            else:
                colors.append((0.1, 0.1, 0.1, 1.0))
            if node.left:
                G.add_edge(node.val, node.left.val)
                plot(node.left, depth + 1, pos_x - 1/(2**depth))
            if node.right:
                G.add_edge(node.val, node.right.val)
                plot(node.right, depth + 1, pos_x + 1/(2**depth))
    plot(tree)
    nx.draw(G, pos, with_labels=True, node_color=colors)
    plt.title(f'Tree Traversal: {traversal_type}')
    plt.show()

def dfs(node, visited=None):
    if visited is None:
        visited = []
    if node:
        visited.append(node)
        dfs(node.left, visited)
        dfs(node.right, visited)
    return visited

def bfs(root):
    visited = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            visited.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return visited

# Створення дерева та виконання обходу
root = None
for key in [5, 3, 7, 2, 4, 6, 8]:
    root = insert(root, key)

dfs_order = dfs(root)
bfs_order = bfs(root)

# Візуалізація
visualize_tree(root, dfs_order, "DFS")
visualize_tree(root, bfs_order, "BFS")
