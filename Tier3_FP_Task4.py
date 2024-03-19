import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_node(heap, key, index=0, color="skyblue"):
    if index < len(heap):
        node = Node(key, color)
        heap[index] = node
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        if left_index < len(heap):
            node.left = add_node(heap, heap[left_index].val, left_index)
        if right_index < len(heap):
            node.right = add_node(heap, heap[right_index].val, right_index)
        return node
    return None

def create_heap_from_list(lst):
    heap = [None] * len(lst)
    for i, item in enumerate(lst):
        heap[i] = Node(item) 
    root = add_node(heap, heap[0].val) 
    return root

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Використовуємо функцію draw_tree без змін для відображення купи
def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Створення бінарної купи зі списку
heap_list = [0, 4, 1, 5, 10, 3] 
root = create_heap_from_list(heap_list)

# Відображення бінарної купи
draw_tree(root)
