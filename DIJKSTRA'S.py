import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import heapq

def load_dataset(file_path):                #load dataset
    dataset = pd.read_csv(file_path, header=None, sep='\s+')
    return dataset.values.tolist()

def calculate_total_distance(path, graph):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]
    return total_distance
def dijkstra(graph, start):
    num_nodes = len(graph)
    distances = [float('inf')] * num_nodes
    distances[start] = 0
    visited = [False] * num_nodes
    heap = [(0, start)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if visited[current_node]:
            continue

        visited[current_node] = True

        for neighbor in range(num_nodes):
            if not visited[neighbor]:
                new_distance = current_distance + graph[current_node][neighbor]

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(heap, (new_distance, neighbor))

    return distances
def tsp(graph, visualize=True):
    num_nodes = len(graph)

    # Start from the first node
    start_node = 0

    # Run Dijkstra's algorithm to find the optimal path
    distances = dijkstra(graph, start_node)

    # Find the minimum distance Hamiltonian cycle using the distances
    path = [start_node]
    current_node = start_node

    for _ in range(num_nodes - 1):
        next_node = min((n for n in range(num_nodes) if n not in path), key=lambda x: distances[current_node] + graph[current_node][x])
        path.append(next_node)
        current_node = next_node

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

    total_distance = calculate_total_distance(path, graph)
    print("Optimal Path:", path)
    print("Total Distance:", total_distance)
    return total_distance