import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations

def load_dataset(file_path): #load the dataset
    dataset = pd.read_csv(file_path, header=None, sep='\s+')
    return dataset.values.tolist()
def calculate_total_distance(path, graph):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]
    return total_distance

def dfs(graph, current_node, visited, path, visualize=True):
    num_nodes = len(graph)

    visited[current_node] = True
    path.append(current_node)

    # Visualization setup
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))
    edge_labels = {}

    if visualize:
        pos = nx.spring_layout(G)

    for i in range(len(path) - 1):
        G.add_edge(path[i], path[i + 1])
        edge_labels[(path[i], path[i + 1])] = graph[path[i]][path[i + 1]]

    if visualize:
        nx.draw(G, pos, with_labels=True, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show()

    if len(path) == num_nodes:
        return path

    for neighbor in range(num_nodes):
        if not visited[neighbor]:
            dfs_result = dfs(graph, neighbor, visited.copy(), path.copy(), visualize)
            if dfs_result:
                return dfs_result

    return None