import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


def load_dataset(file_path):     #load the dataset
    dataset = pd.read_csv(file_path, header=None, sep='\s+')
    return dataset.values.tolist()
def bfs(graph, visualize=True): #dfs algorithm
    num_nodes = len(graph)

    # Initialize visited nodes and distances
    visited = [False] * num_nodes
    distances = [float('inf')] * num_nodes

    # Start from the first node
    start_node = 0
    visited[start_node] = True
    distances[start_node] = 0

    # Visualization setup
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))
    edge_labels = {}

    # Use deque for the queue to efficiently pop from the left
    queue = deque([start_node])

    while queue:
        current_node = queue.popleft()

        # Visualization: Highlight visited nodes
        if visualize:
            G.nodes[current_node]['visited'] = True
            for neighbor in range(num_nodes):
                if graph[current_node][neighbor] != 0 and not visited[neighbor]:
                    G.add_edge(current_node, neighbor)
                    edge_labels[(current_node, neighbor)] = graph[current_node][neighbor]
        # Explore neighbors
        for neighbor in range(num_nodes):
            if not visited[neighbor]:
                # Calculate total distance for the path
                total_distance = distances[current_node] + graph[current_node][neighbor]

                # Update distance if it is shorter
                if total_distance < distances[neighbor]:
                    distances[neighbor] = total_distance

                # Mark the neighbor as visited and add to the queue
                visited[neighbor] = True
                queue.append(neighbor)
    if visualize:
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold',
                node_color=['red' if G.nodes[node].get('visited') else 'blue' for node in G.nodes()])
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show()

    return distances


# File path to my dataset
file_path = "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/fri26_d.txt"

# Load the dataset
graph_data = load_dataset(file_path)

# Run BFS algorithm with visualization
distances = bfs(graph_data, visualize=True)

# Print the distances
for i, distance in enumerate(distances):
    print(f"Distance from node 0 to node {i}: {distance}")


