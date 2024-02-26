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