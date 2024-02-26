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
def tsp(graph, visualize=True):
    num_nodes = len(graph)

    # Start from the first node
    start_node = 0

    # Initialize visited nodes
    visited = [False] * num_nodes

    # Run DFS to find the optimal path
    optimal_path = dfs(graph, start_node, visited, [], visualize)

    if optimal_path is not None:
        print("Optimal Path:", optimal_path)
        total_distance = calculate_total_distance(optimal_path, graph)
        print("Total Distance:", total_distance)
        return total_distance
    else:
        print("No valid path found.")
        return None

# File path to my dataset
file_path = "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/fri26_d.txt"

# Load the dataset
graph_data = load_dataset(file_path)

# Run TSP algorithm with visualization
total_distance = tsp(graph_data, visualize=True)

# Print the total distance
if total_distance is not None:
    print("Total Distance:", total_distance)